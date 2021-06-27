import subprocess
import os
import readline

# --------check what user needs and do it automatically
def check_action(answer):
    if answer == "1":
        option = input("1: Change mac address\n"
                       "2: Wireshark the magician\n"
                       "3: MDK3\n"
                       "4: PRISM-AP\n"
                       "9: Back\n"
                       "Choose: ")
        if option == "1":
            subprocess.call("ifconfig wlan0 down", shell=True)
            subprocess.call("macchanger -r wlan0", shell=True, stdout=file_)
            subprocess.call("service NetworkManager restart", shell=True)
            print("DONE...")
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
                subprocess.call("nmap -sS 192.168.1.*", shell=True, stdout=file_)
            if option_2 == "2":
                print("Executing commands...")
                subprocess.call("nmap -T3 192.168.1.*", shell=True, stdout=file_)
            if option_2 == "3":
                print("Executing commands...")
                subprocess.call("nmap -D 192.168.0.1,192.168.0.2 192.168.1.*", shell=True, stdout=file_)
            if option_2 == "9":
                return
        if option == "2":
            subprocess.call("netdiscover -i wlan0", shell=True, stdout=file_, timeout=20)
        if option == "3":
            web_name = input("Type the Webserver's link or IP: ")
            web_option = input("AVAILABLE OPTIONS:\n"
                               "1: Check for open ports\n"
                               "2: DDOS attack\n"
                               "3: Gather General Information\n"
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




"""
    if answer == "4":
        print("--------OUTPUTS--------")
        option = input("1: SPOOFING\n"
                       "2: WIRELESS ATTACKS\n"
                       "3: GATHER INFO\n"
                       "9: Back\n"
                       "Choose:   ")
        if option == "1":
            print("PRINTING ALL THE OUTPUTS FROM THE SPOOFING CATEGORY\n"
                  "1: output_of_mdk3_script.txt\n"
                  "2: tshark_output.txt")
        if option == "2":
            print("PRINTING ALL OUTPUTS FROM THE WIRELESS ATTACKS CATEGORY\n"
                  "1: WIFITE RESULTS HERE \n")
        if option == "3":
            return
"""


# ---------------------------------LIST OF POSSIBLE HACKS AND APP LOOP-------------------------------------------
list_of_possible_hacks = ("\n1: SPOOFING\n"
                          "2: WIRELESS ATTACKS\n"
                          "3: GATHER INFO\n"
                          "(STOP = '')")
print("------------HACKER MODE-----------")
print("\nRemember to never do any harm and use that for educational purposes... or not at all just let it be.\n"
      "Anyway don't blame the developer for your bullshit, this whole project is only a proof of concept\n")
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