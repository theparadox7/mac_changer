import subprocess
interface = "Wlan0"
new_mac = "00:11:22:33:44:77"
print("[+] Changing MAC adress for "+ interface+" to "+ new_mac)
subprocess.call("ifconfig "+interface+ "down",shell=True)
subprocess.call("ifconfig "+interface+ "hw ether "+ new_mac, shell=True)
subprocess.call("ifconfig "+interface+ "up",shell=True)