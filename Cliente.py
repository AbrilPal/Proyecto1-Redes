# Project No.1
# Author: Abril Palencia
# date: 07/08/2021
# bilographic reference: https://slixmpp.readthedocs.io/en/latest/getting_started/index.html

# Libraries import
import logging
from getpass import getpass
from argparse import ArgumentParser
import slixmpp as xmpp

class Cliente(xmpp.ClientXMPP):
    def __init__(self, jid, password):
        xmpp.ClientXMPP.__init__(self, jid, password)
        self.jid = jid
        self.password = password
        self.add_event_handler("session_start", self.start)
        

    async def start(self, event):
        self.send_presence()

        def mensaje_privado():
            to = input("Para: ")
            msg = input("Mensaje: ")
            self.send_message(mto= to, mbody= msg, mtype='chat')
            print("********* Mensaje enviado exitosamente *********")
            self.disconnect()

        mensaje_privado()
        await self.get_roster()

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