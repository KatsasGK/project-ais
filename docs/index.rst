----------INSTALL------------

1) Download everything from the github link is here -> https://github.com/KatsasGK/project-ais

More info soon....


----------CONTENTS---------

CATEGORIES:

SPOOFING:


1 MAC_ADDEESS_CHANGER_CUSTOM

2 WIRESHARK

3 MDK3

4 Prism-AP

WIRELESS:

1 Wifite

2 Wifi_dos_own

INFO GATHERING:

1 NMAP

2 Net-Discovery

3 WEB_ANALYZER

CUSTOM COMMANDS:

--------OVERCLOCK CPU--------

Cant recommend to overclock the cpu but i had stable results after installing a heatsink + fan.

~$sudo nano /boot/config.txt

#uncomment to overclock the arm. 700 MHz is the default.

over_voltage=2

arm_freq=1800

always test it for yourself to see if its stable

(mine was around 70-71c so with better cooling you can achieve up to 2.0ghz stable, all you have to do is increase over_voltage to max 6 as more than that will void your warranty + arm_freq)