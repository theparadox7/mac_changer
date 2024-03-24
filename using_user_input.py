import subprocess
import optparse

parser = optparse.OptionParser()

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

