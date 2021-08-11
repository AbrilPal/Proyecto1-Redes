# Project No.1
# Author: Abril Palencia
# date: 07/08/2021
# bilographic reference: https://slixmpp.readthedocs.io/en/latest/getting_started/index.html

# Libraries import
import logging
from getpass import getpass
from argparse import ArgumentParser
import slixmpp as xmpp
from Cliente import Cliente

print("********************* Bienvenido *********************")
print()
print("1. Ingresar")
print("2. Registrarse")
print("3. salir")
print()
opcion = int(input("Que opcion quieres? "))

if opcion == 1:
    print()
    print("******* Ingresar a la plataforma *******")
    print()
    Cliente.ingresar()
elif opcion == 2:
    print()
    print("******* Registrarse a la plataforma *******")
    print()
elif opcion == 3:
    exit()