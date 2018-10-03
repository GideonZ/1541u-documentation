
Software IEC Settings
=====================

The Software-IEC module is a serial bus service that can be enabled in the configuration menu. 
This module provides two additional devices on the Commodore serial bus; the IEC bus:

- Virtual drive that gives direct access to the Ultimate file system;
- A virtual printer

+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Menu name                    | Explanation                                                                    | Options           |
|                              |                                                                                | (bold default)    |
+==============================+================================================================================+===================+
| IEC Drive and printer        |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Soft Drive Bus ID            |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Default Path                 |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Printer Bus ID               |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Printer output file          |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Printer output type          |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Printer ink density          |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Printer Emulation            |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Printer Commodore charset    |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Printer Epson charset        |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+
| Printer IBM table 2          |                                                                                |                   |
+------------------------------+--------------------------------------------------------------------------------+-------------------+


**Virtual drive**

The virtual drive can only be used to access files of the file system, through the OPEN/CLOSE commands on the IEC bus. 
By default, the path of the IEC drive is ‘/Usb0’, which is the top most USB connector on the right of the unit. 
This default path can be changed in the configuration menu. 
When the USB drive contains a program ‘TEST.PRG’, it can be loaded with the basic command LOAD”TEST.PRG”,10. 
Similarly, you can save your programs with the SAVE command. When loading the directory (LOAD “$”,10), the path will be shown as disk name.

The command channel 15, can currently only be used to change the current directory. 
Just like on modern systems, “..” is the parent directory and “/” is the root directory:

OPEN 15,10,15,”CD:/USB1/MYPROGRAMS”:CLOSE 15

At this point, the virtual drive is not JiffyDOS compliant.

**Printer**

The virtual printer is a valuable contribution created by René Garcia. 
It takes printer commands from the Commodore 64, and creates a black and white image of the printed graphics and text. 
This image is then saved to the USB flash drive. 

The full documentation of the printer emulation and all of its capabilities and options is available here:

http://1541ultimate.net/content/download/mps_printer_emulation.pdf
