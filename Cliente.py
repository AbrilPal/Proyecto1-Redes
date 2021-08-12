# Project No.1
# Author: Abril Palencia
# date: 07/08/2021
# bilographic reference: https://slixmpp.readthedocs.io/en/latest/getting_started/index.html

# Libraries import
import logging
from getpass import getpass
from argparse import ArgumentParser
import slixmpp as xmpp

logging.basicConfig(level=logging.DEBUG, format="%(levelname)-8s %(message)s")

class Cliente(xmpp.ClientXMPP):
    def __init__(self, jid, password):
        xmpp.ClientXMPP.__init__(self, jid, password)
        self.jid = jid
        self.password = password
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("register", self.registration)
        self.add_event_handler("message", self.mensajes)

    async def start(self, event):
        self.send_presence()

        def mensaje_privado():
            to = input("Para: ")
            msg = input("Mensaje: ")
            self.send_message(mto= to, mbody= msg, mtype='chat')
            print("********* Mensaje enviado exitosamente *********")

        def cerra_sesion():
            self.disconnect()
            print("********* Cerro sesion exitosamente *********")

        def contacto_nuevo():
            usuario = input("Usuario: ")
            self.send_presence_subscription(pto=usuario)
            print("********* Agrego contacto exitosamente *********")

        def eliminar_cuenta():
            self.register_plugin('xep_0030') 
            self.register_plugin('xep_0004')
            self.register_plugin('xep_0077')
            self.register_plugin('xep_0199')
            self.register_plugin('xep_0066')

            # delete logged account
            eliminar = self.Iq()
            eliminar['type'] = 'set'
            eliminar['from'] = self.boundjid.user
            eliminar['register']['remove'] = True
            eliminar.send()
            
            self.disconnect()
            print("********* Elimino la cuenta exitosamente *********")

        def mostrar_contactos():
            print('********* Lista de Contactos *********')
            print()
            contactos = self.client_roster.groups()
            for contacto in contactos:
                for jid in contactos[contacto]:
                    # contacts
                    usuario = self.client_roster[jid]['name']
                    if usuario:
                        pass
                    else:
                        print('Usuario: ', jid)

                    # contact status and info
                    conectados = self.client_roster.presence(jid)
                    for res, pres in conectados.items():
                        show = 'conectado'
                        if pres['show']:
                            show = pres['show']
                        print("     INFO:")
                        print('        ', show)
                        if pres['status']:
                            print('     Estado: ', pres['status'])
            print()
        
        def cambiar_estado():
            estado = input("Coloca el estado que desees: ")
            info = input("Que info deseas mostar: (ej.: chat, conectado): ")
            self.send_presence(pshow=info, pstatus=estado)
            print("********* Se guardo exitosamente *********")

        def detalle_cuenta():
            self.get_roster()
            usuario = input("Usuario: ")
            contactos = self.client_roster.presence(usuario)
            for res, pres in contactos.items():
                show = 'chat'
                if pres['show']:
                    show = pres['show']
                print("     INFO:")
                print('        ', show)
                print('     Estado: ', pres['status'])
            
        # menu
        menu = True
        while menu:
            print()
            print("1. Enviar mensajes directos") # done
            print("2. Mostrar todos los usuarios/contactos y su estado") # done
            print("3. Agregar un usuario a los contactos") # done
            print("4. Mostrar detalles de contacto de un usuario") # done
            print("5. participar en conversaciones grupales")
            print("6. Definir mensaje de presencia") # done
            print("7. Enviar/recibir notificaciones")
            print("8. Enviar/recibir archivos")
            print("9. Eliminar la cuenta del servidor") # done
            print("10. Cerrar sesion") # done
            print("")
            op_menu = int(input("Que opcion quieres? "))

            if op_menu == 1:
                mensaje_privado()
            elif op_menu == 10:
                cerra_sesion()
                menu = False
            elif op_menu == 3:
                contacto_nuevo()
            elif op_menu == 9:
                eliminar_cuenta()
            elif op_menu == 2:
                mostrar_contactos()
            elif op_menu == 6:
                cambiar_estado()
            elif op_menu == 4:
                detalle_cuenta()
            elif op_menu == 5:
                print()
                print("Lo siento, esta opcion no esta disponible en esta version!")
                print()
                pass
            elif op_menu == 7:
                print()
                print("Lo siento, esta opcion no esta disponible en esta version!")
                print()
                pass
            elif op_menu == 8:
                print()
                print("Lo siento, esta opcion no esta disponible en esta version!")
                print()
                pass

            await self.get_roster()

    async def mensajes(self, mensaje):
        logging.info(mensaje)
        print()
        print("            CHAT           ")
        usuario = str(mensaje["from"]).split("/")
        usuario_mostar = usuario[0]
        mensaje = mensaje["body"]
        print(usuario_mostar , ": ", mensaje)
        print()

    async def registration(self, iq):
        self.send_presence()
        self.get_roster()

        resp = self.Iq()
        resp['type'] = 'set'
        resp['register']['username'] = self.boundjid.user
        resp['register']['password'] = self.password

        try:
            await resp.send()
            logging.info("Account created for %s!" % self.boundjid)
        except IqError as e:
            logging.error("Could not register account: %s" %
                    e.iq['error']['text'])
            self.disconnect()

    def ingresar():
        # Setup the command line arguments.
        parser = ArgumentParser(description=Cliente.__doc__)

        # Output verbosity options.
        parser.add_argument("-q", "--quiet", help="set logging to ERROR",
                            action="store_const", dest="loglevel",
                            const=logging.ERROR, default=logging.INFO)
        parser.add_argument("-d", "--debug", help="set logging to DEBUG",
                            action="store_const", dest="loglevel",
                            const=logging.DEBUG, default=logging.INFO)

        usuario = input("Usuario: ")
        password = getpass("Contraseña: ")

        xmpp = Cliente(usuario, password)
        xmpp.register_plugin('xep_0030') 
        xmpp.register_plugin('xep_0199') 

        # Connect to the XMPP server and start processing XMPP stanzas.
        xmpp.connect()
        xmpp.process(forever=False)

    def registo():
        # Setup the command line arguments.
        parser = ArgumentParser(description=Cliente.__doc__)

        # Output verbosity options.
        parser.add_argument("-q", "--quiet", help="set logging to ERROR",
                            action="store_const", dest="loglevel",
                            const=logging.ERROR, default=logging.INFO)
        parser.add_argument("-d", "--debug", help="set logging to DEBUG",
                            action="store_const", dest="loglevel",
                            const=logging.DEBUG, default=logging.INFO)

        usuario = input("Usuario: ")
        password = getpass("Contraseña: ")

        xmpp = Cliente(usuario, password)
        xmpp.register_plugin('xep_0030') 
        xmpp.register_plugin('xep_0004')
        xmpp.register_plugin('xep_0077')
        xmpp.register_plugin('xep_0199')
        xmpp.register_plugin('xep_0066')
        xmpp["xep_0077"].force_registration = True

        # Connect to the XMPP server and start processing XMPP stanzas.
        xmpp.connect()
        xmpp.process(forever=False)
        