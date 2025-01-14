# import needed libraries
import subprocess
import optparse
import re

# function to get the command line arguments
def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change mac address")
	parser.add_option("-m", "--mac", dest="new_mac", help="add the new mac address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error(" Please specify an interface, use --help for more details")
	elif not options.new_mac:
		parser.error(" Please specify a new mac, use --help for more details")
	return options

# function to change the MAC for a specific interface
def change_mac(interface, new_mac):
	print("Changing Mac Changer address for: " + interface + " to " + new_mac)
	
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])
	subprocess.call(["ifconfig", interface])

# gets the current MAC for a specific interface
def get_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	#print(ifconfig_result) ## for testing

	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result)) 

	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("Could not read mac address: ")

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
	print("MAC address was changed successfully to " + current_mac)
else:
	print("MAC address did not change.")