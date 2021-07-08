import subprocess
import os
import readline
import random

# --------check what user needs and do it automatically
def check_action(answer):
    if answer == "1":
        option = input("\n1: Change mac address\n"
                       "2: Wireshark the magician\n"
                       "3: MDK3\n"
                       "4: PRISM-AP\n"
                       "9: Back\n"
                       "Choose: ")
        if option == "1":
            mac_address_list = ["FC:54:CC:27:2B:4A", "09:57:02:44:4F:81", "53:79:FC:2C:DB:95", "F3:17:51:63:BF:83",
                                "7E:A7:48:34:8F:12", "E8:6C:34:77:0C:25", "FA:D1:57:FB:AC:7D", "CE:1C:4C:D0:D3:7B",
                                "19:D3:49:48:51:67", "72:D8:9B:1F:A8:F6", "46:CE:E9:69:38:07", "92:E6:71:AB:7C:45",
                                "0A:27:7F:07:3D:94", "77:2B:9D:40:76:C2", "C7:41:93:24:32:55", "C8:A0:3F:F2:64:21",
                                "5E:2A:49:49:79:F6", "6E:4F:8E:5B:DB:B6", "82:07:F6:58:32:83", "51:F2:DA:5E:BD:CC",
                                "13:86:CC:1E:09:87", "52:A8:F6:E4:30:61", "7D:E4:41:98:65:A8", "82:FC:1C:AB:D6:C8",
                                "57:BF:64:71:28:DC", "F7:A3:81:61:41:88", "70:DA:D7:E4:F0:36", "87:E0:0F:A8:69:2E",
                                "TS:69:BW:96:9D:69", "DF:65:AC:24:H3:20"]
            new_mac = random.choice(mac_address_list)
            subprocess.call("ifconfig wlan0 down", shell=True)
            subprocess.call(["ifconfig", "wlan0", "hw", "ether", new_mac])
            subprocess.call("ifconfig wlan0 up", shell=True)
            print("[+] Changed Mac address successfully to", new_mac)

        if option == "2":
            print("Starting WIRESHARK...")
            subprocess.call("airmon-ng check kill", shell=True)
            subprocess.call("airmon-ng start wlan0", shell=True)
            print("Executing Commands...")
            subprocess.call("tshark -i wlan0 > tshark_output.txt", shell=True)
            subprocess.call("ifconfig wlan0 down", shell=True)
            subprocess.call("iwconfig wlan0 mode managed", shell=True)
            subprocess.call("ifconfig wlan0 up", shell=True)
            subprocess.call("service NetworkManager restart", shell=True)
            print("DONE...\n"
                  "results are stored at /Scripts/tshark_output.txt")
        if option == "3":
            option_2 = input("\nMDK3 has multiple options\n"
                             "1: BEACON FLOOD MODE\n"
                             "2: DEAUTHENTICATION / DISASSOCIATION AMOK MODE\n"
                             "3: AUTHENTICATION DoS MODE\n"
                             "9: Back\n"
                             "CHOOSE: ")
            if option_2 == "1":
                subprocess.call("airmon-ng start wlan0", shell=True)
                print("Executing the commands...ending in 120 seconds")
                subprocess.call("mdk3 mon0 b", shell=True, timeout=120)
                subprocess.call("sudo", shell=True)
                print("DONE...")
            if option_2 == "2":
                subprocess.call("airmon-ng start wlan0", shell=True)
                print("executing commands...ending in 120 seconds")
                subprocess.call("mdk3 mon0 d -c [1,2,3,4,5,6,7,8,9,10,11,12]", shell=True, timeout=120)
                subprocess.call("service NetworkManager restart", shell=True)
                print("DONE...")
            if option_2 == "3":
                subprocess.call("airmon-ng start wlan0", shell=True)
                print("executing commands...ending in 120 seconds")
                subprocess.call("mdk3 mon0 a", shell=True, timeout=120)
                subprocess.call("service NetworkManager restart", shell=True)
                print("DONE...")
            if option_2 == "9":
                return
        if option == "4":
            subprocess.call("prism-ap", shell=True)
        if option == "9":
            return

    if answer == "2":
        option = input("\nWhich of the following:\n"
                       "1: WIFITE \n"
                       "9: Back\n"
                       "Choose: ")
        if option == "1":
                print("STARTING PROCESS...")
                subprocess.call("wifite --kill", shell=True)
                print("DONE...")
        if option == "9":
            return

    if answer == "3":
        option = input("\n1: NMAP\n"
                       "2: Net-Discovery\n"
                       "3: WEBSITE/IP analyze"
                       "9: Back\n"
                       "Choose: ")
        if option == "1":
            print("\nNMAP has multiple options")
            option_2 = input("1: Stealth Scan\n"
                             "2: Aggressive Scan\n"
                             "3: Scan With Decoys\n"
                             "9: Back\n"
                             "Choose:  ")
            if option_2 == "1":
                print("Executing commands...")
                subprocess.call("nmap -sS 192.168.1.*", shell=True)
            if option_2 == "2":
                print("Executing commands...")
                subprocess.call("nmap -T3 192.168.1.*", shell=True)
            if option_2 == "3":
                print("Executing commands...")
                subprocess.call("nmap -D 192.168.0.1,192.168.0.2 192.168.1.*", shell=True)
            if option_2 == "9":
                return
        if option == "2":
            subprocess.call("netdiscover -i wlan0", shell=True, timeout=30)
        if option == "3":
            # FUNCTION THAT CHECKS IF THE IP/WEB IS UP NOW
            web_name = input("Type the Webserver's link or IP: ")
            web_option = input("\nAVAILABLE OPTIONS:\n"
                               "1: Check for open ports\n"
                               "2: DDOS attack\n"
                               "3: Gather General Information\n"
                               "4: Retype IP/WEB address"
                               "9: BACK\n"
                               "Choose: ")
            if web_option == "1":
                return
            if web_option == "2":
                return
            if web_option == "3":
                return
            if web_option == "9":
                return

    if answer == "99":
        print("---------CUSTOM COMMANDS---------")
        cc = "yes"
        while cc != "":
            cc = input("Enter: ")
            subprocess.call(cc, shell=True)

# ---------------------------------LIST OF POSSIBLE HACKS AND APP LOOP-------------------------------------------
list_of_possible_hacks = ("\n1: SPOOFING\n"
                          "2: WIRELESS ATTACKS\n"
                          "3: GATHER INFO\n"
                          "99: CUSTOM COMMANDS\n"
                          "(STOP = '')")
print("------------HACKER MODE-----------")
print("\nRemember to never do any harm and use that for educational purposes... or not at all just leave it here.\n"
      "Anyway don't blame the developer for your bullshit, this whole project is only a proof of concept.\n")
print("-----WHAT DO YOU WANT TO TEST-----")
done = False
while not done:
    print(list_of_possible_hacks)
    answer = input("Choose number (I READ THE WARNING AND IT'S ALL ON ME): ")
    if answer == "":
        done = True
    else:
        check_action(answer)




















# THE EVOLUTION OF PROJECT S. <3
