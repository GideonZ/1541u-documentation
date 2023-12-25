Using WiFi on the Ultimate 64
-----------------------------

Instructions
============

Before the WiFi module on the U64 can be used, it needs to be programmed with a supplied ".esp" file. This file contains
the firmware for the ESP32 module. Without this firmware, the Ultimate is not able to 'talk' with the WiFi module, and
will therefore not detect it, and not be able to set up a network connection.

In order to install the firmware, simply browse to the supplied ".esp" file and select the option "Flash into ESP32".
The ultimate will then start a programming cycle of the module in the application background. The user is still able to
use the ultimate application while the module is being programmed. Do not attempt to access the module during this time.
After about two minutes or so, a popup appears that informs you that programming the ESP32 is complete. From that moment,
the WiFi line in the main screen will be operational.

*Note that the ESP32 only supports WiFi on the 2.4 GHz band. Therefore, this band must be enabled in the configuration
of your accesspoint.*

Setting up a connection
=======================

When the WiFi line in the main screen shows a MAC address, the module has been recognized and is waiting to connect to
a WiFi access point (AP). Take the following steps to connect:

* Select the context menu item "Show APs..". A list appears of access points that the module has found. The list is sorted
  by signal strength, the strongest signals / nearest APs on top.
* Select the network you want to connect to. A popup appears to enter the network password.
* Once you enter the password, you can leave the list of APs by pressing CRSR-LEFT.
* The WiFi should now connect and show an IP address.

Invisible SSIDs
~~~~~~~~~~~~~~~
When you are using an accesspoint where the SSID is not published on the network, you can also manually connect
by entering the SSID and password in the configuration menu. Press F2 to enter the configuration and navigate to
"WiFi Settings". There you can enter the SSID and password manually. Do not forget to also specify the type of
authentication. This is required for a successful connection.


Functionality Available on WiFi
===============================
The WiFi module is used as a transparent network adapter to the Ultimate 64 management application. Therefore, the
WiFi can be used for telnet, ftp, modem emulation and also to connect to the internet with the appropriate software or
built-in functionality such as searching the online Assembly64 database. The WiFi *cannot* be used for streaming
video and audio. This is only available on the LAN port.

Tin Foil Hats
=============
For those that wear tin-foiled hats: When the WiFi module is disabled in the configuration, or by means of the
context menu, the entire WiFi module is in deep sleep mode with all radio circuitry turned off. 

Speaking of tin foils: If your C64 case still has the foil that covers the board, it might be necessary to remove it
for a better WiFi signal.
