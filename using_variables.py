import subprocess

interface = "Wlan0"
new_mac = "00:11:22:33:44:77"


# subprocess.call("ifconfig wlan0 down",shell=True)
# subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66",shell=True)
# subprocess.call("ifconfig wlan0 up",shell=True)

print("[+] Changing MAC adress for "+ interface+" to "+ new_mac)
#this just prints