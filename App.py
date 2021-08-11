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
opcion = input("Que opcion quieres? ")