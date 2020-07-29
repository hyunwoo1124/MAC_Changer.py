

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface to change the MAC address')
    parser.add_option('-m','--mac', dest='new_mac', help="New MAC address to change to")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Please specify an mac, use --help for more information.")
    return options


def change_mac(interface, new_mac):
    print("Changing MAC adress for " + interface + " to " + new_mac)
    subprocess.call(['ifconfig', interface,"down"])
    #print("CHeck 1")
    subprocess.call(['ifconfig', interface,'hw','ether', new_mac])
    #print("Check 2")
    subprocess.call(['ifconfig', interface,'up'])
    #print("CHeck 3")

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    #print(ifconfig_result)


    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Coudld not read MAC address.")

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC: " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interfacChainginge)
if current_mac == options.new_mac:
    print("[+] MAC address was succesfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed. ")
