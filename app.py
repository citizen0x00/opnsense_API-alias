import os
import argparse

#####################CONFIGMODE###########################
opnsense = "10.0.1.1" #IP to the OPNSense on the network
key = "" #Key made in the usersection of OPNSense
secret = #Secretkey made in the usersection of OPNSense
alias = "" #The alias you want to add the IP to | Comment out this if you want to parse the alias as an argument
##########################################################
argParser = argparse.ArgumentParser()
argParser.add_argument("-ip","--ip", help="IP to add to OPNSense")
argParser.add_argument("-a","--alias", help="Alias you want to add the IP to")
args = argParser.parse_args()
ip = args.ip
#alias = args.alias #uncomment out this if you want alias to hardcode the alias
os.system('curl --header "Content-Type: application/json" --basic --user "'+key+'":"'+secret+'" --insecure --verbose --data \'{"address":"'+ip+'"}\' http://'+opnsense+'/api/firewall/alias_util/add/'+alias+'') #Adding IP to alias
os.system('curl -X POST -d "" -k --user "'+key+'":"'+secret+'" http://'+opnsense+'/api/firewall/alias/reconfigure') #"Save/Commiting" the changes

print("\nDone - "+ip+" is added to the alias: "+alias+"!")
