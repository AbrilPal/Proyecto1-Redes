# Project No.1
# Author: Abril Palencia
# date: 07/08/2021

# Libraries import
import logging
from getpass import getpass
from argparse import ArgumentParser
import slixmpp as xmpp

class Cliente(xmpp.ClientXMPP):
    def __init__(self, jid, password):
        xmpp.ClientXMPP.__init__(self, jid, password)