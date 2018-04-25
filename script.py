#!/usr/bin/env python

from blockcypher import get_address_overview
import json
import requests
import argparse

parser = argparse.ArgumentParser(description='Process some arguments.')

parser.add_argument('--crypto', type=str)
parser.add_argument('--wallet', type=str)

args = parser.parse_args()

for arg in vars(args):
    argvalue = getattr(args, arg)
    if str(argvalue) == 'None':
        print "No argument given for " + str(arg)
        exec(arg + " = raw_input('Give value for ' + arg + ': ')")
        #print eval(arg)
        if eval(arg) == "":
            print "No value given, exiting, try again.."
            sys.exit(0)
    else:
        exec(arg + " = argvalue")

oAddressOverview = get_address_overview(wallet, crypto)
print(oAddressOverview['final_balance'])
