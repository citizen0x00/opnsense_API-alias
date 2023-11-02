import os
import argparse

argParser = argparse.ArgumentParser()
argParser.add_argument("-ip","--ip", help="IP to add to OPNSense")
args = argParser.parse_args()
ip = args.ip

opnsense = "10.0.1.1" #IP to the OPNSense on the network
key = "" #Key made in the usersection of OPNSense
secret = #Secretkey made in the usersection of OPNSense

os.system('curl --header "Content-Type: application/json" --basic --user "'+key+'":"'+secret+'" --insecure --verbose --data \'{"address":"'+ip+'"}\' http://'+opnsense+'/api/firewall/alias_util/add/AllovedIPs') #Adding IP to alias
os.system('curl -X POST -d "" -k --user "'+key+'":"'+secret+'" http://'+opnsense+'/api/firewall/alias/reconfigure') #"Save/Commiting" the changes

print("\nDone - "+ip+" is added to alias!")
