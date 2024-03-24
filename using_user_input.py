import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface",help = "interface to Change its MAC")

parser.parse_args()

interface =input("Interface > ")

new_mac = input("New MAC > ")

print("[+] Changing MAC adress for "+ interface+" to "+ new_mac)

# subprocess.call("ifconfig "+interface+ " down ",shell=True)
# subprocess.call("ifconfig "+interface+ " hw ether "+ new_mac, shell=True)
# subprocess.call("ifconfig "+interface+ " up",shell=True)

#handling inputs
subprocess.call(["ifconfig",interface, "down"])
subprocess.call(["ifconfig",interface,"hw", "ether", new_mac])
subprocess.call(["ifconfig",interface, "up"])

