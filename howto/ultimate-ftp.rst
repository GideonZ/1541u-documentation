Ultimate 2/2+/64 FTP Server

The Ultimate devices have a built in FTP server, that is accessible via the Ethernet connection.
Later on the U64 it also will be accessible via the built in WiFi interface.
For the older U2 cart you'll need an additional USB NIC with the ASIX AX88772 (A/B) chipset.

To connect via FTP, you can use any FTP client availble for your operating system (Filezilla, Total Commander, Windows FTP do work fine ...).

To make a connection, enter the IP address that was assigned via DHCP, or that you manualy set in the network client and use any username and password.

As a special feature, you can display *.64 files as directorys via FTP:
-every chosen FTP username enables this feature (*.d64 are shown as directory AND as *.d64 files)
-the username "d64" deactivates the listing of *.d64 files (*.d64 are only shown as directory)
-the username "d642" disables this feature completely, (*.d64 are only shown as files)
