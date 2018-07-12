+-----------------------------+
| Ultimate-II Virtual Printer |
+=============================+
| User’s Guide                |
+-----------------------------+
| René Garcia                 |
+-----------------------------+

+---------------------------------------+--+--+
| Version , February 18\ :sup:`th` 2018 |  |  |
+---------------------------------------+--+--+

All rights reserved.

Table of Contents
=================

`1. Introduction 5 <#introduction>`__

`1.1. Context 5 <#context>`__

`1.2. License 5 <#license>`__

`1.3. Purpose of this document 5 <#purpose-of-this-document>`__

`2. Configuration 6 <#configuration>`__

`2.1. Overview 6 <#overview>`__

`2.2. Enable the printer 6 <#enable-the-printer>`__

`2.3. Printer configuration items 6 <#printer-configuration-items>`__

`3. Using the printer 8 <#using-the-printer>`__

`3.1. Printing from the C64/C128 8 <#printing-from-the-c64c128>`__

`3.2. Flushing the printer spool 8 <#flushing-the-printer-spool>`__

`3.3. Resetting the printer 8 <#resetting-the-printer>`__

`3.4. Performances 8 <#performances>`__

`4. Capabilities 9 <#capabilities>`__

`5. Commodore MPS commands 10 <#commodore-mps-commands>`__

`5.1. Simple example 10 <#simple-example>`__

`5.2. Secondary address 10 <#secondary-address>`__

`5.3. Commands 10 <#commands>`__

`5.3.1. Graphical operations 10 <#graphical-operations>`__

`5.3.2. Paper feeding 14 <#paper-feeding>`__

`5.3.3. Format control 14 <#format-control>`__

`5.3.4. Graphic Bitmap 16 <#graphic-bitmap>`__

`5.3.5. Character creation, Down Line Loading (DLL)
17 <#character-creation-down-line-loading-dll>`__

`6. EPSON FX-80 commands 19 <#epson-fx-80-commands>`__

`6.1. Secondary address 19 <#secondary-address-1>`__

`6.2. Commands 19 <#commands-1>`__

`6.2.1. Graphical operations 19 <#graphical-operations-1>`__

`6.2.2. Paper feeding 23 <#paper-feeding-1>`__

`6.2.3. Format control 24 <#format-control-1>`__

`6.2.4. Graphic Bitmap 26 <#graphic-bitmap-1>`__

`6.2.5. Charset selection 29 <#charset-selection>`__

`6.2.6. Character creation, Down Line Loading (DLL)
30 <#character-creation-down-line-loading-dll-1>`__

`6.2.7. Other commands 31 <#other-commands>`__

`7. IBM Graphics Printer commands 32 <#ibm-graphics-printer-commands>`__

`7.1. Secondary address 32 <#secondary-address-2>`__

`7.2. Commands 32 <#commands-2>`__

`7.2.1. Graphical operations 32 <#graphical-operations-2>`__

`7.2.2. Paper feeding 35 <#paper-feeding-2>`__

`7.2.3. Format control 36 <#format-control-2>`__

`7.2.4. Graphic Bitmap 37 <#graphic-bitmap-2>`__

`7.2.5. Charset selection 38 <#charset-selection-1>`__

`7.2.6. Character creation, Down Line Loading (DLL)
38 <#character-creation-down-line-loading-dll-2>`__

`7.2.7. Other commands 39 <#other-commands-1>`__

`8. IBM Proprinter commands 40 <#ibm-proprinter-commands>`__

`8.1. Secondary address 40 <#secondary-address-3>`__

`8.2. Commands 40 <#commands-3>`__

`8.2.1. Graphical operations 40 <#graphical-operations-3>`__

`8.2.2. Paper feeding 42 <#paper-feeding-3>`__

`8.2.3. Format control 44 <#format-control-3>`__

`8.2.4. Graphic Bitmap 45 <#graphic-bitmap-3>`__

`8.2.5. Charset selection 46 <#charset-selection-2>`__

`8.2.6. Character creation, Down Line Loading (DLL)
46 <#character-creation-down-line-loading-dll-3>`__

`8.2.7. Other commands 47 <#other-commands-2>`__

`9. PETASCII character table 48 <#petascii-character-table>`__

`9.1. USA/UK 48 <#usauk>`__

`9.2. Denmark 49 <#denmark>`__

`9.3. France / Italy 50 <#france-italy>`__

`9.4. Germany 51 <#germany>`__

`9.5. Spain 52 <#spain>`__

`9.6. Sweden 53 <#sweden>`__

`9.7. Switzerland 54 <#switzerland>`__

`10. EPSON FX-80 character table 55 <#epson-fx-80-character-table>`__

`10.1. Basic charset 55 <#basic-charset>`__

`10.2. Extended charset 55 <#extended-charset>`__

`10.3. International charsets changes
55 <#international-charsets-changes>`__

`11. IBM character tables 56 <#ibm-character-tables>`__

`11.1. Table 1 56 <#table-1>`__

`11.2. Table 2 56 <#table-2>`__

`11.2.1. International 1 56 <#international-1>`__

`11.2.2. International 2 57 <#international-2>`__

`11.2.3. Israel 57 <#israel>`__

`11.2.4. Greece 57 <#greece>`__

`11.2.5. Portugal 58 <#portugal>`__

`11.2.6. Spain 58 <#spain-1>`__

`12. Commodore commands reference 59 <#commodore-commands-reference>`__

`13. EPSON FX-80 commands reference
60 <#epson-fx-80-commands-reference>`__

`14. IBM Graphics Printer command reference
62 <#ibm-graphics-printer-commands-reference>`__

`15. IBM Proprinter command reference
64 <#ibm-proprinter-commands-reference>`__

`16. Technical Specifications 66 <#technical-specifications>`__

`17. Print Sample 67 <#print-sample>`__

`18. Document Revisions 68 <#document-revisions>`__

Introduction
============

Context
-------

The virtual printer is an Ultimate-II feature since 3.0 firmware. With
this functionality you can print from your Commodore 64/128 using a
virtual IEC device #4 or #5.

This emulation simulates a Commodore MPS-1230 printer with all the
commands that this printer can understand. Not all commands are executed
as some of them are hardware related and cannot obviously be
implemented. The results are printed to PNG image files, one file per
page. You can also choose to bypass the printer emulation and to send
the raw data from #4 or #5 IEC device to a file.

MPS-1230 was a mid-range black ink ribbon 9 needle matrix printer sold
by Commodore in the late 80’s.

This printer is compatible with nearly all the usual programs that have
been edited for C64/C128. It can interpret 4 printer instruction sets:

-  Commodore MPS-801

-  Epson FX-80

-  IBM Graphics Printer

-  IBM Proprinter

License
-------

Virtual Printer is released under the GNU General Public License 3.0. A
full copy of the license is included in the root of the Ultimate-II
firmware sources.

Purpose of this document
------------------------

This document describes how to use and configure the Ultimate-II
embedded virtual printer.

You will also find all the commands and charsets supported by the
printer. Then you can add printer facility to your own BASIC programs!

Configuration
=============

Overview
--------

You will find all the configuration items for the printer in the IEC
configuration menu.

Enable the printer
------------------

To enable the printer, you need to enable the software IEC feature in
the Ultimate-II:

-  Use the F2 Menu to enter Ultimate-II configuration and then select
   “\ **Software IEC Settings**\ ”

-  Then on item “\ **IEC Drive and Printer**\ ” select “\ **Enabled**\ ”

Printer configuration items
---------------------------

-  | **Printer Bus ID**: 4 or 5 (default is 4)
   | This will assign device ID 4 or 5 to the printer.

-  | **Printer output file**: (default is */SD/*\ printer on Ultimate II
     or */Usb0/printer* on Ultimate II+)
   | You can select file base name that the virtual printer will use to
     create the PNG files. If you choose to generate PNG files they will
     be named *printer-001.png*, *printer-002.png*, and so on. If you
     chose the bypass the emulation and write RAW binary data to disk
     the file will be named *printer* with no extension. When using
     ASCII filter output, extension .\ *txt* will be appended to file
     name.

-  | **Printer output type**: PNG, ASCII or RAW (default is PNG)
   | PNG are images created by the printer emulator each time a page is
     ejected from the printer. Caution, if a file with the same name
     already exists, it will not be overwritten and the page is lost.
     RAW is the data directly sent by the C64/128 to the IEC port and
     recorded as binary to a file. ASCII will keep and convert printable
     characters to ISO8859-1 standard. This output only makes sense if
     you are printing text as you will only get garbage with bitmap. In
     both RAW and ASCII output mode, if the file already exists, the new
     data will be appended to it.

-  | **Printer ink density**: Low, Medium or High (default is Medium)
   | You can consider this as “how strong is the pin impact on the
     paper”. *Low* will only print very small dots and *High* larger
     dots. As a consequence, this will change the resulting contrast.
     *High* gives the best result for DRAFT character mode. *Medium* may
     be well suited for NLQ character mode. Just test and see what match
     your needs. *See table below for samples*.

-  | **Printer emulation**: Commodore MPS, Epson FX-80, IBM Graphics
     Printer, IBM Proprinter (default is Commodore MPS)
   | You can select which instruction set the emulator will recognize.
     Changing from one emulation to another will reset the printer
     attributes but the printer head stays at the same place and the
     page is not ejected.

-  | **Printer Commodore charset:** USA/UK, Denmark, France/Italy,
     Germany, Spain, Sweden, Switzerland (default is USA/UK)
   | Select which charset to use when using Commodore MPS emulation. If
     you don’t know which one to choose, USA/UK is the one you want. See
     Commodore charset description on chapter 19.

-  | **Printer Epson charset:** Basic, USA, France, Germany, England,
     Denmark I, Sweden, Italy, Spain, Japan, Norway, Denmark II (default
     is Basic)
   | Select which charset to use when using Epson FX-80 emulation. See
     Epson charset description on chapter 10.

-  | **Printer IBM table 2:** International 1, International 2, Israel,
     Greece, Portugal, Spain (default is International 1)
   | Select which charset to use for Table2 when using IBM Graphics
     Printer or IBM Proprinter emulation. IBM printers can use 2
     charsets: Table 1 and Table2. Table 1 cannot be modified and is the
     default charset. Table 2 is the one you chose with this parameter.
     See IBM charset description in chapter 11.

+-----------------------+-----------+-----------+-----------+
| Ink Density           | Low       | Medium    | High      |
+=======================+===========+===========+===========+
| Elementary Dot (x1)   | |image0|  | |image1|  | |image2|  |
+-----------------------+-----------+-----------+-----------+
| Elementary Dot (x300) | |image3|  | |image4|  | |image5|  |
+-----------------------+-----------+-----------+-----------+
| Draft text            | |image6|  | |image7|  | |image8|  |
+-----------------------+-----------+-----------+-----------+
| NLQ text              | |image9|  | |image10| | |image11| |
+-----------------------+-----------+-----------+-----------+
| Draft graphic chars   | |image12| | |image13| | |image14| |
+-----------------------+-----------+-----------+-----------+
| NLQ graphic chars     | |image15| | |image16| | |image17| |
+-----------------------+-----------+-----------+-----------+

Using the printer
=================

Printing from the C64/C128
--------------------------

Just use your program and tell it that you have a connected printer
compatible with MPS Commodore series (e.g.: MPS-801/MPS-803 are the most
frequently supported commodore printers).

Flushing the printer spool
--------------------------

The printer has a very small buffer (256 bytes) and some data may still
be in the buffer waiting to be printed when your print job is finished.
The printer doesn’t know that your job is finished and waits for more
data to print until the end of the page.

You need to tell the printer that you want all the buffered data to be
printed and to eject the current page. This works as the *Form Feed*
button on the real MPS-1230 to eject the page.

Go to F5 Menu and select “\ **Flush Printer/Eject Page**\ ”. In PNG
mode, this will make the current page to be written to a file. Next
print job will start on a blank page. In RAW and ASCII mode this will
write the buffered data to the file.

Resetting the printer
---------------------

You may need to reset printer to go back to an initial state. Go to F5
Menu and select “\ **Reset IEC and Printer**\ ”. Current data in printer
buffer is lost. Current page that was being printed is also lost.

Performances
------------

Composing a page full of text and creating the PNG file will need
approximatively 15 seconds on the Ultimate-II (28 seconds using NLQ
mode). You may think it’s slow but this is much faster than a real
MPS-1230 printer (1 min in DRAFT mode, 4 min in NLQ mode) !

The Ultimate-II middle button becomes unresponsive while composing a
page. The green LED on the right of the cartridge is lit when printer is
working. Be patient and look at the activity LED to stop blinking.

RAW and ASCII modes are nearly immediate. There is no process time to
wait.

At this time, with firmware 3.2, The virtual printer is slower on
Ultimate II+ than on Ultimate II as it is using a slower CPU. In fact,
no processor cache is implemented yet in Ultimate II+, this may change
in a future firmware as CPU is implemented in FPGA using VHDL.

Capabilities
============

This table summarize the printer capabilities depending on which printer
emulation is active:

+-------------+-------------+-------------+-------------+-------------+
|             | Commodore   | Epson FX-80 | IBM         | IBM         |
|             | MPS         |             | Graphics    | Proprinter  |
|             |             |             | Printer     |             |
+=============+=============+=============+=============+=============+
| Draft       | •           | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| Double      | •           | •           | •           | •           |
| strike      |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Bold        | •           | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| Italic      | •           | •           | • [2]_      |             |
| *(draft     |             |             |             |             |
| only)*      |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| NLQ         | •           | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| Underline   | •           | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| Double      | •           | •           | •           | •           |
| width       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Superscript | •           | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| Subscript   | •           | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| Reverse     | •           |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Overline    |             |             |             | •           |
+-------------+-------------+-------------+-------------+-------------+
| Backspace   |             | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| Reverse     |             | •           |             |             |
| page feed   |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| CR=CR+LF    | •           |             |             | *optional*  |
+-------------+-------------+-------------+-------------+-------------+
| LF=CR+LF    | •           | •           |             |             |
+-------------+-------------+-------------+-------------+-------------+
| 7 dot BIM   | •           |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| 8 dot BIM   |             | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| 9 dot BIM   |             | •           |             |             |
+-------------+-------------+-------------+-------------+-------------+
| HT Program  |             | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| VT Program  |             | •           |             | •           |
+-------------+-------------+-------------+-------------+-------------+
| 60 dpi BIM  | • *(double  | •           | •           | •           |
|             | width)*     |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| 75 dpi BIM  |             | •           |             |             |
+-------------+-------------+-------------+-------------+-------------+
| 80 dpi BIM  |             | •           |             |             |
+-------------+-------------+-------------+-------------+-------------+
| 90 dpi BIM  |             | •           |             |             |
+-------------+-------------+-------------+-------------+-------------+
| 120 dpi BIM |             | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| 240 dpi BIM |             | •           | •           | •           |
+-------------+-------------+-------------+-------------+-------------+
| Pica        | •           | •           | •           | •           |
| (10cpi)     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Elite       | •           | •           | •           | •           |
| (12cpi)     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Micro       | •           |             |             |             |
| (15cpi)     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Condensed   | •           | •           | •           | •           |
| (17.1cpi)   |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Pica        | •           |             |             |             |
| Compressed  |             |             |             |             |
| (20cpi)     |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Elite       | •           |             |             |             |
| Compressed  |             |             |             |             |
| (24 cpi)    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| Micro       | •           |             |             |             |
| Compressed  |             |             |             |             |
| (30 cpi)    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+

Commodore MPS commands
======================

This chapter describes the commands the printer can understand when
using the Commodore MPS emulation. You will find Commodore BASIC
examples to explain you how to use them. This printer uses PETASCII.

Simple example
--------------

This will print a first line with HELLO WORLD! on it and a second line
with HELLO printed with double width characters.

10 OPEN1,4

20 PRINT#1,”HELLO WORLD!”

30 PRINT#1,CHR$(14)”HELLO”

40 CLOSE1

|image18|

Secondary address
-----------------

Only on Commodore MPS emulation, you can specify an optional secondary
address on OPEN :

-  **0** : Select PETASCII charset with uppercases and graphic chars

-  **7** : Select PETASCII charset with lowercases and uppercases

If no secondary address is specified, 0 is the default.

Commands
--------

Graphical operations
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **ESC g**                         | Select the **Double Strike**      |
|                                   | print mode. Characters are        |
| **27 71**                         | printed twice and paper is lifted |
|                                   | 1/216” between the two passes.    |
| **1Bh 47h**                       |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);chr$(71);”DOUBLE |
|                                   | STRIKE”                           |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image29|                         |
+===================================+===================================+
| **ESC h**                         | Disable **Double Strike** print   |
|                                   | mode                              |
| **27 72**                         |                                   |
|                                   | 10 OPEN1,4,7                      |
| **1Bh 48h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);chr$(72);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **EN ON**                         | Select the **Double Width** print |
|                                   | mode (Enhanced ON)                |
| **14**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **0Eh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(14);”DOUBLE       |
|                                   | WIDTH”                            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image30|                         |
+-----------------------------------+-----------------------------------+
| **EN OFF**                        | Disable the **Double Width**      |
|                                   | print mode (Enhanced OFF)         |
| **15**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **0Fh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(15);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **RVS ON**                        | Select the **Reverse** print      |
|                                   | mode. Each character is printed   |
| **18**                            | in negative.                      |
|                                   |                                   |
| **12h**                           | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(18);”REVERSE”     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image31|                         |
+-----------------------------------+-----------------------------------+
| **RVS OFF**                       | Disable the **reverse** print     |
|                                   | mode                              |
| **146**                           |                                   |
|                                   | 10 OPEN1,4                        |
| **92h**                           |                                   |
|                                   | 20 PRINT#1,CHR$(146);             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC - 1**                       | Select the **Underline** print    |
|                                   | mode for all characters and       |
| **27 45 49**                      | spaces that follow.               |
|                                   |                                   |
| **1Bh 2Dh 31h**                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(45);CHR$(49 |
|                                   | );”UNDERLINE”                     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image32|                         |
+-----------------------------------+-----------------------------------+
| **ESC - 0**                       | Disable the Underline print mode. |
|                                   |                                   |
| **27 45 48**                      | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 2Dh 30h**                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(45);CHR$(48 |
|                                   | );                                |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC e**                         | Select the **Bold** print mode.   |
|                                   |                                   |
| **27 69**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 45h**                       | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(69);”BOLD”  |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image33|                         |
+-----------------------------------+-----------------------------------+
| **ESC f**                         | Disable the Bold print mode.      |
|                                   |                                   |
| **27 70**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 46h**                       | 20 PRINT#1,CHR$(27);CHR$(70);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 4**                         | Select the **Italic** print mode. |
|                                   |                                   |
| **27 52**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 34h**                       | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(52);”ITALIC |
|                                   | ”                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image34|                         |
+-----------------------------------+-----------------------------------+
| **ESC 5**                         | Disable the **Italic** print      |
|                                   | mode.                             |
| **27 53**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 35h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(53);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC [ n**                       | Select the spacing mode depending |
|                                   | on parameter “n” as described on  |
| **27 91 n**                       | this table:                       |
|                                   |                                   |
| **1Bh 5Bh n**                     | +---------+---------+---------+   |
|                                   | | n       | SPACING |             |
|                                   | +=========+=========+=========+   |
|                                   | | 0       | PICA    | 10      |   |
|                                   | |         |         | chars/i |   |
|                                   | |         |         | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 1       | ELITE   | 12      |   |
|                                   | |         |         | chars/i |   |
|                                   | |         |         | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 2       | MICRO   | 15      |   |
|                                   | |         |         | chars/i |   |
|                                   | |         |         | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 3       | CONDENS | 17.1    |   |
|                                   | |         | ED      | chars/i |   |
|                                   | |         |         | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 4       | PICA    | 20      |   |
|                                   | |         | COMPRES | chars/i |   |
|                                   | |         | SED     | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 5       | ELITE   | 24      |   |
|                                   | |         | COMPRES | chars/i |   |
|                                   | |         | SED     | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 6       | MICRO   | 30      |   |
|                                   | |         | COMPRES | chars/i |   |
|                                   | |         | SED     | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(91);CHR$(n) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image35|                         |
+-----------------------------------+-----------------------------------+
| **ESC s 0**                       | Select the **Superscript** print  |
|                                   | mode. Characters are half high    |
| **27 83 48**                      | than the normal height and are    |
|                                   | printer on the upper half         |
| **1Bh 53h 30h**                   | interline.                        |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,”NORMAL”;CHR$(27);CHR$(83 |
|                                   | );CHR$(48);”SUPERSCRIPT”          |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image36|                         |
+-----------------------------------+-----------------------------------+
| **ESC s 1**                       | Select the **Subscript** print    |
|                                   | mode. Characters are half high    |
| **27 83 49**                      | than the normal height and are    |
|                                   | printer on the lower half         |
| **1Bh 53h 31h**                   | interline.                        |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,”NORMAL”;CHR$(27);CHR$(83 |
|                                   | );CHR$(49);”SUBSCRIPT”            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image37|                         |
+-----------------------------------+-----------------------------------+
| **ESC t**                         | Disable Superscript and Subscript |
|                                   | print mode.                       |
| **27 84**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 54h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(84);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC X n**                       | If n=0, select standard quality   |
|                                   | mode (Draft)                      |
| **27 120 n**                      |                                   |
|                                   | If n=1, select near letter        |
| **1Bh 78h n**                     | quality mode (NLQ)                |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(120);CHR$(n |
|                                   | );                                |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **NLQ ON**                        | Select the Near Letter Quality    |
|                                   | print mode (NLQ)                  |
| **31**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **1Fh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(31);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image38|                         |
+-----------------------------------+-----------------------------------+
| **NLQ OFF**                       | Disable the Near Letter Quality   |
|                                   | print mode (NLQ)                  |
| **159**                           |                                   |
|                                   | 10 OPEN1,4                        |
| **9Fh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(159);             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **CRSR DWN**                      | Select PETASCII charset for       |
|                                   | uppercases/lowercases characters. |
| **17**                            | With this charset, a limited      |
|                                   | number of graphical characters    |
| **11h**                           | are available.                    |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(17);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **CRSR UP**                       | Select PETASCII charset for       |
|                                   | uppercases only characters. With  |
| **145**                           | this charset, all graphical       |
|                                   | characters are available.         |
| **91h**                           |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(145);             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

Paper feeding
~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **LF**                            | A **Line Feed** returns the print |
|                                   | head to le left margin and        |
| **10**                            | advances the paper to the next    |
|                                   | line (behavior is LF+CR).         |
| **0Ah**                           |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(10);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **CR**                            | A **Carriage Return** returns the |
|                                   | print head to le left margin and  |
| **13**                            | advances the paper to the next    |
|                                   | line (behavior is CR+LF).         |
| **0Dh**                           |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(13);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **FF**                            | A **Form Feed** prints the        |
|                                   | current page to a PNG file and    |
| **12**                            | then continues printing on the    |
|                                   | first line of a new blank page.   |
| **0Ch**                           |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(12);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **CS**                            | Returns the print head to le left |
|                                   | margin but stays in the same line |
| **141**                           | (behavior is CR).                 |
|                                   |                                   |
| **8Dh**                           | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(141);             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

Format control
~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **ESC c n**                       | Defines the page length in number |
|                                   | of text lines (range 1-127).      |
| **27 67 n**                       |                                   |
|                                   | 10 OPEN1,4,7                      |
| **1Bh 43h n**                     |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(67);CHR$(1- |
|                                   | 127);                             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **ESC c NUL n**                   | Defines the page length in inches |
|                                   | (range 1-22).                     |
| **27 67 0 n**                     |                                   |
|                                   | 10 OPEN1,4,7                      |
| **1Bh 43h 00h n**                 |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(67);CHR$(0) |
|                                   | ;CHR$(1-22);                      |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC n m**                       | Define the **Bottom of Form**     |
|                                   | (BOF) in number “m” of interlines |
| **27 78 m**                       | at the end of the page that are   |
|                                   | not used to print and are         |
| **1Bh 4Eh m**                     | automatically skipped.            |
|                                   |                                   |
|                                   | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(78);CHR$(m) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC o**                         | Disable the **Bottom of Form**    |
|                                   | (BOF).                            |
| **27 79**                         |                                   |
|                                   | This command is ignored by        |
| **1Bh 4Fh**                       | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(79);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 8**                         | Disable the end of paper detector |
|                                   | to be able to print until the end |
| **27 56**                         | of the paper.                     |
|                                   |                                   |
| **1Bh 38h**                       | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(56);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 9**                         | Enable the end of paper detector. |
|                                   |                                   |
| **27 57**                         | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
| **1Bh 39h**                       |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(57);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **HTAB**                          | This is the traditional           |
|                                   | horizontal tabulation. Head jumps |
| **9**                             | to the next tabulation stop.      |
|                                   | Stops are located every 8 PICA    |
| **09h**                           | character position since the      |
|                                   | beginning of a line. This is      |
|                                   | fixed, not configurable.          |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(9);”THIS IS THE   |
|                                   | PRINT POSITION 8”                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **POS n\ 1 n\ 2**                 | On the current line, jump to the  |
|                                   | horizontal position corresponding |
| **16 n\ 1 n\ 2**                  | to the n\ :sub:`1`\ n\ :sub:`2`   |
|                                   | decimal number of PICA characters |
| **10h n\ 1 n\ 2**                 | since the beginning of the line.  |
|                                   | Each parameter is a value between |
|                                   | 0 and 9. 00 is the position of    |
|                                   | the first character.              |
|                                   | n\ :sub:`1`\ n\ :sub:`2` can      |
|                                   | range from 00 to 79. Does nothing |
|                                   | is current position is already    |
|                                   | over the n\ :sub:`1`\ n\ :sub:`2` |
|                                   | position.                         |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(16);CHR$(2);CHR$(6); |
|                                   | ”THIS                             |
|                                   | IS THE PRINT POSITION 26”         |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC POS n\ 1 n\ 2**             | On the current line, jump to the  |
|                                   | horizontal position corresponding |
| **27 16 n\ 1 n\ 2**               | to the dot position given by      |
|                                   | parameters n\ :sub:`1` and        |
| **1Bh 10h n\ 1 n\ 2**             | n\ :sub:`2` from the beginning of |
|                                   | the line. Parameter is calculated |
|                                   | using the formula                 |
|                                   | n\ :sub:`1`\ x256+n\ :sub:`2`.    |
|                                   | Value range is 0 to 480           |
|                                   |                                   |
|                                   | Examples:                         |
|                                   |                                   |
|                                   | +---------+---------+---------+   |
|                                   | | n\ :sub | n\ :sub | POSITIO |   |
|                                   | | :`1`    | :`2`    | N       |   |
|                                   | +=========+=========+=========+   |
|                                   | | CHR$(0) | CHR$(20 | 0 + 20  |   |
|                                   | |         | )       | = 20    |   |
|                                   | +---------+---------+---------+   |
|                                   | | CHR$(1) | CHR$(0) | 256 + 0 |   |
|                                   | |         |         | = 256   |   |
|                                   | +---------+---------+---------+   |
|                                   | | CHR$(1) | CHR$(22 | 256 +   |   |
|                                   | |         | 4)      | 224 =   |   |
|                                   | |         |         | 480     |   |
|                                   | +---------+---------+---------+   |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(16);CHR$(1) |
|                                   | ;CHR$(6);”THIS                    |
|                                   | IS THE PRINT POSITION 262”        |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

Graphic Bitmap
~~~~~~~~~~~~~~

Printer can print graphic data using the Bit Image Mode (BIM). An image
is defined by a bit array of 7 rows. Each column is encoded in a byte,
LSB is up, MSB is not printed and always set to 1. Horizontal definition
is 60 dpi. Vertical definition is 72 dpi.

Example for a 16 columns array:

+-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|       | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  |
+=======+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+=====+
| 1     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
+-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| 2     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
+-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| 4     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
+-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| 8     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
+-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| 16    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
+-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| 32    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
+-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| 64    |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
+-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| Total | 136 | 148 | 162 | 193 | 162 | 148 | 136 | 136 | 156 | 190 | 255 | 190 | 156 | 136 | 235 | 136 |
+-------+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+

Don’t forget that bit 2\ :sup:`7` is always set, this adds 128 to each
value.

First byte with 2\ :sup:`7` bit does not set mean that BIM data has
ended. Printer is still on BIM mode as long as a printable character has
not been sent. Commands with bit 2\ :sup:`7` not set are executed (CR,
LF, …). As BIM is always printed using the double width mode, you can
use code **EN OFF** (15 0Fh) to tell the printer that BIM data has
ended.

When in BIM, interline is automatically set to 7 dot height.

+-----------------------------------+-----------------------------------+
| **BIT IMG**                       | Select the **Bit Image Mode**.    |
|                                   | Provided data is printed as an    |
| **8**                             | array of dots as described above. |
|                                   | Maximum BIM data width that can   |
| **08h**                           | be printed on printable area is   |
|                                   | 480 dots.                         |
|                                   |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20 A$=””                          |
|                                   |                                   |
|                                   | 30 FOR I=1 TO 16                  |
|                                   |                                   |
|                                   | 40 READ A:A$=A$+CHR$(A)           |
|                                   |                                   |
|                                   | 50 NEXT I                         |
|                                   |                                   |
|                                   | 60 FOR J=1 TO 3                   |
|                                   |                                   |
|                                   | 70 PRINT#1,CHR$(8);A$             |
|                                   |                                   |
|                                   | 80 NEXT J                         |
|                                   |                                   |
|                                   | 90 CLOSE1                         |
|                                   |                                   |
|                                   | 100 END                           |
|                                   |                                   |
|                                   | 110 DATA                          |
|                                   | 136,148,162,193,162,148,136,136   |
|                                   |                                   |
|                                   | 120 DATA                          |
|                                   | 156,186,255,186,156,136,235,136   |
|                                   |                                   |
|                                   | |image41|                         |
+===================================+===================================+
| **BIT IMG SUB n**                 | Repeat n times the next byte      |
|                                   | while in Bit Image Mode. If you   |
| **8 26 n**                        | need to send many times the same  |
|                                   | byte you can use this command to  |
| **08h 1Ah n**                     | tell how many times to repeat the |
|                                   | same byte while in BIM data. If   |
|                                   | n=0 data will be repeated 256     |
|                                   | times. If you need more than 256  |
|                                   | repetitions, you will have to     |
|                                   | call SUB with the same data       |
|                                   | several times. Printer is still   |
|                                   | in BIM mode and a second SUB can  |
|                                   | be sent.                          |
|                                   |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20 A$=””                          |
|                                   |                                   |
|                                   | 30 FOR I=1 TO 16                  |
|                                   |                                   |
|                                   | 40 READ A:A$=A$+CHR$(A)           |
|                                   |                                   |
|                                   | 50 NEXT I                         |
|                                   |                                   |
|                                   | 60 FOR J=1 TO 3                   |
|                                   |                                   |
|                                   | 70                                |
|                                   | PRINT#1,CHR$(8);CHR$(26);CHR$(100 |
|                                   | );A$                              |
|                                   |                                   |
|                                   | 80 NEXT J                         |
|                                   |                                   |
|                                   | 90 CLOSE1                         |
|                                   |                                   |
|                                   | 100 END                           |
|                                   |                                   |
|                                   | 110 DATA                          |
|                                   | 136,148,162,193,162,148,136,136   |
|                                   |                                   |
|                                   | 120 DATA                          |
|                                   | 156,186,255,186,156,136,235,136   |
|                                   |                                   |
|                                   | |image42|                         |
+-----------------------------------+-----------------------------------+

Character creation, Down Line Loading (DLL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On a MPS-1230 user can create from 1 to 94 custom characters to replace
normal characters. These characters are loaded in RAM. Consecutive
characters can be defined in a single sequence beginning by the first
character. DLL has to be enabled in the configuration of a real MPS-1230
printer and RAM buffer is smaller as a part of the RAM is reserved for
DLL.

On Ultimate-II Virtual Printer, DLL is not available but commands are
correctly recognized and skipped with all their data.

+-----------------------------------+-----------------------------------+
| **ESC =**                         | This code has to be followed by   |
|                                   | parameters **m n c s a p\ 1       |
| **27 61**                         | p\ 2**\ …\ **p\ 11** which        |
|                                   | represents decimal byte codes to  |
| **1Bh 3Dh**                       | describe characters to load.      |
|                                   |                                   |
|                                   | | **m** and **n** are the number  |
|                                   |   of bytes to load. Use the       |
|                                   |   formula                         |
|                                   | | t = (number of chars x 13) +2   |
|                                   | | then calculate m and n in order |
|                                   |   to have m + (n x 256) = t using |
|                                   |   formulas                        |
|                                   | | n = t / 256 (keep entire part   |
|                                   |   only)                           |
|                                   | | m = t – (n x 256)               |
|                                   | | E.g.: for 94 characters,        |
|                                   | | t = (94 x 13) +2 = 1224         |
|                                   | | n = 1224 / 256 = 4              |
|                                   | | m = 1224 – (4 x 256) = 200      |
|                                   |                                   |
|                                   | **c** Is the decimal ASCII code   |
|                                   | of the first character of the     |
|                                   | sequence. Only decimal codes from |
|                                   | 33 to 126 can be used for DDL.    |
|                                   | Code 65 is “A”                    |
|                                   |                                   |
|                                   | **s** Is a constant value 20      |
|                                   | (14h) (missing from official      |
|                                   | documentation but present in all  |
|                                   | examples)                         |
|                                   |                                   |
|                                   | | **a** This parameter tells      |
|                                   |   which needles have to be used   |
|                                   |   to print that character. Head   |
|                                   |   has 9 needles of which 8 can be |
|                                   |   used here.                      |
|                                   | | a = 0 : use the 8 upper needles |
|                                   | | a = 1 : use the 8 lower needles |
|                                   |                                   |
|                                   | **p\ 1 p\ 2\ …p\ 11** Represents  |
|                                   | the 11 columns defining the dots  |
|                                   | printed for the character.        |
|                                   |                                   |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   | |       | 1   | 2 | 3 | 4 | 5 | 6 |
|                                   |  | 7  | 8  | 9  | 10 | 11 |       |
|                                   | +=======+=====+===+===+===+===+== |
|                                   | =+====+====+====+====+====+       |
|                                   | | 1     |     |   |   |   |   |   |
|                                   |  |    |    |    |    |    |       |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   | | 2     |     |   |   |   |   |   |
|                                   |  |    |    |    |    |    |       |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   | | 4     |     |   |   |   |   |   |
|                                   |  |    |    |    |    |    |       |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   | | 8     |     |   |   |   |   |   |
|                                   |  |    |    |    |    |    |       |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   | | 16    |     |   |   |   |   |   |
|                                   |  |    |    |    |    |    |       |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   | | 32    |     |   |   |   |   |   |
|                                   |  |    |    |    |    |    |       |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   | | 64    |     |   |   |   |   |   |
|                                   |  |    |    |    |    |    |       |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   | | 128   |     |   |   |   |   |   |
|                                   |  |    |    |    |    |    |       |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   | | Total | 136 | 0 | 9 | 0 | 9 | 0 |
|                                   |  | 25 | 32 | 70 | 0  | 0  |       |
|                                   | +-------+-----+---+---+---+---+-- |
|                                   | -+----+----+----+----+----+       |
|                                   |                                   |
|                                   | This represents the real R        |
|                                   | character in DRAFT quality.       |
|                                   |                                   |
|                                   | In the 8x11 matrix you have to    |
|                                   | remind that a dot active in a     |
|                                   | column cannot be active in the    |
|                                   | next column to let the head       |
|                                   | recycle. Ultimate-II Virtual      |
|                                   | Printer does not suffer from this |
|                                   | limitation.                       |
|                                   |                                   |
|                                   | *Note from the author: I tested   |
|                                   | this command on a real MPS-1230   |
|                                   | because explanations given by     |
|                                   | Commodore seems to be false. I    |
|                                   | can’t make it work, example in    |
|                                   | the MPS-1230 manual prints        |
|                                   | nothing. Where are the 13 bytes   |
|                                   | by character? I only count 12     |
|                                   | (*\ **a p\ 1                      |
|                                   | p\ 2**\ *\ …\ *\ **p\ 11**\ *)*   |
+===================================+===================================+
| **ESC i n**                       | Select the print quality          |
|                                   | depending on parameter “n”        |
| **27 73 n**                       |                                   |
|                                   | n=0 standard quality (draft) and  |
| **1Bh 49h n**                     | normal characters                 |
|                                   |                                   |
|                                   | n=2 near letter quality (NLQ) and |
|                                   | normal characters                 |
|                                   |                                   |
|                                   | n=4 standard quality (draft) and  |
|                                   | special characters created with   |
|                                   | Down Line Loading (DLL). Not      |
|                                   | supported on Ultimate-II Virtual  |
|                                   | Printer, same behavior as n=0.    |
|                                   |                                   |
|                                   | n=6 near letter quality (NLQ) and |
|                                   | special characters created with   |
|                                   | Down Line Loading (DLL). Not      |
|                                   | supported on Ultimate-II Virtual  |
|                                   | Printer, same behavior as n=2.    |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(73);CHR$(n) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image44|                         |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
+-----------------------------------+-----------------------------------+

EPSON FX-80 commands
====================

This chapter describes the commands the printer can understand when
using the Epson FX-80. This was one of the most popular printers in the
80’s for its powerful graphic instruction set. With this emulation you
can reach the maximum graphical resolution the printer can print
(240x216dpi). This is still much lower than modern printers. This
printer uses ASCII7.

.. _secondary-address-1:

Secondary address
-----------------

Secondary address on OPEN command is not used by Epson FX-80 emulation.

.. _commands-1:

Commands
--------

.. _graphical-operations-1:

Graphical operations
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **ESC G**                         | Select the **Double Strike**      |
|                                   | print mode. Characters are        |
| **27 71**                         | printed twice and paper is lifted |
|                                   | 1/216” between the two passes.    |
| **1Bh 47h**                       |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);chr$(71);”DOUBLE |
|                                   | STRIKE”                           |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image53|                         |
+===================================+===================================+
| **ESC H**                         | Disable **Double Strike** print   |
|                                   | mode                              |
| **27 72**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 48h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);chr$(72);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **SO**                            | Select the **Double Width** print |
|                                   | mode                              |
| **14**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **0Eh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(14);”DOUBLE       |
|                                   | WIDTH”                            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image54|                         |
+-----------------------------------+-----------------------------------+
| **DC4**                           | Disable the **Double Width**      |
|                                   | print mode                        |
| **20**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **14h**                           |                                   |
|                                   | 20 PRINT#1,CHR$(20);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC SO**                        | Same as **SO** (Double Width      |
|                                   | print mode ON).                   |
| **27 14**                         |                                   |
|                                   |                                   |
| **1Bh 0Eh**                       |                                   |
+-----------------------------------+-----------------------------------+
| **ESC W 1**                       | Same as **SO** (Double Width ON). |
|                                   | 1 can be sent with ASCII code of  |
| **27 87 1**                       | ‘1’ (49 - 31h)                    |
|                                   |                                   |
| **1Bh 57h 01h**                   |                                   |
+-----------------------------------+-----------------------------------+
| **ESC W 0**                       | Same as **DC4** (Double Width     |
|                                   | OFF). 0 can be sent with ASCII    |
| **27 87 0**                       | code of ‘0’ (48 - 30h)            |
|                                   |                                   |
| **1Bh 57h 00h**                   |                                   |
+-----------------------------------+-----------------------------------+
| **ESC – 1**                       | Select the **Underline** print    |
|                                   | mode for all characters and       |
| **27 45 49**                      | spaces that follow.               |
|                                   |                                   |
| **1Bh 2Dh 31h**                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(45);CHR$(49 |
|                                   | );”UNDERLINE”                     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image55|                         |
+-----------------------------------+-----------------------------------+
| **ESC - 0**                       | Disable the Underline print mode. |
|                                   |                                   |
| **27 45 48**                      | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 2Dh 30h**                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(45);CHR$(48 |
|                                   | );                                |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC E**                         | Select the **Bold** print mode.   |
|                                   |                                   |
| **27 69**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 45h**                       | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(69);”BOLD”  |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image56|                         |
+-----------------------------------+-----------------------------------+
| **ESC F**                         | Disable the Bold print mode.      |
|                                   |                                   |
| **27 70**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 46h**                       | 20 PRINT#1,CHR$(27);CHR$(70);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 4**                         | Select the **Italic** print mode. |
|                                   |                                   |
| **27 52**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 34h**                       | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(52);”ITALIC |
|                                   | ”                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image57|                         |
+-----------------------------------+-----------------------------------+
| **ESC 5**                         | Disable the **Italic** print      |
|                                   | mode.                             |
| **27 53**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 35h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(53);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **SI**                            | Select the **CONDENSED** spacing  |
|                                   | mode (17.1 chars/inch)            |
| **15**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **0Fh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(15);”CONDENSED”   |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC SI**                        | Same as **SI** (Condensed 17.1    |
|                                   | chars/inch)                       |
| **27 15**                         |                                   |
|                                   |                                   |
| **1Bh 0Fh**                       |                                   |
+-----------------------------------+-----------------------------------+
| **ESC M**                         | Select the **ELITE** spacing mode |
|                                   | (12 chars/inch).                  |
| **27 77**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 4Dh**                       |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(77);”PICA”  |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **DC2**                           | Select the **PICA** spacing mode  |
|                                   | (10 chars/inch). This is the      |
| **18**                            | default spacing.                  |
|                                   |                                   |
| **12h**                           | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(18);”PICA”        |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC P**                         | Same as **DC2** (PICA 10          |
|                                   | chars/inch)                       |
| **27 80**                         |                                   |
|                                   |                                   |
| **1Bh 50h**                       |                                   |
+-----------------------------------+-----------------------------------+
| **ESC S 0**                       | Select the **Superscript** print  |
|                                   | mode. Characters are half high    |
| **27 83 48**                      | than the normal height and are    |
|                                   | printer on the upper half         |
| **1Bh 53h 30h**                   | interline.                        |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,”NORMAL”;CHR$(27);CHR$(83 |
|                                   | );CHR$(48);”SUPERSCRIPT”          |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image58|                         |
+-----------------------------------+-----------------------------------+
| **ESC S 1**                       | Select the **Subscript** print    |
|                                   | mode. Characters are half high    |
| **27 83 49**                      | than the normal height and are    |
|                                   | printer on the lower half         |
| **1Bh 53h 31h**                   | interline.                        |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,”NORMAL”;CHR$(27);CHR$(83 |
|                                   | );CHR$(49);”SUBSCRIPT”            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image59|                         |
+-----------------------------------+-----------------------------------+
| **ESC T**                         | Disable Superscript and Subscript |
|                                   | print mode.                       |
| **27 84**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 54h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(84);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC x n**                       | If n=0, select standard quality   |
|                                   | mode (Draft)                      |
| **27 120 n**                      |                                   |
|                                   | If n=1, select near letter        |
| **1Bh 78h n**                     | quality mode (NLQ)                |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(120);CHR$(n |
|                                   | );                                |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image60|                         |
+-----------------------------------+-----------------------------------+
| **ESC p n**                       | **Proportional** spacing ON/OFF   |
|                                   |                                   |
| **27 112 n**                      | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
| **1Bh 70h n**                     |                                   |
+-----------------------------------+-----------------------------------+
| **ESC ! n**                       | Select graphical layout for text. |
|                                   | This is a composite of multiple   |
| **27 33 n**                       | attributes set by only one        |
|                                   | command. Value n is taken from    |
| **1Bh 21h n**                     | this table :                      |
|                                   |                                   |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | n  | U | I | W | S | B | C | E  |
|                                   | |  | n   | U | I | W | S | B | C  |
|                                   | | E |  | n   | U | I | W | S | B  |
|                                   | | C | E |                         |
|                                   | +====+===+===+===+===+===+===+=== |
|                                   | +==+=====+===+===+===+===+===+=== |
|                                   | +===+==+=====+===+===+===+===+=== |
|                                   | +===+===+                         |
|                                   | | 0  |   |   |   |   |   |   |    |
|                                   | |  | 86  |   | • |   | • |   | •  |
|                                   | |   |  | 172 | • |   | • |   | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 1  |   |   |   |   |   |   | •  |
|                                   | |  | 87  |   | • |   | • |   |    |
|                                   | | • |  | 173 | • |   | • |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 2  |   |   |   |   |   |   |    |
|                                   | |  | 88  |   | • |   | • | • |    |
|                                   | |   |  | 174 | • |   | • |   | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 3  |   |   |   |   |   |   | •  |
|                                   | |  | 89  |   | • |   | • | • |    |
|                                   | | • |  | 175 | • |   | • |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 4  |   |   |   |   |   | • |    |
|                                   | |  | 90  |   | • |   | • | • |    |
|                                   | |   |  | 176 | • |   | • | • |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 5  |   |   |   |   |   |   | •  |
|                                   | |  | 91  |   | • |   | • | • |    |
|                                   | | • |  | 177 | • |   | • | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 6  |   |   |   |   |   | • |    |
|                                   | |  | 92  |   | • |   | • | • | •  |
|                                   | |   |  | 178 | • |   | • | • |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 7  |   |   |   |   |   |   | •  |
|                                   | |  | 93  |   | • |   | • | • |    |
|                                   | | • |  | 179 | • |   | • | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 8  |   |   |   |   | • |   |    |
|                                   | |  | 94  |   | • |   | • | • | •  |
|                                   | |   |  | 180 | • |   | • | • |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 9  |   |   |   |   | • |   | •  |
|                                   | |  | 95  |   | • |   | • | • |    |
|                                   | | • |  | 181 | • |   | • | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 10 |   |   |   |   | • |   |    |
|                                   | |  | 96  |   | • | • |   |   |    |
|                                   | |   |  | 182 | • |   | • | • |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 11 |   |   |   |   | • |   | •  |
|                                   | |  | 97  |   | • | • |   |   |    |
|                                   | | • |  | 183 | • |   | • | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 12 |   |   |   |   | • | • |    |
|                                   | |  | 98  |   | • | • |   |   |    |
|                                   | |   |  | 184 | • |   | • | • | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 13 |   |   |   |   | • |   | •  |
|                                   | |  | 99  |   | • | • |   |   |    |
|                                   | | • |  | 185 | • |   | • | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 14 |   |   |   |   | • | • |    |
|                                   | |  | 100 |   | • | • |   |   | •  |
|                                   | |   |  | 186 | • |   | • | • | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 15 |   |   |   |   | • |   | •  |
|                                   | |  | 101 |   | • | • |   |   |    |
|                                   | | • |  | 187 | • |   | • | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 16 |   |   |   | • |   |   |    |
|                                   | |  | 102 |   | • | • |   |   | •  |
|                                   | |   |  | 188 | • |   | • | • | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 17 |   |   |   | • |   |   | •  |
|                                   | |  | 103 |   | • | • |   |   |    |
|                                   | | • |  | 189 | • |   | • | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 18 |   |   |   | • |   |   |    |
|                                   | |  | 104 |   | • | • |   | • |    |
|                                   | |   |  | 190 | • |   | • | • | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 19 |   |   |   | • |   |   | •  |
|                                   | |  | 105 |   | • | • |   | • |    |
|                                   | | • |  | 191 | • |   | • | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 20 |   |   |   | • |   | • |    |
|                                   | |  | 106 |   | • | • |   | • |    |
|                                   | |   |  | 192 | • | • |   |   |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 21 |   |   |   | • |   |   | •  |
|                                   | |  | 107 |   | • | • |   | • |    |
|                                   | | • |  | 193 | • | • |   |   |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 22 |   |   |   | • |   | • |    |
|                                   | |  | 108 |   | • | • |   | • | •  |
|                                   | |   |  | 194 | • | • |   |   |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 23 |   |   |   | • |   |   | •  |
|                                   | |  | 109 |   | • | • |   | • |    |
|                                   | | • |  | 195 | • | • |   |   |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 24 |   |   |   | • | • |   |    |
|                                   | |  | 110 |   | • | • |   | • | •  |
|                                   | |   |  | 196 | • | • |   |   |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 25 |   |   |   | • | • |   | •  |
|                                   | |  | 111 |   | • | • |   | • |    |
|                                   | | • |  | 197 | • | • |   |   |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 26 |   |   |   | • | • |   |    |
|                                   | |  | 112 |   | • | • | • |   |    |
|                                   | |   |  | 198 | • | • |   |   |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 27 |   |   |   | • | • |   | •  |
|                                   | |  | 113 |   | • | • | • |   |    |
|                                   | | • |  | 199 | • | • |   |   |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 28 |   |   |   | • | • | • |    |
|                                   | |  | 114 |   | • | • | • |   |    |
|                                   | |   |  | 200 | • | • |   |   | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 29 |   |   |   | • | • |   | •  |
|                                   | |  | 115 |   | • | • | • |   |    |
|                                   | | • |  | 201 | • | • |   |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 30 |   |   |   | • | • | • |    |
|                                   | |  | 116 |   | • | • | • |   | •  |
|                                   | |   |  | 202 | • | • |   |   | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 31 |   |   |   | • | • |   | •  |
|                                   | |  | 117 |   | • | • | • |   |    |
|                                   | | • |  | 203 | • | • |   |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 32 |   |   | • |   |   |   |    |
|                                   | |  | 118 |   | • | • | • |   | •  |
|                                   | |   |  | 204 | • | • |   |   | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 33 |   |   | • |   |   |   | •  |
|                                   | |  | 119 |   | • | • | • |   |    |
|                                   | | • |  | 205 | • | • |   |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 34 |   |   | • |   |   |   |    |
|                                   | |  | 120 |   | • | • | • | • |    |
|                                   | |   |  | 206 | • | • |   |   | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 35 |   |   | • |   |   |   | •  |
|                                   | |  | 121 |   | • | • | • | • |    |
|                                   | | • |  | 207 | • | • |   |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 36 |   |   | • |   |   | • |    |
|                                   | |  | 122 |   | • | • | • | • |    |
|                                   | |   |  | 208 | • | • |   | • |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 37 |   |   | • |   |   |   | •  |
|                                   | |  | 123 |   | • | • | • | • |    |
|                                   | | • |  | 209 | • | • |   | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 38 |   |   | • |   |   | • |    |
|                                   | |  | 124 |   | • | • | • | • | •  |
|                                   | |   |  | 210 | • | • |   | • |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 39 |   |   | • |   |   |   | •  |
|                                   | |  | 125 |   | • | • | • | • |    |
|                                   | | • |  | 211 | • | • |   | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 40 |   |   | • |   | • |   |    |
|                                   | |  | 126 |   | • | • | • | • | •  |
|                                   | |   |  | 212 | • | • |   | • |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 41 |   |   | • |   | • |   | •  |
|                                   | |  | 127 |   | • | • | • | • |    |
|                                   | | • |  | 213 | • | • |   | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 42 |   |   | • |   | • |   |    |
|                                   | |  | 128 | • |   |   |   |   |    |
|                                   | |   |  | 214 | • | • |   | • |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 43 |   |   | • |   | • |   | •  |
|                                   | |  | 129 | • |   |   |   |   |    |
|                                   | | • |  | 215 | • | • |   | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 44 |   |   | • |   | • | • |    |
|                                   | |  | 130 | • |   |   |   |   |    |
|                                   | |   |  | 216 | • | • |   | • | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 45 |   |   | • |   | • |   | •  |
|                                   | |  | 131 | • |   |   |   |   |    |
|                                   | | • |  | 217 | • | • |   | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 46 |   |   | • |   | • | • |    |
|                                   | |  | 132 | • |   |   |   |   | •  |
|                                   | |   |  | 218 | • | • |   | • | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 47 |   |   | • |   | • |   | •  |
|                                   | |  | 133 | • |   |   |   |   |    |
|                                   | | • |  | 219 | • | • |   | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 48 |   |   | • | • |   |   |    |
|                                   | |  | 134 | • |   |   |   |   | •  |
|                                   | |   |  | 220 | • | • |   | • | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 49 |   |   | • | • |   |   | •  |
|                                   | |  | 135 | • |   |   |   |   |    |
|                                   | | • |  | 221 | • | • |   | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 50 |   |   | • | • |   |   |    |
|                                   | |  | 136 | • |   |   |   | • |    |
|                                   | |   |  | 222 | • | • |   | • | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 51 |   |   | • | • |   |   | •  |
|                                   | |  | 137 | • |   |   |   | • |    |
|                                   | | • |  | 223 | • | • |   | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 52 |   |   | • | • |   | • |    |
|                                   | |  | 138 | • |   |   |   | • |    |
|                                   | |   |  | 224 | • | • | • |   |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 53 |   |   | • | • |   |   | •  |
|                                   | |  | 139 | • |   |   |   | • |    |
|                                   | | • |  | 225 | • | • | • |   |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 54 |   |   | • | • |   | • |    |
|                                   | |  | 140 | • |   |   |   | • | •  |
|                                   | |   |  | 226 | • | • | • |   |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 55 |   |   | • | • |   |   | •  |
|                                   | |  | 141 | • |   |   |   | • |    |
|                                   | | • |  | 227 | • | • | • |   |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 56 |   |   | • | • | • |   |    |
|                                   | |  | 142 | • |   |   |   | • | •  |
|                                   | |   |  | 228 | • | • | • |   |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 57 |   |   | • | • | • |   | •  |
|                                   | |  | 143 | • |   |   |   | • |    |
|                                   | | • |  | 229 | • | • | • |   |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 58 |   |   | • | • | • |   |    |
|                                   | |  | 144 | • |   |   | • |   |    |
|                                   | |   |  | 230 | • | • | • |   |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 59 |   |   | • | • | • |   | •  |
|                                   | |  | 145 | • |   |   | • |   |    |
|                                   | | • |  | 231 | • | • | • |   |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 60 |   |   | • | • | • | • |    |
|                                   | |  | 146 | • |   |   | • |   |    |
|                                   | |   |  | 232 | • | • | • |   | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 61 |   |   | • | • | • |   | •  |
|                                   | |  | 147 | • |   |   | • |   |    |
|                                   | | • |  | 233 | • | • | • |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 62 |   |   | • | • | • | • |    |
|                                   | |  | 148 | • |   |   | • |   | •  |
|                                   | |   |  | 234 | • | • | • |   | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 63 |   |   | • | • | • |   | •  |
|                                   | |  | 149 | • |   |   | • |   |    |
|                                   | | • |  | 235 | • | • | • |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 64 |   | • |   |   |   |   |    |
|                                   | |  | 150 | • |   |   | • |   | •  |
|                                   | |   |  | 236 | • | • | • |   | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 65 |   | • |   |   |   |   | •  |
|                                   | |  | 151 | • |   |   | • |   |    |
|                                   | | • |  | 237 | • | • | • |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 66 |   | • |   |   |   |   |    |
|                                   | |  | 152 | • |   |   | • | • |    |
|                                   | |   |  | 238 | • | • | • |   | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 67 |   | • |   |   |   |   | •  |
|                                   | |  | 153 | • |   |   | • | • |    |
|                                   | | • |  | 239 | • | • | • |   | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 68 |   | • |   |   |   | • |    |
|                                   | |  | 154 | • |   |   | • | • |    |
|                                   | |   |  | 240 | • | • | • | • |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 69 |   | • |   |   |   |   | •  |
|                                   | |  | 155 | • |   |   | • | • |    |
|                                   | | • |  | 241 | • | • | • | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 70 |   | • |   |   |   | • |    |
|                                   | |  | 156 | • |   |   | • | • | •  |
|                                   | |   |  | 242 | • | • | • | • |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 71 |   | • |   |   |   |   | •  |
|                                   | |  | 157 | • |   |   | • | • |    |
|                                   | | • |  | 243 | • | • | • | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 72 |   | • |   |   | • |   |    |
|                                   | |  | 158 | • |   |   | • | • | •  |
|                                   | |   |  | 244 | • | • | • | • |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 73 |   | • |   |   | • |   | •  |
|                                   | |  | 159 | • |   |   | • | • |    |
|                                   | | • |  | 245 | • | • | • | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 74 |   | • |   |   | • |   |    |
|                                   | |  | 160 | • |   | • |   |   |    |
|                                   | |   |  | 246 | • | • | • | • |    |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 75 |   | • |   |   | • |   | •  |
|                                   | |  | 161 | • |   | • |   |   |    |
|                                   | | • |  | 247 | • | • | • | • |    |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 76 |   | • |   |   | • | • |    |
|                                   | |  | 162 | • |   | • |   |   |    |
|                                   | |   |  | 248 | • | • | • | • | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 77 |   | • |   |   | • |   | •  |
|                                   | |  | 163 | • |   | • |   |   |    |
|                                   | | • |  | 249 | • | • | • | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 78 |   | • |   |   | • | • |    |
|                                   | |  | 164 | • |   | • |   |   | •  |
|                                   | |   |  | 250 | • | • | • | • | •  |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 79 |   | • |   |   | • |   | •  |
|                                   | |  | 165 | • |   | • |   |   |    |
|                                   | | • |  | 251 | • | • | • | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 80 |   | • |   | • |   |   |    |
|                                   | |  | 166 | • |   | • |   |   | •  |
|                                   | |   |  | 252 | • | • | • | • | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 81 |   | • |   | • |   |   | •  |
|                                   | |  | 167 | • |   | • |   |   |    |
|                                   | | • |  | 253 | • | • | • | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 82 |   | • |   | • |   |   |    |
|                                   | |  | 168 | • |   | • |   | • |    |
|                                   | |   |  | 254 | • | • | • | • | •  |
|                                   | | • |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 83 |   | • |   | • |   |   | •  |
|                                   | |  | 169 | • |   | • |   | • |    |
|                                   | | • |  | 255 | • | • | • | • | •  |
|                                   | |   | • |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 84 |   | • |   | • |   | • |    |
|                                   | |  | 170 | • |   | • |   | • |    |
|                                   | |   |  |     |   |   |   |   |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   | | 85 |   | • |   | • |   |   | •  |
|                                   | |  | 171 | • |   | • |   | • |    |
|                                   | | • |  |     |   |   |   |   |    |
|                                   | |   |   |                         |
|                                   | +----+---+---+---+---+---+---+--- |
|                                   | +--+-----+---+---+---+---+---+--- |
|                                   | +---+--+-----+---+---+---+---+--- |
|                                   | +---+---+                         |
|                                   |                                   |
|                                   | U: Underline, I:Italic, W:Double  |
|                                   | width, S:Double strike, B:Bold,   |
|                                   | C:Condensed, E:Elite              |
+-----------------------------------+-----------------------------------+

.. _paper-feeding-1:

Paper feeding
~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **LF**                            | A **Line Feed** returns the print |
|                                   | head to le left margin and        |
| **10**                            | advances the paper to the next    |
|                                   | line (behavior is LF+CR).         |
| **0Ah**                           |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(10);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **CR**                            | A **Carriage Return** returns the |
|                                   | print head to le left margin but  |
| **13**                            | stays on the same line (behavior  |
|                                   | is CR only, no LF).               |
| **0Dh**                           |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(13);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **FF**                            | A **Form Feed** prints the        |
|                                   | current page to a PNG file and    |
| **12**                            | then continues printing on the    |
|                                   | first line of a new blank page.   |
| **0Ch**                           |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(12);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 0**                         | Select vertical spacing **1/8”**  |
|                                   | between each printed line.        |
| **27 48**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 30h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(48);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 1**                         | Select vertical spacing **7/72”** |
|                                   | between each printed line.        |
| **27 49**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 31h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(49);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 2**                         | Select vertical spacing **1/6”**  |
|                                   | between each printed line.        |
| **27 50**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 32h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(50);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 3 n**                       | Select vertical spacing           |
|                                   | **n/216”** between each printed   |
| **27 51 n**                       | line.                             |
|                                   |                                   |
| **1Bh 32h n**                     | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(51);CHR$(37 |
|                                   | )”37/216                          |
|                                   | inch”                             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC A n**                       | Select vertical spacing **n/72”** |
|                                   | between each printed line.        |
| **27 65 n**                       |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 41h n**                     |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(65);CHR$(8) |
|                                   | ”8/72                             |
|                                   | inch for one pass BIM”            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC J n**                       | Skip down **n/216”** of paper.    |
|                                   |                                   |
| **27 74 n**                       | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 4Ah n**                     | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(74);CHR$(70 |
|                                   | )”70/216                          |
|                                   | inch skipped”                     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC j n**                       | Reverse paper feed **n/216”** up. |
|                                   |                                   |
| **27 106 n**                      | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 6Ah n**                     | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(106);CHR$(7 |
|                                   | 0)”70/216                         |
|                                   | inch up”                          |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

.. _format-control-1:

Format control
~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **BS**                            | **Backspace**, go back one        |
|                                   | character. Left character is not  |
| **8**                             | erased and next character will be |
|                                   | printed over it. You can combine  |
| **08h**                           | characters this way.              |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,”a”;CHR$(8)”^ to print |
|                                   | a with a circumflex”;             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **ESC C n**                       | Defines the page length in number |
|                                   | of lines (range 1-127). Current   |
| **27 67 n**                       | line spacing is used to calculate |
|                                   | form length.                      |
| **1Bh 43h n**                     |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(67);CHR$(1- |
|                                   | 127);                             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC C NUL n**                   | Defines the page length in inches |
|                                   | (range 1-22).                     |
| **27 67 0 n**                     |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 43h 00h n**                 |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(67);CHR$(0) |
|                                   | ;CHR$(1-22);                      |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC l n**                       | Defines the left margin in number |
|                                   | of characters. Current char pitch |
| **27 108 n**                      | is used to calculate margin       |
|                                   | position in the line.             |
| **1Bh 6Ch n**                     |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(108);CHR$(1 |
|                                   | 0)                                |
|                                   |                                   |
|                                   | 30 PRINT#1,”MARGIN LEFT AT 10”    |
|                                   |                                   |
|                                   | 40 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC Q n**                       | Defines the right margin in       |
|                                   | number of characters. Current     |
| **27 81 n**                       | char pitch is used to calculate   |
|                                   | margin position in the line.      |
| **1Bh 51h n**                     |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(81);CHR$(70 |
|                                   | )                                 |
|                                   |                                   |
|                                   | 30 PRINT#1,”RIGHT MARGIN AT 70”   |
|                                   |                                   |
|                                   | 40 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC N m**                       | Define the **Bottom of Form**     |
|                                   | (BOF) in number “m” of lines at   |
| **27 78 m**                       | the end of the page that are      |
|                                   | skipped to jump over perforations |
| **1Bh 4Eh m**                     | when using continuous paper.      |
|                                   |                                   |
|                                   | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(78);CHR$(m) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC O**                         | Disable the **Bottom of Form**    |
|                                   | (BOF).                            |
| **27 79**                         |                                   |
|                                   | This command is ignored by        |
| **1Bh 4Fh**                       | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(79);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 8**                         | Disable the end of paper detector |
|                                   | to be able to print until the end |
| **27 56**                         | of the paper.                     |
|                                   |                                   |
| **1Bh 38h**                       | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(56);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 9**                         | Enable the end of paper detector. |
|                                   |                                   |
| **27 57**                         | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
| **1Bh 39h**                       |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(57);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **TAB**                           | This is the traditional           |
|                                   | **horizontal tabulation**. Head   |
| **9**                             | jumps to the next tabulation      |
|                                   | stop. Default stops are located   |
| **09h**                           | every 8 PICA character position   |
|                                   | since the beginning of a line.    |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(9);”THIS IS THE   |
|                                   | PRINT POSITION 8”                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **VT**                            | Jump to next **vertical           |
|                                   | tabulation** stop. There is no    |
| **11**                            | Carriage Return. No default stops |
|                                   | are defined. If no vertical stops |
| **0Bh**                           | are defined, it will jump one     |
|                                   | line, same as LF.                 |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(11);”JUMPED TO    |
|                                   | NEXT VERTICAL TAB STOP”           |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC B n\ 1 … 0**                | Define the **vertical tabulation  |
|                                   | stop program**. Each value **n**  |
| **27 66 n\ 1 … 0**                | represents a line number where to |
|                                   | set a vertical tab stop in        |
| **1Bh 42h n\ 1 … 0**              | ascending order. Last one is 0 to |
|                                   | tell that the sequence has ended. |
|                                   | Up to 32 stops can be created.    |
|                                   | Current line spacing is used to   |
|                                   | calculate tab position in the     |
|                                   | page.                             |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(66);CHR$(5) |
|                                   | ;CHR$(10);CHR$(15);CHR$(0)        |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC D n\ 1 … 0**                | Define the **horizontal           |
|                                   | tabulation stop program**. Each   |
| **27 68 n\ 1 … 0**                | value **n** represents a          |
|                                   | character position where to set a |
| **1Bh 44h n\ 1 … 0**              | tab stop in ascending order. Last |
|                                   | one is 0 to tell that the         |
|                                   | sequence has ended. Up to 32      |
|                                   | stops can be created. Current     |
|                                   | char pitch is used to calculate   |
|                                   | tab position in the line.         |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(68);CHR$(10 |
|                                   | );CHR$(20);CHR$(30);CHR$(0)       |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC b m n\ 1 … 0**              | Define a **vertical tabulation    |
|                                   | stop program**. You can define up |
| **27 98 m n\ 1 … 0**              | to 8 programs (**m**\ =0-7). Each |
|                                   | value **n** represents a line     |
| **1Bh 62h m n\ 1 … 0**            | number where to set a vertical    |
|                                   | tab stop in ascending order. Last |
|                                   | one is 0 to tell that the         |
|                                   | sequence has ended. Up to 32      |
|                                   | stops can be created per program. |
|                                   | Current line spacing is used to   |
|                                   | calculate tab position in the     |
|                                   | page. Use **ESC /** to activate   |
|                                   | the program. Previous command     |
|                                   | **ESC B** modifies only the       |
|                                   | current program. Default current  |
|                                   | program is 0.                     |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(98);CHR$(7) |
|                                   | ;CHR$(5);CHR$(25);CHR$(0)         |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC / n**                       | Activate one of the 8 possible    |
|                                   | vertical tabulation stop          |
| **27 47 n**                       | programs. Value **n** is program  |
|                                   | number from 0 to 7.               |
| **1Bh 2Fh n**                     |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(47);CHR$(n) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

.. _graphic-bitmap-1:

Graphic Bitmap
~~~~~~~~~~~~~~

Epson emulation can print bitmap data. An image is defined by a bit
array of 8 rows. Each column is encoded in a byte, MSB is up. Horizontal
definition can be one of 60, 120 or 240 dpi. Vertical definition is 72
dpi.

Example for a 16 columns array:

+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+
|       | 1  | 2  | 3   | 4   | 5   | 6  | 7  | 8  | 9  | 10  | 11  | 12  | 13 | 14 | 15  | 16 |
+=======+====+====+=====+=====+=====+====+====+====+====+=====+=====+=====+====+====+=====+====+
| 128   |    |    |     |     |     |    |    |    |    |     |     |     |    |    |     |    |
+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+
| 64    |    |    |     |     |     |    |    |    |    |     |     |     |    |    |     |    |
+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+
| 32    |    |    |     |     |     |    |    |    |    |     |     |     |    |    |     |    |
+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+
| 16    |    |    |     |     |     |    |    |    |    |     |     |     |    |    |     |    |
+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+
| 8     |    |    |     |     |     |    |    |    |    |     |     |     |    |    |     |    |
+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+
| 4     |    |    |     |     |     |    |    |    |    |     |     |     |    |    |     |    |
+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+
| 2     |    |    |     |     |     |    |    |    |    |     |     |     |    |    |     |    |
+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+
| 1     |    |    |     |     |     |    |    |    |    |     |     |     |    |    |     |    |
+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+
| Total | 60 | 66 | 129 | 129 | 129 | 66 | 60 | 24 | 60 | 126 | 255 | 126 | 60 | 24 | 235 | 24 |
+-------+----+----+-----+-----+-----+----+----+----+----+-----+-----+-----+----+----+-----+----+

Prior to BIM printing you need to change the line spacing to match the
graphic height. Standard line height in graphic mode is 1/9” (8/72”) if
you use 8 dots or 7/27” if you use 7 dots.

+-----------------------------------+-----------------------------------+
| **ESC K …**                       | Select the **Bit Image Mode** in  |
|                                   | simple density. You have to       |
| **27 75 …**                       | provide parameters **n m d\ 1     |
|                                   | d\ 2 …**                          |
| **1Bh 4Bh …**                     |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print. Default resolution |
|                                   | using **ESC K** is 60 dpi but it  |
|                                   | can be changed using command      |
|                                   | **ESC ?**                         |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | A$=CHR$(27)+CHR$(75)+CHR$(16)+CHR |
|                                   | $(0);                             |
|                                   |                                   |
|                                   | 30 FOR I=1 TO 16                  |
|                                   |                                   |
|                                   | 40 READ A:A$=A$+CHR$(A)           |
|                                   |                                   |
|                                   | 50 NEXT I                         |
|                                   |                                   |
|                                   | 60                                |
|                                   | PRINT#1,CHR$(27);CHR$(65);CHR$(8) |
|                                   | ;CHR$(10);CHR$(13)                |
|                                   |                                   |
|                                   | 70 FOR J=1 TO 3                   |
|                                   |                                   |
|                                   | 80                                |
|                                   | PRINT#1,A$;A$;A$;A$;CHR$(10);CHR$ |
|                                   | (13)                              |
|                                   |                                   |
|                                   | 90 NEXT J                         |
|                                   |                                   |
|                                   | 100 CLOSE1                        |
|                                   |                                   |
|                                   | 110 END                           |
|                                   |                                   |
|                                   | 120 DATA                          |
|                                   | 60,66,129,129,129,66,60,24        |
|                                   |                                   |
|                                   | 130 DATA                          |
|                                   | 60,126,255,126,60,24,235,24       |
|                                   |                                   |
|                                   | |image64|                         |
+===================================+===================================+
| **ESC L …**                       | Select the **Bit Image Mode** in  |
|                                   | double density, half speed. You   |
| **27 76 …**                       | have to provide parameters **n m  |
|                                   | d\ 1 d\ 2 …**                     |
| **1Bh 4Ch …**                     |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print. Default resolution |
|                                   | using **ESC L** is 120 dpi but it |
|                                   | can be changed using command      |
|                                   | **ESC ?**                         |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | A$=CHR$(27)+CHR$(76)+CHR$(16)+CHR |
|                                   | $(0);                             |
|                                   |                                   |
|                                   | 30 FOR I=1 TO 16                  |
|                                   |                                   |
|                                   | 40 READ A:A$=A$+CHR$(A)           |
|                                   |                                   |
|                                   | 50 NEXT I                         |
|                                   |                                   |
|                                   | 60                                |
|                                   | PRINT#1,CHR$(27);CHR$(65);CHR$(8) |
|                                   | ;CHR$(10);CHR$(13)                |
|                                   |                                   |
|                                   | 70 FOR J=1 TO 3                   |
|                                   |                                   |
|                                   | 80                                |
|                                   | PRINT#1,A$;A$;A$;A$;CHR$(10);CHR$ |
|                                   | (13)                              |
|                                   |                                   |
|                                   | 90 NEXT J                         |
|                                   |                                   |
|                                   | 100 CLOSE1                        |
|                                   |                                   |
|                                   | 110 END                           |
|                                   |                                   |
|                                   | 120 DATA                          |
|                                   | 60,66,129,129,129,66,60,24        |
|                                   |                                   |
|                                   | 130 DATA                          |
|                                   | 60,126,255,126,60,24,235,24       |
|                                   |                                   |
|                                   | |image65|                         |
+-----------------------------------+-----------------------------------+
| **ESC Y …**                       | Select the **Bit Image Mode** in  |
|                                   | double density, normal speed.     |
| **27 89 …**                       |                                   |
|                                   | On Ultimate-II Virtual Printer,   |
| **1Bh 59h …**                     | **ESC Y** behaves the same as     |
|                                   | **ESC L**                         |
+-----------------------------------+-----------------------------------+
| **ESC Z …**                       | Select the **Bit Image Mode** in  |
|                                   | quadruple density, half speed.    |
| **27 90 …**                       | You have to provide parameters    |
|                                   | **n m d\ 1 d\ 2 …**               |
| **1Bh 5Ah …**                     |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print. Default resolution |
|                                   | using **ESC Z** is 240 dpi but it |
|                                   | can be changed using command      |
|                                   | **ESC ?**                         |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | A$=CHR$(27)+CHR$(90)+CHR$(16)+CHR |
|                                   | $(0);                             |
|                                   |                                   |
|                                   | 30 FOR I=1 TO 16                  |
|                                   |                                   |
|                                   | 40 READ A:A$=A$+CHR$(A)           |
|                                   |                                   |
|                                   | 50 NEXT I                         |
|                                   |                                   |
|                                   | 60                                |
|                                   | PRINT#1,CHR$(27);CHR$(65);CHR$(8) |
|                                   | ;CHR$(10);CHR$(13)                |
|                                   |                                   |
|                                   | 70 FOR J=1 TO 3                   |
|                                   |                                   |
|                                   | 80                                |
|                                   | PRINT#1,A$;A$;A$;A$;CHR$(10);CHR$ |
|                                   | (13)                              |
|                                   |                                   |
|                                   | 90 NEXT J                         |
|                                   |                                   |
|                                   | 100 CLOSE1                        |
|                                   |                                   |
|                                   | 110 END                           |
|                                   |                                   |
|                                   | 120 DATA                          |
|                                   | 60,66,129,129,129,66,60,24        |
|                                   |                                   |
|                                   | 130 DATA                          |
|                                   | 60,126,255,126,60,24,235,24       |
|                                   |                                   |
|                                   | |image66|                         |
+-----------------------------------+-----------------------------------+
| **ESC \* …**                      | Select the **Bit Image Mode**     |
|                                   | with provided density. You have   |
| **27 42 …**                       | to provide parameters **d n m     |
|                                   | d\ 1 d\ 2 …**                     |
| **1Bh 2Ah …**                     |                                   |
|                                   | Value **d** is horizontal density |
|                                   | as shown in this table :          |
|                                   |                                   |
|                                   | +------+------+------+------+     |
|                                   | | d    | DENS | DESC | MAX  |     |
|                                   | |      | ITY  | RIPT | DOTS |     |
|                                   | |      |      | ION  | /LIN |     |
|                                   | |      |      |      | E    |     |
|                                   | +======+======+======+======+     |
|                                   | | 0    | 60   | Sing | 480  |     |
|                                   | |      | dpi  | le   |      |     |
|                                   | +------+------+------+------+     |
|                                   | | 1    | 120  | Doub | 960  |     |
|                                   | |      | dpi  | le   |      |     |
|                                   | +------+------+------+------+     |
|                                   | | 2    | 120  | Hi-s | 960  |     |
|                                   | |      | dpi  | peed |      |     |
|                                   | |      |      | doub |      |     |
|                                   | |      |      | le   |      |     |
|                                   | |      |      | (sam |      |     |
|                                   | |      |      | e    |      |     |
|                                   | |      |      | as 1 |      |     |
|                                   | |      |      | in   |      |     |
|                                   | |      |      | Ulti |      |     |
|                                   | |      |      | mate |      |     |
|                                   | |      |      | )    |      |     |
|                                   | +------+------+------+------+     |
|                                   | | 3    | 240  | Quad | 1920 |     |
|                                   | |      | dpi  | rupl |      |     |
|                                   | |      |      | e    |      |     |
|                                   | +------+------+------+------+     |
|                                   | | 4    | 80   | CRT  | 640  |     |
|                                   | |      | dpi  | scre |      |     |
|                                   | |      |      | en   |      |     |
|                                   | +------+------+------+------+     |
|                                   | | 5    | 72   | Plot | 576  |     |
|                                   | |      | dpi  | ter  |      |     |
|                                   | +------+------+------+------+     |
|                                   | | 6    | 90   | Hi-r | 720  |     |
|                                   | |      | dpi  | es   |      |     |
|                                   | |      |      | CRT  |      |     |
|                                   | +------+------+------+------+     |
|                                   |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of bitmap data |
|                                   | (n is LSB) total = n + m x 256    |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print.                    |
+-----------------------------------+-----------------------------------+
| **ESC ? n m**                     | Change density for bitmap         |
|                                   | commands. Value **n** is one from |
| **27 63 n m**                     | **K**, **L**, **Y** or **Z**.     |
|                                   | Value m is the new density for    |
| **1Bh 3Fh n m**                   | the command (see table in **ESC   |
|                                   | \*** description).                |
|                                   |                                   |
|                                   | Example, to change density of ESC |
|                                   | L to 80dpi :                      |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(63);”L”;CHR |
|                                   | $(4)                              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC ^ …**                       | Select the **Bit Image Mode**     |
|                                   | using all the 9 pin of the head.  |
| **27 94 …**                       | You have to provide parameters    |
|                                   | **d n m h\ 1 l\ 1 h\ 2 l\ 2 …**   |
| **1Bh 5Eh …**                     |                                   |
|                                   | Value **d** is density. Only 0    |
|                                   | and 1 are allowed for single      |
|                                   | (60dpi) or double density (120    |
|                                   | dpi).                             |
|                                   |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **h\ 1 l\ 1 h\ 2 l\ 2 …** are the |
|                                   | bitmap data to print. Values      |
|                                   | **h\ n** encode the upper 8 dots  |
|                                   | and values **l\ n** encode the    |
|                                   | lower dot in the MSB bit          |
|                                   | (2:sup:`7`\ =128). This needs     |
|                                   | double of data for just one more  |
|                                   | dot.                              |
|                                   |                                   |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 9-Dots |  |  |                  |
|                                   | +========+==+==+================= |
|                                   | ==+                               |
|                                   | | 128    |  |  | 1\ :sup:`st` byt |
|                                   | e |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 64     |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 32     |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 16     |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 8      |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 4      |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 2      |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 1      |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 128    |  |  | 2\ :sup:`nd` byt |
|                                   | e |                               |
|                                   | |        |  |  |                  |
|                                   |   |                               |
|                                   | |        |  |  | *Grey is unused* |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 64     |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 32     |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 16     |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 8      |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 4      |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 2      |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
|                                   | | 1      |  |  |                  |
|                                   |   |                               |
|                                   | +--------+--+--+----------------- |
|                                   | --+                               |
+-----------------------------------+-----------------------------------+

Charset selection
~~~~~~~~~~~~~~~~~

FX-80 emulation uses ASCII7 to encode characters. This allows only 128
combinations to address characters. When MSB is set to 1 the character
is printed using Italic (MSB is 2\ :sup:`7`\ =128).

+-----------------------------------+-----------------------------------+
| **ESC 7**                         | Select Basic character table.     |
|                                   | This is the default charset for   |
| **27 55**                         | FX-80 printer.                    |
|                                   |                                   |
| **1Bh 37h**                       | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(55);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **ESC R n**                       | Select National character table.  |
|                                   | Value **n** selects the character |
| **27 82 n**                       | table :                           |
|                                   |                                   |
| **1Bh 52h n**                     | +----+--------------------------+ |
|                                   | | n  | NATIONAL CHARACTER TABLE | |
|                                   | +====+==========================+ |
|                                   | | 0  | USA                      | |
|                                   | +----+--------------------------+ |
|                                   | | 1  | France                   | |
|                                   | +----+--------------------------+ |
|                                   | | 2  | Germany                  | |
|                                   | +----+--------------------------+ |
|                                   | | 3  | UK                       | |
|                                   | +----+--------------------------+ |
|                                   | | 4  | Denmark I                | |
|                                   | +----+--------------------------+ |
|                                   | | 5  | Sweden                   | |
|                                   | +----+--------------------------+ |
|                                   | | 6  | Italy                    | |
|                                   | +----+--------------------------+ |
|                                   | | 7  | Spain                    | |
|                                   | +----+--------------------------+ |
|                                   | | 8  | Japan                    | |
|                                   | +----+--------------------------+ |
|                                   | | 9  | Norway                   | |
|                                   | +----+--------------------------+ |
|                                   | | 10 | Denmark II               | |
|                                   | +----+--------------------------+ |
|                                   |                                   |
|                                   | See national charset changes      |
|                                   | compared to basic charset in      |
|                                   | chapter 10.3                      |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(82);CHR$(1) |
|                                   | ;”FRENCH                          |
|                                   | CHARSET”                          |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC I 1**                       | Enable the extension of the       |
|                                   | character table. Parameter 1 can  |
| **27 73 1**                       | be passed using the ‘1’ character |
|                                   | (33, 31h). See table in chapter   |
| **1Bh 49h 01h**                   | 10.2 for details about extended   |
|                                   | charset.                          |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(73);CHR$(1) |
|                                   | ;”EXTENDED                        |
|                                   | CHARSET ENABLED”                  |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC I 0**                       | Disable the extension of the      |
|                                   | character table. Parameter 0 can  |
| **27 73 0**                       | be passed using the ‘0’ character |
|                                   | (32, 30h).                        |
| **1Bh 49h 00h**                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(73);CHR$(0) |
|                                   | ;”EXTENDED                        |
|                                   | CHARSET DISABLED”                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 6**                         | Extend only the italic part of    |
|                                   | the printable charset             |
| **27 54**                         |                                   |
|                                   | This command is ignored by        |
| **1Bh 36h**                       | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(54);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

.. _character-creation-down-line-loading-dll-1:

Character creation, Down Line Loading (DLL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All the commands related to character creation are ignored in the
Ultimate-II Virtual Printer. The commands are understood and correctly
interpreted but ignored to skip them gently.

+-----------------------------------+-----------------------------------+
| **ESC : 000**                     | Copy standard character generator |
|                                   | from ROM to RAM.                  |
| **27 58 0 0 0**                   |                                   |
|                                   | This command is ignored by        |
| **1Bh 3Ah 0 0 0**                 | Ultimate-II Virtual Printer.      |
+===================================+===================================+
| **ESC & 0**                       | This code has to be followed by   |
|                                   | parameters **n m a p\ 1           |
| **27 38 0**                       | p\ 2**\ …\ **p\ 11** which        |
|                                   | represents decimal byte codes to  |
| **1Bh 26h 00h**                   | describe characters to load.      |
|                                   |                                   |
|                                   | **0** is code 0, always present.  |
|                                   |                                   |
|                                   | **n** ASCII code of first         |
|                                   | redefined char                    |
|                                   |                                   |
|                                   | **m** ASCII code of last          |
|                                   | redefined char (n=m if only one   |
|                                   | char to define)                   |
|                                   |                                   |
|                                   | next parameters are repeated for  |
|                                   | each defined char.                |
|                                   |                                   |
|                                   | | **a** This parameter tells      |
|                                   |   which needles have to be used   |
|                                   |   to print that character. Head   |
|                                   |   has 9 needles of which 8 can be |
|                                   |   used here.                      |
|                                   | | a = 0 : use the 8 upper needles |
|                                   | | a = 1 : use the 8 lower needles |
|                                   |                                   |
|                                   | **p\ 1 p\ 2\ …p\ 11** Represents  |
|                                   | the 11 columns defining the dots  |
|                                   | printed for the character.        |
|                                   |                                   |
|                                   | In the 8x11 matrix you have to    |
|                                   | remind that a dot active in a     |
|                                   | column cannot be active in the    |
|                                   | next column to let the head       |
|                                   | recycle. Ultimate-II Virtual      |
|                                   | Printer does not suffer from this |
|                                   | limitation.                       |
+-----------------------------------+-----------------------------------+
| **ESC % n**                       | If n=1 select RAM (special        |
|                                   | characters) and if n=0 select ROM |
| **27 37 n**                       | (standard characters)             |
|                                   |                                   |
| **1Bh 25h n**                     | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+

Other commands
~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **DC1**                           | **Select the printer**. Wake up   |
|                                   | the printer if the printer has    |
| **17**                            | been disabled with DC3.           |
|                                   |                                   |
| **11h**                           | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
+===================================+===================================+
| **DC3**                           | **Suspend the printer**. The      |
|                                   | printer will ignore the input     |
| **19**                            | data until DC1 is sent.           |
|                                   |                                   |
| **13h**                           | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **CAN**                           | **Cancel** the current job and    |
|                                   | clear printer buffer.             |
| **24**                            |                                   |
|                                   | This command is ignored by        |
| **18h**                           | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **ESC =**                         | Force **bit 7** (MSB) to 0. All   |
|                                   | data received will have its bit 7 |
| **27 61**                         | cleared except commands.          |
|                                   |                                   |
| **1Bh 3Dh**                       | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **ESC >**                         | Force **bit 7** (MSB) to 1. All   |
|                                   | data received will have its bit 7 |
| **27 62**                         | set except commands.              |
|                                   |                                   |
| **1Bh 3Eh**                       | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **ESC #**                         | Clear **bit 7** (MSB) forcing.    |
|                                   |                                   |
| **27 35**                         | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
| **1Bh 23h**                       |                                   |
+-----------------------------------+-----------------------------------+
| **ESC <**                         | Set **left to right** printing    |
|                                   | for one line.                     |
| **27 60**                         |                                   |
|                                   | This command is ignored by        |
| **1Bh 3Ch**                       | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **ESC @**                         | **Initialize** the printer. Set   |
|                                   | all parameters to default values. |
| **27 64**                         | Paper and head are not moved.     |
|                                   |                                   |
| **1Bh 40h**                       |                                   |
+-----------------------------------+-----------------------------------+
| **ESC U n**                       | Select **Mono/Bidirectional**     |
|                                   | printing.                         |
| **27 85 n                         |                                   |
| 1Bh 30h n**                       | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | | n=0 : bidirectional             |
|                                   | | n=1 : mono-directional (left to |
|                                   |   right) for better alignment.    |
+-----------------------------------+-----------------------------------+
| **ESC i n**                       | Immediate character printing      |
|                                   | ON/OFF like a typewriter.         |
| **27 105 n**                      |                                   |
|                                   | | This command is ignored by      |
| **1Bh 69h n**                     |   Ultimate-II Virtual Printer.    |
|                                   | | n=1 : immediate printing ON     |
|                                   |   (incompatible with continuous   |
|                                   |   paper feeding)                  |
|                                   |                                   |
|                                   | n=0 : immediate printing OFF      |
+-----------------------------------+-----------------------------------+
| **ESC s n**                       | Half speed printing ON/OFF to     |
|                                   | make less noise.                  |
|                                   |                                   |
|                                   | | This command is ignored by      |
|                                   |   Ultimate-II Virtual Printer.    |
|                                   | | n=1 : half speed                |
|                                   |                                   |
|                                   | n=0 : full speed                  |
+-----------------------------------+-----------------------------------+
| **DEL**                           | Delete the last printable         |
|                                   | character from buffer.            |
| **127**                           |                                   |
|                                   | This command is ignored by        |
| **7Fh**                           | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+

IBM Graphics Printer commands
=============================

This chapter describes the commands the printer can understand when
using the IBM Graphics Printer emulation. The power of IBM printers
resides in its charsets using ASCII8.

.. _secondary-address-2:

Secondary address
-----------------

Secondary address on OPEN command is not used by IBM Graphics Printer
emulation.

.. _commands-2:

Commands
--------

.. _graphical-operations-2:

Graphical operations
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **ESC G**                         | Select the **Double Strike**      |
|                                   | print mode. Characters are        |
| **27 71**                         | printed twice and paper is lifted |
|                                   | 1/216” between the two passes.    |
| **1Bh 47h**                       |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);chr$(71);”DOUBLE |
|                                   | STRIKE”                           |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image76|                         |
+===================================+===================================+
| **ESC H**                         | Disable **Double Strike** print   |
|                                   | mode                              |
| **27 72**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 48h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);chr$(72);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **SO**                            | Select the **Double Width** print |
|                                   | mode                              |
| **14**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **0Eh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(14);”DOUBLE       |
|                                   | WIDTH”                            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image77|                         |
+-----------------------------------+-----------------------------------+
| **DC4**                           | Disable the **Double Width**      |
|                                   | print mode                        |
| **20**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **14h**                           |                                   |
|                                   | 20 PRINT#1,CHR$(20);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC SO**                        | Same as **SO** (Double Width      |
|                                   | print mode ON).                   |
| **27 14**                         |                                   |
|                                   |                                   |
| **1Bh 0Eh**                       |                                   |
+-----------------------------------+-----------------------------------+
| **ESC W 1**                       | Same as **SO** (Double Width ON). |
|                                   | 1 can be sent with ASCII code of  |
| **27 87 1**                       | ‘1’ (49 - 31h)                    |
|                                   |                                   |
| **1Bh 57h 01h**                   |                                   |
+-----------------------------------+-----------------------------------+
| **ESC W 0**                       | Same as **DC4** (Double Width     |
|                                   | OFF). 0 can be sent with ASCII    |
| **27 87 0**                       | code of ‘0’ (48 - 30h)            |
|                                   |                                   |
| **1Bh 57h 00h**                   |                                   |
+-----------------------------------+-----------------------------------+
| **ESC – 1**                       | Select the **Underline** print    |
|                                   | mode for all characters and       |
| **27 45 49**                      | spaces that follow.               |
|                                   |                                   |
| **1Bh 2Dh 31h**                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(45);CHR$(49 |
|                                   | );”UNDERLINE”                     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image78|                         |
+-----------------------------------+-----------------------------------+
| **ESC - 0**                       | Disable the Underline print mode. |
|                                   |                                   |
| **27 45 48**                      | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 2Dh 30h**                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(45);CHR$(48 |
|                                   | );                                |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC E**                         | Select the **Bold** print mode.   |
|                                   |                                   |
| **27 69**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 45h**                       | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(69);”BOLD”  |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image79|                         |
+-----------------------------------+-----------------------------------+
| **ESC F**                         | Disable the Bold print mode.      |
|                                   |                                   |
| **27 70**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 46h**                       | 20 PRINT#1,CHR$(27);CHR$(70);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 4**                         | Select the **Italic** print mode. |
|                                   |                                   |
| **27 52**                         | This feature has been added in    |
|                                   | Ultimate-II Virtual Printer and   |
| **1Bh 34h**                       | does not exist in a real MPS-1230 |
|                                   | printer. Italic was not supported |
|                                   | in IBM Graphics Printer.          |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(52);”ITALIC |
|                                   | ”                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image80|                         |
+-----------------------------------+-----------------------------------+
| **ESC 5**                         | Disable the **Italic** print      |
|                                   | mode.                             |
| **27 53**                         |                                   |
|                                   | This feature has been added in    |
| **1Bh 35h**                       | Ultimate-II Virtual Printer and   |
|                                   | does not exist in a real MPS-1230 |
|                                   | printer. Italic was not supported |
|                                   | in IBM Graphics Printer.          |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(53);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **SI**                            | Select the **CONDENSED** spacing  |
|                                   | mode (17.1 chars/inch)            |
| **15**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **0Fh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(15);”CONDENSED”   |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC M**                         | Select the **ELITE** spacing mode |
|                                   | (12 chars/inch).                  |
| **27 77**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 4Dh**                       |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(77);”PICA”  |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **DC2**                           | Select the **PICA** spacing mode  |
|                                   | (10 chars/inch). This is the      |
| **18**                            | default spacing.                  |
|                                   |                                   |
| **12h**                           | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(18);”PICA”        |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC [ n**                       | Select the spacing mode depending |
|                                   | on parameter “n” as described on  |
| **27 91 n**                       | this table:                       |
|                                   |                                   |
| **1Bh 5Bh n**                     | +---------+---------+---------+   |
|                                   | | n       | SPACING |             |
|                                   | +=========+=========+=========+   |
|                                   | | 0       | PICA    | 10      |   |
|                                   | |         |         | chars/i |   |
|                                   | |         |         | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 1       | ELITE   | 12      |   |
|                                   | |         |         | chars/i |   |
|                                   | |         |         | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 2       | MICRO   | 15      |   |
|                                   | |         |         | chars/i |   |
|                                   | |         |         | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 3       | CONDENS | 17.1    |   |
|                                   | |         | ED      | chars/i |   |
|                                   | |         |         | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 4       | PICA    | 20      |   |
|                                   | |         | COMPRES | chars/i |   |
|                                   | |         | SED     | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 5       | ELITE   | 24      |   |
|                                   | |         | COMPRES | chars/i |   |
|                                   | |         | SED     | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   | | 6       | MICRO   | 30      |   |
|                                   | |         | COMPRES | chars/i |   |
|                                   | |         | SED     | nch     |   |
|                                   | +---------+---------+---------+   |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(91);CHR$(n) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image81|                         |
+-----------------------------------+-----------------------------------+
| **ESC S 0**                       | Select the **Superscript** print  |
|                                   | mode. Characters are half high    |
| **27 83 48**                      | than the normal height and are    |
|                                   | printer on the upper half         |
| **1Bh 53h 30h**                   | interline.                        |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,”NORMAL”;CHR$(27);CHR$(83 |
|                                   | );CHR$(48);”SUPERSCRIPT”          |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image82|                         |
+-----------------------------------+-----------------------------------+
| **ESC S 1**                       | Select the **Subscript** print    |
|                                   | mode. Characters are half high    |
| **27 83 49**                      | than the normal height and are    |
|                                   | printer on the lower half         |
| **1Bh 53h 31h**                   | interline.                        |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,”NORMAL”;CHR$(27);CHR$(83 |
|                                   | );CHR$(49);”SUBSCRIPT”            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image83|                         |
+-----------------------------------+-----------------------------------+
| **ESC T**                         | Disable Superscript and Subscript |
|                                   | print mode.                       |
| **27 84**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 54h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(84);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC x n**                       | If n=0, select standard quality   |
|                                   | mode (Draft)                      |
| **27 120 n**                      |                                   |
|                                   | If n=1, select near letter        |
| **1Bh 78h n**                     | quality mode (NLQ)                |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(120);CHR$(n |
|                                   | );                                |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image84|                         |
+-----------------------------------+-----------------------------------+
| **ESC ! n**                       | Select graphical layout for text. |
|                                   |                                   |
| **27 33 n**                       | This feature has been added in    |
|                                   | Ultimate-II Virtual Printer and   |
| **1Bh 21h n**                     | does not exist in a real MPS-1230 |
|                                   | printer. See EPSON-FX80 command   |
|                                   | description page 22 for details.  |
+-----------------------------------+-----------------------------------+

.. _paper-feeding-2:

Paper feeding
~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **LF**                            | A **Line Feed** advances the      |
|                                   | paper to the next line (behavior  |
| **10**                            | is LF only, no CR).               |
|                                   |                                   |
| **0Ah**                           | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(10);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **CR**                            | A **Carriage Return** returns the |
|                                   | print head to le left margin but  |
| **13**                            | stays on the same line (behavior  |
|                                   | is CR only, no LF).               |
| **0Dh**                           |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(13);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **FF**                            | A **Form Feed** prints the        |
|                                   | current page to a PNG file and    |
| **12**                            | then continues printing on the    |
|                                   | first line of a new blank page.   |
| **0Ch**                           |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(12);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 0**                         | Select vertical spacing **1/8”**  |
|                                   | between each printed line.        |
| **27 48**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 30h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(48);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 1**                         | Select vertical spacing **7/72”** |
|                                   | between each printed line.        |
| **27 49**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 31h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(49);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 2**                         | Select vertical spacing **1/6”**  |
|                                   | between each printed line.        |
| **27 50**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 32h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(50);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 3 n**                       | Select vertical spacing           |
|                                   | **n/216”** between each printed   |
| **27 51 n**                       | line.                             |
|                                   |                                   |
| **1Bh 32h n**                     | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(51);CHR$(37 |
|                                   | )”37/216                          |
|                                   | inch”                             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC A n**                       | Select vertical spacing **n/72”** |
|                                   | between each printed line.        |
| **27 65 n**                       |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 41h n**                     |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(65);CHR$(8) |
|                                   | ”8/72                             |
|                                   | inch for one pass BIM”            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC J n**                       | Skip down **n/216”** of paper.    |
|                                   |                                   |
| **27 74 n**                       | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 4Ah n**                     | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(74);CHR$(70 |
|                                   | )”70/216                          |
|                                   | inch skipped”                     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

.. _format-control-2:

Format control
~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **BS**                            | **Backspace**, go back one        |
|                                   | character. Left character is not  |
| **8**                             | erased and next character will be |
|                                   | printed over it. You can combine  |
| **08h**                           | characters this way.              |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,”a”;CHR$(8)”^ to print |
|                                   | a with a circumflex”;             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **ESC C n**                       | Defines the page length in number |
|                                   | of lines (range 1-127). Current   |
| **27 67 n**                       | line spacing is used to calculate |
|                                   | form length.                      |
| **1Bh 43h n**                     |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(67);CHR$(1- |
|                                   | 127);                             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC C NUL n**                   | Defines the page length in inches |
|                                   | (range 1-22).                     |
| **27 67 0 n**                     |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 43h 00h n**                 |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(67);CHR$(0) |
|                                   | ;CHR$(1-22);                      |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC N m**                       | Define the **Bottom of Form**     |
|                                   | (BOF) in number “m” of lines at   |
| **27 78 m**                       | the end of the page that are      |
|                                   | skipped to jump over perforations |
| **1Bh 4Eh m**                     | when using continuous paper.      |
|                                   |                                   |
|                                   | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(78);CHR$(m) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC O**                         | Disable the **Bottom of Form**    |
|                                   | (BOF).                            |
| **27 79**                         |                                   |
|                                   | This command is ignored by        |
| **1Bh 4Fh**                       | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(79);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 8**                         | Disable the end of paper detector |
|                                   | to be able to print until the end |
| **27 56**                         | of the paper.                     |
|                                   |                                   |
| **1Bh 38h**                       | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(56);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 9**                         | Enable the end of paper detector. |
|                                   |                                   |
| **27 57**                         | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
| **1Bh 39h**                       |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(57);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **TAB**                           | This is the traditional           |
|                                   | **horizontal tabulation**. Head   |
| **9**                             | jumps to the next tabulation      |
|                                   | stop. Default stops are located   |
| **09h**                           | every 8 PICA character position   |
|                                   | since the beginning of a line.    |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(9);”THIS IS THE   |
|                                   | PRINT POSITION 8”                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **VT**                            | The same behavior as **LF**.      |
|                                   | Advances the paper to the next    |
| **11**                            | line (no CR).                     |
|                                   |                                   |
| **0Bh**                           | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(11);”JUMPED ONE   |
|                                   | LINE”                             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC D n\ 1 … 0**                | Define the **horizontal           |
|                                   | tabulation stop program**. Each   |
| **27 68 n\ 1 … 0**                | value **n** represents a          |
|                                   | character position where to set a |
| **1Bh 44h n\ 1 … 0**              | tab stop in ascending order. Last |
|                                   | one is 0 to tell that the         |
|                                   | sequence has ended. Up to 32      |
|                                   | stops can be created. Current     |
|                                   | char pitch is used to calculate   |
|                                   | tab position in the line.         |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(68);CHR$(10 |
|                                   | );CHR$(20);CHR$(30);CHR$(0)       |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

.. _graphic-bitmap-2:

Graphic Bitmap
~~~~~~~~~~~~~~

IBM Graphics Printer emulation prints bitmap data the same way as EPSON
FX-80. An image is defined by a bit array of 8 rows. Each column is
encoded in a byte, MSB is up. Horizontal definition can be one of 60,
120 or 240 dpi. Vertical definition is 72 dpi. See Graphic Bitmap for
EPSON page 26 for details.

+-----------------------------------+-----------------------------------+
| **ESC K …**                       | Select the **Bit Image Mode** in  |
|                                   | simple density (60 dpi). You have |
| **27 75 …**                       | to provide parameters **n m d\ 1  |
|                                   | d\ 2 …**                          |
| **1Bh 4Bh …**                     |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print.                    |
|                                   |                                   |
|                                   | *See EPSON command description    |
|                                   | page* *27 for an example.*        |
+===================================+===================================+
| **ESC L …**                       | Select the **Bit Image Mode** in  |
|                                   | double density (120 dpi), half    |
| **27 76 …**                       | speed. You have to provide        |
|                                   | parameters **n m d\ 1 d\ 2 …**    |
| **1Bh 4Ch …**                     |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print.                    |
|                                   |                                   |
|                                   | *See EPSON command description    |
|                                   | page* *27 for an example.*        |
+-----------------------------------+-----------------------------------+
| **ESC Y …**                       | Select the **Bit Image Mode** in  |
|                                   | double density (120 dpi), normal  |
| **27 89 …**                       | speed.                            |
|                                   |                                   |
| **1Bh 59h …**                     | On Ultimate-II Virtual Printer,   |
|                                   | **ESC Y** behaves the same as     |
|                                   | **ESC L**                         |
+-----------------------------------+-----------------------------------+
| **ESC Z …**                       | Select the **Bit Image Mode** in  |
|                                   | quadruple density (240 dpi), half |
| **27 90 …**                       | speed. You have to provide        |
|                                   | parameters **n m d\ 1 d\ 2 …**    |
| **1Bh 5Ah …**                     |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print.                    |
|                                   |                                   |
|                                   | *See EPSON command description    |
|                                   | page* *28 for an example.*        |
+-----------------------------------+-----------------------------------+

.. _charset-selection-1:

Charset selection
~~~~~~~~~~~~~~~~~

IBM emulation uses ASCII8 to encode characters. This allows 256
combinations to address characters. IBM printers work with 2 character
tables. Default is Table 1 described page 56. Table2 is configurable by
the user in Ultimate Printer configuration menu from 6 possible
international tables. A command can select Table 2 but no command can
change the international setting.

+-----------------------------------+-----------------------------------+
| **ESC 7**                         | Select **Table 1** character set. |
|                                   | This is the default charset for   |
| **27 55**                         | IBM printers.                     |
|                                   |                                   |
| **1Bh 37h**                       | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(55);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **ESC 6**                         | Select **Table 2** character set. |
|                                   | This is the international charset |
| **27 54**                         | user configured.                  |
|                                   |                                   |
| **1Bh 36h**                       | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(54);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

.. _character-creation-down-line-loading-dll-2:

Character creation, Down Line Loading (DLL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All the commands related to character creation are ignored in the
Ultimate-II Virtual Printer. The commands are understood and correctly
interpreted but ignored to skip them gently.

+-----------------------------------+-----------------------------------+
| **ESC =**                         | This code has to be followed by   |
|                                   | parameters **m n** and data.      |
| **27 61**                         |                                   |
|                                   | This command is ignored by        |
| **1Bh 3Dh**                       | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | **m** and **n** are the number of |
|                                   | bytes to load in order to have n  |
|                                   | + (m x 256) = size                |
+===================================+===================================+
| **ESC I n**                       | Select the print quality          |
|                                   | depending on parameter “n”        |
| **27 73 n**                       |                                   |
|                                   | n=0 standard quality (draft) and  |
| **1Bh 49h n**                     | normal characters                 |
|                                   |                                   |
|                                   | n=2 near letter quality (NLQ) and |
|                                   | normal characters                 |
|                                   |                                   |
|                                   | n=4 standard quality (draft) and  |
|                                   | special characters created with   |
|                                   | Down Line Loading (DLL). Not      |
|                                   | supported on Ultimate-II Virtual  |
|                                   | Printer, same behavior as n=0.    |
|                                   |                                   |
|                                   | n=6 near letter quality (NLQ) and |
|                                   | special characters created with   |
|                                   | Down Line Loading (DLL). Not      |
|                                   | supported on Ultimate-II Virtual  |
|                                   | Printer, same behavior as n=2.    |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(73);CHR$(n) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image86|                         |
+-----------------------------------+-----------------------------------+

.. _other-commands-1:

Other commands
~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **BELL**                          | Make a short beep.                |
|                                   |                                   |
| **7**                             | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
| **07h**                           |                                   |
+===================================+===================================+
| **CAN**                           | **Cancel** the current job and    |
|                                   | clear printer buffer.             |
| **24**                            |                                   |
|                                   | This command is ignored by        |
| **18h**                           | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **ESC <**                         | Set **left to right** printing    |
|                                   | for one line.                     |
| **27 60**                         |                                   |
|                                   | This command is ignored by        |
| **1Bh 3Ch**                       | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **ESC @**                         | **Initialize** the printer. Set   |
|                                   | all parameters to default values. |
| **27 64**                         | Paper and head are not moved.     |
|                                   |                                   |
| **1Bh 40h**                       | This feature has been added in    |
|                                   | Ultimate-II Virtual Printer and   |
|                                   | does not exist in a real MPS-1230 |
|                                   | printer.                          |
+-----------------------------------+-----------------------------------+
| **ESC U n**                       | Select **Mono/Bidirectional**     |
|                                   | printing.                         |
| **27 85 n                         |                                   |
| 1Bh 30h n**                       | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | | n=0 : bidirectional             |
|                                   | | n=1 : mono-directional (left to |
|                                   |   right) for better alignment.    |
+-----------------------------------+-----------------------------------+

IBM Proprinter commands
=======================

This chapter describes the commands the printer can understand when
using the IBM Proprinter emulation. This is the less powerful emulation
that the MPS-1230 can do. IBM Proprinter was a widely spread printer in
the office and business world.

.. _secondary-address-3:

Secondary address
-----------------

Secondary address on OPEN command is not used by IBM Proprinter
emulation.

.. _commands-3:

Commands
--------

.. _graphical-operations-3:

Graphical operations
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **ESC G**                         | Select the **Double Strike**      |
|                                   | print mode. Characters are        |
| **27 71**                         | printed twice and paper is lifted |
|                                   | 1/216” between the two passes.    |
| **1Bh 47h**                       |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);chr$(71);”DOUBLE |
|                                   | STRIKE”                           |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image94|                         |
+===================================+===================================+
| **ESC H**                         | Disable **Double Strike** print   |
|                                   | mode                              |
| **27 72**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 48h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);chr$(72);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **SO**                            | Select the **Double Width** print |
|                                   | mode                              |
| **14**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **0Eh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(14);”DOUBLE       |
|                                   | WIDTH”                            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image95|                         |
+-----------------------------------+-----------------------------------+
| **DC4**                           | Disable the **Double Width**      |
|                                   | print mode                        |
| **20**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **14h**                           |                                   |
|                                   | 20 PRINT#1,CHR$(20);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC W 1**                       | Same as **SO** (Double Width ON). |
|                                   | 1 can be sent with ASCII code of  |
| **27 87 1**                       | ‘1’ (49 - 31h)                    |
|                                   |                                   |
| **1Bh 57h 01h**                   |                                   |
+-----------------------------------+-----------------------------------+
| **ESC W 0**                       | Same as **DC4** (Double Width     |
|                                   | OFF). 0 can be sent with ASCII    |
| **27 87 0**                       | code of ‘0’ (48 - 30h)            |
|                                   |                                   |
| **1Bh 57h 00h**                   |                                   |
+-----------------------------------+-----------------------------------+
| **ESC – 1**                       | Select the **Underline** print    |
|                                   | mode for all characters and       |
| **27 45 49**                      | spaces that follow.               |
|                                   |                                   |
| **1Bh 2Dh 31h**                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(45);CHR$(49 |
|                                   | );”UNDERLINE”                     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image96|                         |
+-----------------------------------+-----------------------------------+
| **ESC - 0**                       | Disable the Underline print mode. |
|                                   |                                   |
| **27 45 48**                      | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 2Dh 30h**                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(45);CHR$(48 |
|                                   | );                                |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC E**                         | Select the **Bold** print mode.   |
|                                   |                                   |
| **27 69**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 45h**                       | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(69);”BOLD”  |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image97|                         |
+-----------------------------------+-----------------------------------+
| **ESC F**                         | Disable the Bold print mode.      |
|                                   |                                   |
| **27 70**                         | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 46h**                       | 20 PRINT#1,CHR$(27);CHR$(70);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **SI**                            | Select the **CONDENSED** spacing  |
|                                   | mode (17.1 chars/inch)            |
| **15**                            |                                   |
|                                   | 10 OPEN1,4                        |
| **0Fh**                           |                                   |
|                                   | 20 PRINT#1,CHR$(15);”CONDENSED”   |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **DC2**                           | Select the **PICA** spacing mode  |
|                                   | (10 chars/inch). This is the      |
| **18**                            | default spacing.                  |
|                                   |                                   |
| **12h**                           | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(18);”PICA”        |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC :**                         | Select the **ELITE** spacing mode |
|                                   | (12 chars/inch).                  |
| **27 58**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 3Ah**                       |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(58);”ELITE” |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC S 0**                       | Select the **Superscript** print  |
|                                   | mode. Characters are half high    |
| **27 83 48**                      | than the normal height and are    |
|                                   | printer on the upper half         |
| **1Bh 53h 30h**                   | interline.                        |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,”NORMAL”;CHR$(27);CHR$(83 |
|                                   | );CHR$(48);”SUPERSCRIPT”          |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image98|                         |
+-----------------------------------+-----------------------------------+
| **ESC S 1**                       | Select the **Subscript** print    |
|                                   | mode. Characters are half high    |
| **27 83 49**                      | than the normal height and are    |
|                                   | printer on the lower half         |
| **1Bh 53h 31h**                   | interline.                        |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,”NORMAL”;CHR$(27);CHR$(83 |
|                                   | );CHR$(49);”SUBSCRIPT”            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image99|                         |
+-----------------------------------+-----------------------------------+
| **ESC T**                         | Disable Superscript and Subscript |
|                                   | print mode.                       |
| **27 84**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 54h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(84);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC \_ n**                      | **Overline** ON/OFF. Will print a |
|                                   | line over the text.               |
| **27 95 n**                       |                                   |
|                                   | n=1: enable overline              |
| **1Bh 5Fh n**                     |                                   |
|                                   | n=0: disable overline             |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(95);CHR$(1) |
|                                   | ;”Overline”                       |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image100|                        |
+-----------------------------------+-----------------------------------+

.. _paper-feeding-3:

Paper feeding
~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **LF**                            | A **Line Feed** advances the      |
|                                   | paper to the next line (behavior  |
| **10**                            | is LF only, no CR).               |
|                                   |                                   |
| **0Ah**                           | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(10);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **CR**                            | A **Carriage Return** returns the |
|                                   | print head to le left margin but  |
| **13**                            | stays on the same line (behavior  |
|                                   | is CR only, no LF). You can       |
| **0Dh**                           | change the LF behavior with **ESC |
|                                   | 5** command.                      |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(13);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **FF**                            | A **Form Feed** prints the        |
|                                   | current page to a PNG file and    |
| **12**                            | then continues printing on the    |
|                                   | first line of a new blank page.   |
| **0Ch**                           |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(12);              |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 0**                         | Select vertical spacing **1/8”**  |
|                                   | between each printed line.        |
| **27 48**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 30h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(48);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 1**                         | Select vertical spacing **7/72”** |
|                                   | between each printed line.        |
| **27 49**                         |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 31h**                       |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(49);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 2**                         | Select vertical spacing **1/6”**  |
|                                   | between each printed line or      |
| **27 50**                         | activate **ESC A** previously     |
|                                   | prepared line spacing.            |
| **1Bh 32h**                       |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(50);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 3 n**                       | Select vertical spacing           |
|                                   | **n/216”** between each printed   |
| **27 51 n**                       | line.                             |
|                                   |                                   |
| **1Bh 32h n**                     | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(51);CHR$(37 |
|                                   | )”37/216                          |
|                                   | inch”                             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 5 n**                       | Automatic LF ON/OFF.              |
|                                   |                                   |
| **27 53 n**                       | n=1: LF is added on each CR       |
|                                   |                                   |
| **1Bh 35h n**                     | n=0: LF is not added on each CR   |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(53);CHR$(1) |
|                                   | ”NOW                              |
|                                   | AUTO LF ENABLED”                  |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC A n**                       | Prepare vertical spacing          |
|                                   | **n/72”** between each printed    |
| **27 65 n**                       | line but you will need to         |
|                                   | activate it with command ESC 2    |
| **1Bh 41h n**                     |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(65);CHR$(8) |
|                                   | ”8/72                             |
|                                   | inch for one pass BIM”            |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC J n**                       | Skip down **n/216”** of paper.    |
|                                   |                                   |
| **27 74 n**                       | 10 OPEN1,4                        |
|                                   |                                   |
| **1Bh 4Ah n**                     | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(74);CHR$(70 |
|                                   | )”70/216                          |
|                                   | inch skipped”                     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

.. _format-control-3:

Format control
~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **BS**                            | **Backspace**, go back one        |
|                                   | character. Left character is not  |
| **8**                             | erased and next character will be |
|                                   | printed over it. You can combine  |
| **08h**                           | characters this way.              |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,”a”;CHR$(8)”^ to print |
|                                   | a with a circumflex”;             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **ESC C n**                       | Defines the page length in number |
|                                   | of lines (range 1-127). Current   |
| **27 67 n**                       | line spacing is used to calculate |
|                                   | form length.                      |
| **1Bh 43h n**                     |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(67);CHR$(1- |
|                                   | 127);                             |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC C NUL n**                   | Defines the page length in inches |
|                                   | (range 1-22).                     |
| **27 67 0 n**                     |                                   |
|                                   | 10 OPEN1,4                        |
| **1Bh 43h 00h n**                 |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(67);CHR$(0) |
|                                   | ;CHR$(1-22);                      |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC N m**                       | Define the **Bottom of Form**     |
|                                   | (BOF) in number “m” of lines at   |
| **27 78 m**                       | the end of the page that are      |
|                                   | skipped to jump over perforations |
| **1Bh 4Eh m**                     | when using continuous paper.      |
|                                   |                                   |
|                                   | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4,7                      |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(78);CHR$(m) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC O**                         | Disable the **Bottom of Form**    |
|                                   | (BOF).                            |
| **27 79**                         |                                   |
|                                   | This command is ignored by        |
| **1Bh 4Fh**                       | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(79);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC 4**                         | Set Top Of Form (TOF). It uses    |
|                                   | the current print line as the top |
| **27 52**                         | margin for next pages. This       |
|                                   | configuration is kept until power |
| **1Bh 34h**                       | off or Printer Reset in the       |
|                                   | Ultimate action F5 menu.          |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(52);”NOW |
|                                   | THIS IS TOP MARGIN”               |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **TAB**                           | This is the traditional           |
|                                   | **horizontal tabulation**. Head   |
| **9**                             | jumps to the next tabulation      |
|                                   | stop. Default stops are located   |
| **09h**                           | every 8 PICA character position   |
|                                   | since the beginning of a line.    |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(9);”THIS IS THE   |
|                                   | PRINT POSITION 8”                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **VT**                            | Jump to next **vertical           |
|                                   | tabulation** stop. There is no    |
| **11**                            | Carriage Return. No default stops |
|                                   | are defined. If no vertical stops |
| **0Bh**                           | are defined, it will jump one     |
|                                   | line, same as LF.                 |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(11);”JUMPED TO    |
|                                   | NEXT VERTICAL STOP”               |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC B n\ 1 … 0**                | Define the **vertical tabulation  |
|                                   | stop program**. Each value **n**  |
| **27 66 n\ 1 … 0**                | represents a line number where to |
|                                   | set a vertical tab stop in        |
| **1Bh 42h n\ 1 … 0**              | ascending order. Last one is 0 to |
|                                   | tell that the sequence has ended. |
|                                   | Up to 32 stops can be created.    |
|                                   | Current line spacing is used to   |
|                                   | calculate tab position in the     |
|                                   | page.                             |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(66);CHR$(5) |
|                                   | ;CHR$(10);CHR$(15);CHR$(0)        |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC D n\ 1 … 0**                | Define the **horizontal           |
|                                   | tabulation stop program**. Each   |
| **27 68 n\ 1 … 0**                | value **n** represents a          |
|                                   | character position where to set a |
| **1Bh 44h n\ 1 … 0**              | tab stop in ascending order. Last |
|                                   | one is 0 to tell that the         |
|                                   | sequence has ended. Up to 32      |
|                                   | stops can be created. Current     |
|                                   | char pitch is used to calculate   |
|                                   | tab position in the line.         |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(68);CHR$(10 |
|                                   | );CHR$(20);CHR$(30);CHR$(0)       |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC R**                         | Clear tab stops. Horizontal stop  |
|                                   | are set to default (every 8       |
| **27 82**                         | characters) and vertical stops    |
|                                   | are deleted.                      |
| **1Bh 52h**                       |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(82);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

.. _graphic-bitmap-3:

Graphic Bitmap
~~~~~~~~~~~~~~

IBM Proprinter emulation prints bitmap data the same way as EPSON FX-80.
An image is defined by a bit array of 8 rows. Each column is encoded in
a byte, MSB is up. Horizontal definition can be one of 60, 120 or 240
dpi. Vertical definition is 72 dpi. See Graphic Bitmap for EPSON page 26
for details.

+-----------------------------------+-----------------------------------+
| **ESC K …**                       | Select the **Bit Image Mode** in  |
|                                   | simple density (60 dpi). You have |
| **27 75 …**                       | to provide parameters **n m d\ 1  |
|                                   | d\ 2 …**                          |
| **1Bh 4Bh …**                     |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print.                    |
|                                   |                                   |
|                                   | *See EPSON command description    |
|                                   | page* *27 for an example.*        |
+===================================+===================================+
| **ESC L …**                       | Select the **Bit Image Mode** in  |
|                                   | double density (120 dpi), half    |
| **27 76 …**                       | speed. You have to provide        |
|                                   | parameters **n m d\ 1 d\ 2 …**    |
| **1Bh 4Ch …**                     |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print.                    |
|                                   |                                   |
|                                   | *See EPSON command description    |
|                                   | page* *27 for an example.*        |
+-----------------------------------+-----------------------------------+
| **ESC Y …**                       | Select the **Bit Image Mode** in  |
|                                   | double density (120 dpi), normal  |
| **27 89 …**                       | speed.                            |
|                                   |                                   |
| **1Bh 59h …**                     | On Ultimate-II Virtual Printer,   |
|                                   | **ESC Y** behaves the same as     |
|                                   | **ESC L**                         |
+-----------------------------------+-----------------------------------+
| **ESC Z …**                       | Select the **Bit Image Mode** in  |
|                                   | quadruple density (240 dpi), half |
| **27 90 …**                       | speed. You have to provide        |
|                                   | parameters **n m d\ 1 d\ 2 …**    |
| **1Bh 5Ah …**                     |                                   |
|                                   | Values **n** and **m** are the 16 |
|                                   | bit encoded amount of data (n is  |
|                                   | LSB) total = n + m x 256          |
|                                   |                                   |
|                                   | **d\ 1 d\ 2 …** are the bitmap    |
|                                   | data to print.                    |
|                                   |                                   |
|                                   | *See EPSON command description    |
|                                   | page* *28 for an example.*        |
+-----------------------------------+-----------------------------------+

.. _charset-selection-2:

Charset selection
~~~~~~~~~~~~~~~~~

IBM emulation uses ASCII8 to encode characters. This allows 256
combinations to address characters. IBM printers work with 2 character
tables. Default is Table 1 described page 56. Table2 is configurable by
the user in Ultimate Printer configuration menu from 6 possible
international tables. A command can select Table 2 but no command can
change the international setting.

+-----------------------------------+-----------------------------------+
| **ESC 7**                         | Select **Table 1** character set. |
|                                   | This is the default charset for   |
| **27 55**                         | IBM printers.                     |
|                                   |                                   |
| **1Bh 37h**                       | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(55);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+===================================+===================================+
| **ESC 6**                         | Select **Table 2** character set. |
|                                   | This is the international charset |
| **27 54**                         | user configured.                  |
|                                   |                                   |
| **1Bh 36h**                       | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20 PRINT#1,CHR$(27);CHR$(54);     |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC \\ n**                      | Print **n** characters from       |
|                                   | extended table. In the next **n** |
| **27 92 n**                       | data, commands will not be        |
|                                   | interpreted. If a code is not     |
| **1Bh 5Ch n**                     | printable it will be replace with |
|                                   | a space.                          |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(92);CHR$(3) |
|                                   | ;CHR$(27);CHR$(92);CHR$(54);      |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+
| **ESC ^**                         | Print **one** character from      |
|                                   | extended table. The next data     |
| **27 94**                         | byte will not be interpreted as a |
|                                   | command. If the code is not       |
| **1Bh 5Eh**                       | printable it will be replace with |
|                                   | a space.                          |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(94);CHR$(13 |
|                                   | );                                |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
+-----------------------------------+-----------------------------------+

.. _character-creation-down-line-loading-dll-3:

Character creation, Down Line Loading (DLL)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All the commands related to character creation are ignored in the
Ultimate-II Virtual Printer. The commands are understood and correctly
interpreted but ignored to skip them gently.

+-----------------------------------+-----------------------------------+
| **ESC =**                         | This code has to be followed by   |
|                                   | parameters **m n** and data.      |
| **27 61**                         |                                   |
|                                   | **m** and **n** are the number of |
| **1Bh 3Dh**                       | bytes to load in order to have n  |
|                                   | + (m x 256) = size                |
|                                   |                                   |
|                                   | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
+===================================+===================================+
| **ESC I n**                       | Select the print quality          |
|                                   | depending on parameter “n”        |
| **27 73 n**                       |                                   |
|                                   | n=0 standard quality (draft) and  |
| **1Bh 49h n**                     | normal characters                 |
|                                   |                                   |
|                                   | n=2 near letter quality (NLQ) and |
|                                   | normal characters                 |
|                                   |                                   |
|                                   | n=4 standard quality (draft) and  |
|                                   | special characters created with   |
|                                   | Down Line Loading (DLL). Not      |
|                                   | supported on Ultimate-II Virtual  |
|                                   | Printer, same behavior as n=0.    |
|                                   |                                   |
|                                   | n=6 near letter quality (NLQ) and |
|                                   | special characters created with   |
|                                   | Down Line Loading (DLL). Not      |
|                                   | supported on Ultimate-II Virtual  |
|                                   | Printer, same behavior as n=2.    |
|                                   |                                   |
|                                   | 10 OPEN1,4                        |
|                                   |                                   |
|                                   | 20                                |
|                                   | PRINT#1,CHR$(27);CHR$(73);CHR$(n) |
|                                   | ;                                 |
|                                   |                                   |
|                                   | 30 CLOSE1                         |
|                                   |                                   |
|                                   | |image102|                        |
+-----------------------------------+-----------------------------------+

.. _other-commands-2:

Other commands
~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------+
| **BELL**                          | Make a short beep.                |
|                                   |                                   |
| **7**                             | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
| **07h**                           |                                   |
+===================================+===================================+
| **DC1**                           | Printer selection.                |
|                                   |                                   |
| **17**                            | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
| **11h**                           |                                   |
+-----------------------------------+-----------------------------------+
| **DC3**                           | No operation.                     |
|                                   |                                   |
| **19**                            |                                   |
|                                   |                                   |
| **13h**                           |                                   |
+-----------------------------------+-----------------------------------+
| **CAN**                           | **Cancel** the current job and    |
|                                   | clear printer buffer.             |
| **24**                            |                                   |
|                                   | This command is ignored by        |
| **18h**                           | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **ESC <**                         | Set **left to right** printing    |
|                                   | for one line.                     |
| **27 60**                         |                                   |
|                                   | This command is ignored by        |
| **1Bh 3Ch**                       | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **ESC @**                         | **Initialize** the printer. Set   |
|                                   | all parameters to default values. |
| **27 64**                         | Paper and head are not moved.     |
|                                   |                                   |
| **1Bh 40h**                       | This feature has been added in    |
|                                   | Ultimate-II Virtual Printer and   |
|                                   | does not exist in a real MPS-1230 |
|                                   | printer.                          |
+-----------------------------------+-----------------------------------+
| **ESC Q**                         | De-select printer.                |
|                                   |                                   |
| **27 81                           | This command is ignored by        |
| 1Bh 51h**                         | Ultimate-II Virtual Printer.      |
+-----------------------------------+-----------------------------------+
| **ESC U n**                       | Select **Mono/Bidirectional**     |
|                                   | printing.                         |
| **27 85 n                         |                                   |
| 1Bh 30h n**                       | This command is ignored by        |
|                                   | Ultimate-II Virtual Printer.      |
|                                   |                                   |
|                                   | | n=0 : bidirectional             |
|                                   | | n=1 : mono-directional (left to |
|                                   |   right) for better alignment.    |
+-----------------------------------+-----------------------------------+

PETASCII character table
========================

USA/UK
------

|image103|

Table : USA/UK Charset in Uppercase/Graphic Mode (Secondary address = 0)

|image104|

Table USA/UK Charset in Lowercase/Uppercase Mode (Secondary address = 7)

Denmark
-------

|image105|

Table : DENMARK Charset in Uppercase/Graphic Mode (Secondary address =
0)

|image106|

Table DENMARK Charset in Lowercase/Uppercase Mode (Secondary address =
7)

France / Italy
--------------

|image107|

Table : FRANCE/ITALY Charset in Uppercase/Graphic Mode (Secondary
address = 0)

|image108|

Table FRANCE/ITALY Charset in Lowercase/Uppercase Mode (Secondary
address = 7)

Germany
-------

|image109|

Table : GERMANY Charset in Uppercase/Graphic Mode (Secondary address =
0)

|image110|

Table GERMANY Charset in Lowercase/Uppercase Mode (Secondary address =
7)

Spain
-----

|image111|

Table : SPAIN Charset in Uppercase/Graphic Mode (Secondary address = 0)

|image112|

Table SPAIN Charset in Lowercase/Uppercase Mode (Secondary address = 7)

Sweden
------

|image113|

Table : SWEDEN Charset in Uppercase/Graphic Mode (Secondary address = 0)

|image114|

Table SWEDEN Charset in Lowercase/Uppercase Mode (Secondary address = 7)

Switzerland
-----------

|image115|

Table : SWITZERLAND Charset in Uppercase/Graphic Mode (Secondary address
= 0)

|image116|

Table SWITZERLAND Charset in Lowercase/Uppercase Mode (Secondary address
= 7)

EPSON FX-80 character table
===========================

Basic charset
-------------

|image117|

Extended charset
----------------

|image118|

International charsets changes
------------------------------

|image119|

IBM character tables
====================

Table 1
-------

|image120|

Table 2
-------

International 1
~~~~~~~~~~~~~~~

|image121|

International 2
~~~~~~~~~~~~~~~

|image122|

Israel
~~~~~~

|image123|

Greece
~~~~~~

|image124|

Portugal
~~~~~~~~

|image125|

.. _spain-1:

Spain
~~~~~

|image126|

Commodore commands reference
============================

+-------------+-------------+-------------+-------------+-------------+
| CODE        | DESCRIPTION | PAGE        |
+=============+=============+=============+=============+=============+
| ASCII       | DEC         | HEX         |             |             |
+-------------+-------------+-------------+-------------+-------------+
| BIT IMG     | 8           | 08          | Select      | 16          |
|             |             |             | graphic Bit |             |
|             |             |             | Image Mode  |             |
+-------------+-------------+-------------+-------------+-------------+
| BIM IMG SUB | 8 26        | 08 1A       | Select      | 16          |
|             |             |             | repeated    |             |
|             |             |             | graphic Bit |             |
|             |             |             | Image Mode  |             |
+-------------+-------------+-------------+-------------+-------------+
| HTAB        | 9           | 09          | Horizontal  | 15          |
|             |             |             | tabulation  |             |
+-------------+-------------+-------------+-------------+-------------+
| LF          | 10          | 0A          | Line Feed   | 14          |
+-------------+-------------+-------------+-------------+-------------+
| FF          | 12          | 0C          | Form Feed   | 14          |
+-------------+-------------+-------------+-------------+-------------+
| CR          | 13          | 0D          | Carriage    | 14          |
|             |             |             | Return      |             |
+-------------+-------------+-------------+-------------+-------------+
| EN ON       | 14          | 0E          | Double      | 10          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| EN OFF      | 15          | 0F          | Double      | 11          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | OFF, Bitmap |             |
|             |             |             | Image Mode  |             |
|             |             |             | OFF         |             |
+-------------+-------------+-------------+-------------+-------------+
| POS         | 16          | 10          | Jump to     | 15          |
|             |             |             | horizontal  |             |
|             |             |             | position in |             |
|             |             |             | number of   |             |
|             |             |             | characters  |             |
+-------------+-------------+-------------+-------------+-------------+
| CRSR DWN    | 17          | 11          | Select      | 13          |
|             |             |             | Commodore   |             |
|             |             |             | charset     |             |
|             |             |             | with        |             |
|             |             |             | lowercases  |             |
|             |             |             | and         |             |
|             |             |             | uppercases  |             |
+-------------+-------------+-------------+-------------+-------------+
| RVS ON      | 18          | 12          | Negative    | 11          |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 27          | 1B          | ASCII code  |             |
|             |             |             | for the     |             |
|             |             |             | Escape      |             |
|             |             |             | character   |             |
+-------------+-------------+-------------+-------------+-------------+
| NLQ ON      | 31          | 1F          | Near Letter | 13          |
|             |             |             | Quality ON  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC POS     | 16          | 10          | Jump to     | 15          |
|             |             |             | horizontal  |             |
|             |             |             | position in |             |
|             |             |             | number of   |             |
|             |             |             | dots        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC -       | 45          | 2D          | Underline   | 11          |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 4       | 52          | 34          | Italic ON   | 11          |
+-------------+-------------+-------------+-------------+-------------+
| ESC 5       | 53          | 35          | Italic OFF  | 12          |
+-------------+-------------+-------------+-------------+-------------+
| ESC 8 [4]_  | 56          | 38          | Disable     | 15          |
|             |             |             | paper end   |             |
|             |             |             | sensor      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 57          | 39          | Enable      | 15          |
| 9\ :sup:`†` |             |             | paper end   |             |
|             |             |             | sensor      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 61          | 3D          | Custom      | 17          |
| =\ :sup:`†` |             |             | character   |             |
|             |             |             | definition  |             |
|             |             |             | using Down  |             |
|             |             |             | Line        |             |
|             |             |             | Loading     |             |
|             |             |             | (DLL)       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC c       | 67          | 43          | Set paper   | 14          |
|             |             |             | height in   |             |
|             |             |             | number of   |             |
|             |             |             | text lines  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC c NUL   | 67 0        | 43 00       | Set paper   | 14          |
|             |             |             | height in   |             |
|             |             |             | inches      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC e       | 69          | 45          | Bold        | 11          |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC f       | 70          | 46          | Bold        | 11          |
|             |             |             | character   |             |
|             |             |             | OFF         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC g       | 71          | 47          | Double      | 10          |
|             |             |             | Strike ON   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC h       | 72          | 48          | Double      | 10          |
|             |             |             | Strike OFF  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC i       | 73          | 49          | Select      | 18          |
|             |             |             | character   |             |
|             |             |             | print       |             |
|             |             |             | definition  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 78          | 4E          | Define      | 14          |
| n\ :sup:`†` |             |             | Bottom of   |             |
|             |             |             | Page (BOF)  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 79          | 4F          | Disable     | 14          |
| o\ :sup:`†` |             |             | Bottom of   |             |
|             |             |             | Page (BOF)  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC s       | 83          | 53          | Select      | 12          |
|             |             |             | Superscript |             |
|             |             |             | or          |             |
|             |             |             | Subscript   |             |
|             |             |             | character   |             |
|             |             |             | mode        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC t       | 84          | 54          | Disable     | 13          |
|             |             |             | Superscript |             |
|             |             |             | and         |             |
|             |             |             | Subscript   |             |
|             |             |             | character   |             |
|             |             |             | mode        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC [       | 91          | 5B          | Select      | 12          |
|             |             |             | character   |             |
|             |             |             | spacing     |             |
|             |             |             | (PICA,      |             |
|             |             |             | ELITE, …)   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC X       | 120         | 78          | Select NLQ  | 13          |
|             |             |             | or DRAFT    |             |
+-------------+-------------+-------------+-------------+-------------+
| CS          | 141         | 8D          | Carriage    | 14          |
|             |             |             | Return with |             |
|             |             |             | no Line     |             |
|             |             |             | Feed        |             |
+-------------+-------------+-------------+-------------+-------------+
| CRSR UP     | 145         | 91          | Select      | 13          |
|             |             |             | Commodore   |             |
|             |             |             | charset     |             |
|             |             |             | with        |             |
|             |             |             | uppercases  |             |
|             |             |             | and         |             |
|             |             |             | graphics    |             |
+-------------+-------------+-------------+-------------+-------------+
| RVS OFF     | 146         | 92          | Negative    | 11          |
|             |             |             | character   |             |
|             |             |             | OFF         |             |
+-------------+-------------+-------------+-------------+-------------+
| NLQ OFF     | 159         | 9F          | Near Letter | 13          |
|             |             |             | Quality OFF |             |
+-------------+-------------+-------------+-------------+-------------+

EPSON FX-80 commands reference
==============================

+-------------+-------------+-------------+-------------+-------------+
| CODE        | DESCRIPTION | PAGE        |
+=============+=============+=============+=============+=============+
| ASCII       | DEC         | HEX         |             |             |
+-------------+-------------+-------------+-------------+-------------+
| BS          | 8           | 08          | Backspace   | 24          |
+-------------+-------------+-------------+-------------+-------------+
| TAB         | 9           | 09          | Horizontal  | 25          |
|             |             |             | tabulation  |             |
+-------------+-------------+-------------+-------------+-------------+
| LF          | 10          | 0A          | Line Feed   | 23          |
+-------------+-------------+-------------+-------------+-------------+
| VT          | 11          | 0B          | Vertical    | 25          |
|             |             |             | tabulation  |             |
+-------------+-------------+-------------+-------------+-------------+
| FF          | 12          | 0C          | Form Feed   | 23          |
+-------------+-------------+-------------+-------------+-------------+
| CR          | 13          | 0D          | Carriage    | 23          |
|             |             |             | Return      |             |
+-------------+-------------+-------------+-------------+-------------+
| SO          | 14          | 0E          | Double      | 19          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| SI          | 15          | 0F          | Condensed   | 20          |
|             |             |             | pitch 17.1  |             |
|             |             |             | cpi ON      |             |
+-------------+-------------+-------------+-------------+-------------+
| DC1 [7]_    | 17          | 11          | Printer     | 31          |
|             |             |             | select      |             |
+-------------+-------------+-------------+-------------+-------------+
| DC2         | 18          | 12          | Condensed   | 21          |
|             |             |             | pitch 17.1  |             |
|             |             |             | cpi OFF     |             |
+-------------+-------------+-------------+-------------+-------------+
| DC3\ :sup:` | 19          | 13          | Printer     | 31          |
| ‡`          |             |             | suspend     |             |
+-------------+-------------+-------------+-------------+-------------+
| DC4         | 20          | 14          | Double      | 19          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | OFF         |             |
+-------------+-------------+-------------+-------------+-------------+
| CAN\ :sup:` | 24          | 18          | Clean print | 31          |
| ‡`          |             |             | buffer      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 27          | 1B          | ASCII code  |             |
|             |             |             | for the     |             |
|             |             |             | Escape      |             |
|             |             |             | character   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC SO      | 14          | 0E          | Double      | 19          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC SI      | 15          | 0F          | Condensed   | 21          |
|             |             |             | pitch 17.1  |             |
|             |             |             | cpi ON      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC !       | 33          | 21          | Select      | 22          |
|             |             |             | graphics    |             |
|             |             |             | layout      |             |
|             |             |             | types       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 35          | 23          | Clear bit 7 | 31          |
| #\ :sup:`‡` |             |             | forcing     |             |
|             |             |             | (MSB)       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 37          | 25          | Select RAM  | 30          |
| %\ :sup:`‡` |             |             | (special    |             |
|             |             |             | chars) and  |             |
|             |             |             | ROM         |             |
|             |             |             | (standard   |             |
|             |             |             | chars)      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 38          | 26          | Define      | 30          |
| &\ :sup:`‡` |             |             | special     |             |
|             |             |             | characters  |             |
|             |             |             | in RAM      |             |
|             |             |             | (DLL)       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC -       | 45          | 2D          | Underline   | 20          |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC /       | 47          | 2F          | Vertical    | 26          |
|             |             |             | TAB stops   |             |
|             |             |             | program     |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 0       | 48          | 30          | Line        | 23          |
|             |             |             | spacing =   |             |
|             |             |             | 1/8"        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 1       | 49          | 31          | Line        | 23          |
|             |             |             | spacing =   |             |
|             |             |             | 7/72"       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 2       | 50          | 32          | Line        | 23          |
|             |             |             | spacing =   |             |
|             |             |             | 1/6"        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 3       | 51          | 33          | Line        | 23          |
|             |             |             | spacing =   |             |
|             |             |             | n/216"      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 4       | 52          | 34          | Italic ON   | 20          |
+-------------+-------------+-------------+-------------+-------------+
| ESC 5       | 53          | 35          | Italic OFF  | 20          |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 54          | 36          | Extend      | 30          |
| 6\ :sup:`‡` |             |             | printable   |             |
|             |             |             | character   |             |
|             |             |             | set         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 7       | 55          | 37          | Select      | 29          |
|             |             |             | basic       |             |
|             |             |             | national    |             |
|             |             |             | characters  |             |
|             |             |             | table       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 56          | 38          | Disable     | 25          |
| 8\ :sup:`‡` |             |             | paper end   |             |
|             |             |             | sensor      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 57          | 39          | Enable      | 25          |
| 9\ :sup:`‡` |             |             | paper end   |             |
|             |             |             | sensor      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 58          | 3A          | Copy        | 30          |
| ::sup:`‡`   |             |             | standard    |             |
|             |             |             | character   |             |
|             |             |             | generator   |             |
|             |             |             | (ROM) into  |             |
|             |             |             | RAM         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 60          | 3C          | Set left to | 31          |
| <:sup:`‡`   |             |             | right       |             |
|             |             |             | printing    |             |
|             |             |             | for one     |             |
|             |             |             | line        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 61          | 3D          | Force bit 7 | 31          |
| =\ :sup:`‡` |             |             | (MSB) to    |             |
|             |             |             | "0"         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 62          | 3E          | Force bit 7 | 31          |
| >\ :sup:`‡` |             |             | (MSB) to    |             |
|             |             |             | "1"         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC ?       | 63          | 3F          | Change BIM  | 28          |
|             |             |             | density     |             |
|             |             |             | selected by |             |
|             |             |             | graphics    |             |
|             |             |             | commands    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC @       | 64          | 40          | Initialize  | 31          |
|             |             |             | printer     |             |
|             |             |             | (main       |             |
|             |             |             | reset)      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC A       | 65          | 41          | Line        | 24          |
|             |             |             | spacing =   |             |
|             |             |             | n/72"       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC B       | 66          | 42          | Vertical    | 25          |
|             |             |             | TAB stops   |             |
|             |             |             | program     |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC C       | 67          | 43          | Set paper   | 24          |
|             |             |             | height in   |             |
|             |             |             | number of   |             |
|             |             |             | text lines  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC C NUL   | 67 0        | 43 00       | Set paper   | 24          |
|             |             |             | height in   |             |
|             |             |             | inches      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC D       | 68          | 44          | Horizontal  | 26          |
|             |             |             | TAB stops   |             |
|             |             |             | program     |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC E       | 69          | 45          | Bold        | 20          |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC F       | 70          | 46          | Bold        | 20          |
|             |             |             | character   |             |
|             |             |             | OFF         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC G       | 71          | 47          | Double      | 19          |
|             |             |             | Strike ON   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC H       | 72          | 48          | Double      | 19          |
|             |             |             | Strike OFF  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC I       | 73          | 49          | Extend      | 29          |
|             |             |             | printable   |             |
|             |             |             | characters  |             |
|             |             |             | set         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC J       | 74          | 4A          | Skip n/216" | 24          |
|             |             |             | of paper    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC K       | 75          | 4B          | Set normal  | 27          |
|             |             |             | density     |             |
|             |             |             | graphics    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC L       | 76          | 4C          | Set double  | 27          |
|             |             |             | density     |             |
|             |             |             | graphics    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC M       | 77          | 4D          | Elite pitch | 21          |
|             |             |             | 12 cpi ON   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC N [8]_  | 78          | 4E          | Define      | 25          |
|             |             |             | Bottom of   |             |
|             |             |             | Page (BOF)  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 79          | 4F          | Disable     | 25          |
| O\ :sup:`§` |             |             | Bottom of   |             |
|             |             |             | Page (BOF)  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC P       | 80          | 50          | Elite pitch | 21          |
|             |             |             | 12 cpi OFF  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC Q       | 81          | 51          | Define      | 24          |
|             |             |             | right       |             |
|             |             |             | margin      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC R       | 82          | 52          | Select      | 29          |
|             |             |             | national    |             |
|             |             |             | character   |             |
|             |             |             | set         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC S       | 83          | 53          | Select      | 21          |
|             |             |             | Superscript |             |
|             |             |             | or          |             |
|             |             |             | Subscript   |             |
|             |             |             | character   |             |
|             |             |             | mode        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC T       | 84          | 54          | Disable     | 21          |
|             |             |             | Superscript |             |
|             |             |             | and         |             |
|             |             |             | Subscript   |             |
|             |             |             | character   |             |
|             |             |             | mode        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 85          | 55          | Mono/Bidire | 31          |
| U\ :sup:`§` |             |             | ctional     |             |
|             |             |             | printing    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC W       | 87          | 57          | Double      | 19          |
|             |             |             | width       |             |
|             |             |             | characters  |             |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC Y       | 89          | 59          | Double      | 27          |
|             |             |             | density BIM |             |
|             |             |             | selection,  |             |
|             |             |             | normal      |             |
|             |             |             | speed       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC Z       | 90          | 5A          | Four times  | 28          |
|             |             |             | density BIM |             |
|             |             |             | selection   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC ^       | 94          | 5E          | 9-dot high  | 28          |
|             |             |             | strips BIM  |             |
|             |             |             | printing    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC b       | 98          | 62          | Select up   | 26          |
|             |             |             | to 8        |             |
|             |             |             | vertical    |             |
|             |             |             | tab stops   |             |
|             |             |             | programs    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 105         | 69          | Immediate   | 31          |
| i\ :sup:`§` |             |             | character   |             |
|             |             |             | printing    |             |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC j       | 106         | 6A          | Reverse     | 24          |
|             |             |             | paper feed  |             |
|             |             |             | n/216"      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC l       | 108         | 6C          | Define left | 24          |
|             |             |             | margin      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 112         | 70          | Proportiona | 22          |
| p\ :sup:`§` |             |             | l           |             |
|             |             |             | spacing     |             |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 115         | 73          | Half speed  | 31          |
| s\ :sup:`§` |             |             | printing    |             |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC x       | 120         | 78          | Select NLQ  | 21          |
|             |             |             | or DRAFT    |             |
+-------------+-------------+-------------+-------------+-------------+
| DEL\ :sup:` | 127         | 7F          | Clear last  | 31          |
| §`          |             |             | printable   |             |
|             |             |             | character   |             |
+-------------+-------------+-------------+-------------+-------------+

IBM Graphics Printer commands reference
=======================================

+-------------+-------------+-------------+-------------+-------------+
| CODE        | DESCRIPTION | PAGE        |
+=============+=============+=============+=============+=============+
| ASCII       | DEC         | HEX         |             |             |
+-------------+-------------+-------------+-------------+-------------+
| BELL [12]_  | 7           | 07          | Beep        | 39          |
+-------------+-------------+-------------+-------------+-------------+
| BS          | 8           | 08          | Backspace   | 36          |
+-------------+-------------+-------------+-------------+-------------+
| TAB         | 9           | 09          | Horizontal  | 37          |
|             |             |             | tabulation  |             |
+-------------+-------------+-------------+-------------+-------------+
| LF          | 10          | 0A          | Line Feed   | 35          |
+-------------+-------------+-------------+-------------+-------------+
| VT          | 11          | 0B          | Line Feed   | 37          |
+-------------+-------------+-------------+-------------+-------------+
| FF          | 12          | 0C          | Form Feed   | 35          |
+-------------+-------------+-------------+-------------+-------------+
| CR          | 13          | 0D          | Carriage    | 35          |
|             |             |             | Return      |             |
+-------------+-------------+-------------+-------------+-------------+
| SO          | 14          | 0E          | Double      | 32          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| SI          | 15          | 0F          | Condensed   | 33          |
|             |             |             | pitch 17.1  |             |
|             |             |             | cpi ON      |             |
+-------------+-------------+-------------+-------------+-------------+
| DC2         | 18          | 12          | Condensed   | 34          |
|             |             |             | pitch 17.1  |             |
|             |             |             | cpi OFF     |             |
+-------------+-------------+-------------+-------------+-------------+
| DC4         | 20          | 14          | Double      | 32          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | OFF         |             |
+-------------+-------------+-------------+-------------+-------------+
| CAN\ :sup:` | 24          | 18          | Clean print | 39          |
| \*\*`       |             |             | buffer      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 27          | 1B          | ASCII code  |             |
|             |             |             | for the     |             |
|             |             |             | Escape      |             |
|             |             |             | character   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC SO      | 14          | 0E          | Double      | 32          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC !       | 33          | 21          | Select      | 35          |
|  [13]_      |             |             | graphics    |             |
|             |             |             | layout      |             |
|             |             |             | types       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC -       | 45          | 2D          | Underline   | 33          |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 0       | 48          | 30          | Line        | 35          |
|             |             |             | spacing =   |             |
|             |             |             | 1/8"        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 1       | 49          | 31          | Line        | 35          |
|             |             |             | spacing =   |             |
|             |             |             | 7/72"       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 2       | 50          | 32          | Line        | 36          |
|             |             |             | spacing =   |             |
|             |             |             | 1/6"        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 3       | 51          | 33          | Line        | 36          |
|             |             |             | spacing =   |             |
|             |             |             | n/216"      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 52          | 34          | Italic ON   | 33          |
| 4\ :sup:`†† |             |             |             |             |
| `           |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 53          | 35          | Italic OFF  | 33          |
| 5\ :sup:`†† |             |             |             |             |
| `           |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 6       | 54          | 36          | IBM Table 2 | 38          |
|             |             |             | charset     |             |
|             |             |             | selection   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 7       | 55          | 37          | IBM Table 1 | 38          |
|             |             |             | charset     |             |
|             |             |             | selection   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 56          | 38          | Disable     | 37          |
| 8\ :sup:`\* |             |             | paper end   |             |
| \*`         |             |             | sensor      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 57          | 39          | Enable      | 37          |
| 9\ :sup:`\* |             |             | paper end   |             |
| \*`         |             |             | sensor      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 60          | 3C          | Set left to | 39          |
| <:sup:`\*\* |             |             | right       |             |
| `           |             |             | printing    |             |
|             |             |             | for one     |             |
|             |             |             | line        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 61          | 3D          | Down Line   | 38          |
| =\ :sup:`\* |             |             | Loading of  |             |
| \*`         |             |             | user        |             |
|             |             |             | characters  |             |
|             |             |             | (DLL)       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 64          | 40          | Initialize  | 39          |
| @\ :sup:`†† |             |             | printer     |             |
| `           |             |             | (main       |             |
|             |             |             | reset)      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC A       | 65          | 41          | Line        | 36          |
|             |             |             | spacing =   |             |
|             |             |             | n/72"       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC C       | 67          | 43          | Set paper   | 36          |
|             |             |             | height in   |             |
|             |             |             | number of   |             |
|             |             |             | text lines  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC C NUL   | 67 0        | 43 00       | Set paper   | 36          |
|             |             |             | height in   |             |
|             |             |             | inches      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC D       | 68          | 44          | Horizontal  | 37          |
|             |             |             | TAB stops   |             |
|             |             |             | program     |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC E       | 69          | 45          | Bold        | 33          |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC F       | 70          | 46          | Bold        | 33          |
|             |             |             | character   |             |
|             |             |             | OFF         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC G       | 71          | 47          | Double      | 32          |
|             |             |             | Strike ON   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC H       | 72          | 48          | Double      | 32          |
|             |             |             | Strike OFF  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC I       | 73          | 49          | Select      | 39          |
|             |             |             | print       |             |
|             |             |             | definition  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC J       | 74          | 4A          | Skip n/216" | 36          |
|             |             |             | of paper    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC K       | 75          | 4B          | Set normal  | 38          |
|             |             |             | density     |             |
|             |             |             | graphics    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC L       | 76          | 4C          | Set double  | 38          |
|             |             |             | density     |             |
|             |             |             | graphics    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC M       | 77          | 4D          | Elite pitch | 34          |
|             |             |             | 12 cpi ON   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC N       | 78          | 4E          | Define      | 36          |
|             |             |             | Bottom of   |             |
|             |             |             | Page (BOF)  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC O       | 79          | 4F          | Disable     | 37          |
|             |             |             | Bottom of   |             |
|             |             |             | Page (BOF)  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC S       | 83          | 53          | Select      | 34          |
|             |             |             | Superscript |             |
|             |             |             | or          |             |
|             |             |             | Subscript   |             |
|             |             |             | character   |             |
|             |             |             | mode        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC T       | 84          | 54          | Disable     | 35          |
|             |             |             | Superscript |             |
|             |             |             | and         |             |
|             |             |             | Subscript   |             |
|             |             |             | character   |             |
|             |             |             | mode        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC U [14]_ | 85          | 55          | Mono/Bidire | 39          |
|             |             |             | ctional     |             |
|             |             |             | printing    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC W       | 87          | 57          | Double      | 32          |
|             |             |             | width       |             |
|             |             |             | characters  |             |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC Y       | 89          | 59          | Double      | 38          |
|             |             |             | density BIM |             |
|             |             |             | selection,  |             |
|             |             |             | normal      |             |
|             |             |             | speed       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC Z       | 90          | 5A          | Four times  | 38          |
|             |             |             | density BIM |             |
|             |             |             | selection   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC [       | 91          | 5B          | Set         | 34          |
|             |             |             | horizontal  |             |
|             |             |             | spacing     |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC x       | 120         | 78          | Select NLQ  | 35          |
|             |             |             | or DRAFT    |             |
+-------------+-------------+-------------+-------------+-------------+

IBM Proprinter commands reference
=================================

+-------------+-------------+-------------+-------------+-------------+
| CODE        | DESCRIPTION | PAGE        |
+=============+=============+=============+=============+=============+
| ASCII       | DEC         | HEX         |             |             |
+-------------+-------------+-------------+-------------+-------------+
| BELL [18]_  | 7           | 07          | Beep        | 47          |
+-------------+-------------+-------------+-------------+-------------+
| BS          | 8           | 08          | Backspace   | 44          |
+-------------+-------------+-------------+-------------+-------------+
| TAB         | 9           | 09          | Horizontal  | 44          |
|             |             |             | tabulation  |             |
+-------------+-------------+-------------+-------------+-------------+
| LF          | 10          | 0A          | Line Feed   | 42          |
+-------------+-------------+-------------+-------------+-------------+
| VT          | 11          | 0B          | Vertical    | 45          |
|             |             |             | tabulation  |             |
+-------------+-------------+-------------+-------------+-------------+
| FF          | 12          | 0C          | Form Feed   | 42          |
+-------------+-------------+-------------+-------------+-------------+
| CR          | 13          | 0D          | Carriage    | 42          |
|             |             |             | Return      |             |
+-------------+-------------+-------------+-------------+-------------+
| SO          | 14          | 0E          | Double      | 40          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| SI          | 15          | 0F          | Condensed   | 41          |
|             |             |             | pitch 17.1  |             |
|             |             |             | cpi         |             |
+-------------+-------------+-------------+-------------+-------------+
| DC1\ :sup:` | 17          | 11          | Printer     | 47          |
| §§`         |             |             | selection   |             |
+-------------+-------------+-------------+-------------+-------------+
| DC2         | 18          | 12          | Pica pitch  | 41          |
|             |             |             | 10 cpi      |             |
+-------------+-------------+-------------+-------------+-------------+
| DC3         | 19          | 13          | No          | 47          |
|             |             |             | operation   |             |
+-------------+-------------+-------------+-------------+-------------+
| DC4         | 20          | 14          | Double      | 40          |
|             |             |             | width       |             |
|             |             |             | character   |             |
|             |             |             | OFF         |             |
+-------------+-------------+-------------+-------------+-------------+
| CAN\ :sup:` | 24          | 18          | Clean print | 47          |
| †`          |             |             | buffer      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 27          | 1B          | ASCII code  |             |
|             |             |             | for the     |             |
|             |             |             | Escape      |             |
|             |             |             | character   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC -       | 45          | 2D          | Underline   | 41          |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 0       | 48          | 30          | Line        | 43          |
|             |             |             | spacing =   |             |
|             |             |             | 1/8"        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 1       | 49          | 31          | Line        | 43          |
|             |             |             | spacing =   |             |
|             |             |             | 7/72"       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 2       | 50          | 32          | Line        | 43          |
|             |             |             | spacing =   |             |
|             |             |             | 1/6" or     |             |
|             |             |             | **ESC A**   |             |
|             |             |             | command     |             |
|             |             |             | execution   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 3       | 51          | 33          | Line        | 43          |
|             |             |             | spacing =   |             |
|             |             |             | n/216"      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 4       | 52          | 34          | Set Top Of  | 44          |
|             |             |             | Form (TOF)  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 5       | 53          | 35          | Automatic   | 43          |
|             |             |             | LF: ON/OFF  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 6       | 54          | 36          | IBM Table 2 | 46          |
|             |             |             | charset     |             |
|             |             |             | selection   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC 7       | 55          | 37          | IBM Table 1 | 46          |
|             |             |             | charset     |             |
|             |             |             | selection   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC :       | 58          | 3A          | Elite pitch | 41          |
|             |             |             | 12 cpi      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 61          | 3D          | Down Line   | 46          |
| =\ :sup:`†` |             |             | Loading of  |             |
|             |             |             | user        |             |
|             |             |             | characters  |             |
|             |             |             | (DLL)       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC @ [19]_ | 64          | 40          | Initialize  | 47          |
|             |             |             | printer     |             |
|             |             |             | (main       |             |
|             |             |             | reset)      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC A       | 65          | 41          | Line        | 43          |
|             |             |             | spacing =   |             |
|             |             |             | n/72"       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC B       | 66          | 42          | Vertical    | 45          |
|             |             |             | tab stops   |             |
|             |             |             | program     |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC C       | 67          | 43          | Set paper   | 44          |
|             |             |             | height in   |             |
|             |             |             | number of   |             |
|             |             |             | text lines  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC C NUL   | 67 0        | 43 00       | Set paper   | 44          |
|             |             |             | height in   |             |
|             |             |             | inches      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC D       | 68          | 44          | Horizontal  | 45          |
|             |             |             | TAB stops   |             |
|             |             |             | program     |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC E       | 69          | 45          | Bold        | 41          |
|             |             |             | character   |             |
|             |             |             | ON          |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC F       | 70          | 46          | Bold        | 41          |
|             |             |             | character   |             |
|             |             |             | OFF         |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC G       | 71          | 47          | Double      | 40          |
|             |             |             | Strike ON   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC H       | 72          | 48          | Double      | 40          |
|             |             |             | Strike OFF  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC I       | 73          | 49          | Select      | 47          |
|             |             |             | print       |             |
|             |             |             | definition  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC J       | 74          | 4A          | Skip n/216" | 43          |
|             |             |             | of paper    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC K       | 75          | 4B          | Set normal  | 45          |
|             |             |             | density     |             |
|             |             |             | graphics    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC L       | 76          | 4C          | Set double  | 45          |
|             |             |             | density     |             |
|             |             |             | graphics    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC N       | 78          | 4E          | Define      | 44          |
|             |             |             | Bottom of   |             |
|             |             |             | Page (BOF)  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC O       | 79          | 4F          | Disable     | 44          |
|             |             |             | Bottom of   |             |
|             |             |             | Page (BOF)  |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC         | 81          | 51          | De-select   | 47          |
| Q\ :sup:`§§ |             |             | printer     |             |
| `           |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC R       | 82          | 52          | Clear tab   | 45          |
|             |             |             | stops       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC S       | 83          | 53          | Select      | 42          |
|             |             |             | Superscript |             |
|             |             |             | or          |             |
|             |             |             | Subscript   |             |
|             |             |             | character   |             |
|             |             |             | mode        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC T       | 84          | 54          | Disable     | 42          |
|             |             |             | Superscript |             |
|             |             |             | and         |             |
|             |             |             | Subscript   |             |
|             |             |             | character   |             |
|             |             |             | mode        |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC U [20]_ | 85          | 55          | Mono/Bidire | 47          |
|             |             |             | ctional     |             |
|             |             |             | printing    |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC W       | 87          | 57          | Double      | 40          |
|             |             |             | width       |             |
|             |             |             | characters  |             |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC Y       | 89          | 59          | Double      | 46          |
|             |             |             | density BIM |             |
|             |             |             | selection,  |             |
|             |             |             | normal      |             |
|             |             |             | speed       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC Z       | 90          | 5A          | Four times  | 46          |
|             |             |             | density BIM |             |
|             |             |             | selection   |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC \\      | 92          | 5C          | Print n     | 46          |
|             |             |             | characters  |             |
|             |             |             | from        |             |
|             |             |             | extended    |             |
|             |             |             | table       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC ^       | 94          | 5E          | Print one   | 46          |
|             |             |             | character   |             |
|             |             |             | from        |             |
|             |             |             | extended    |             |
|             |             |             | table       |             |
+-------------+-------------+-------------+-------------+-------------+
| ESC \_      | 95          | 5F          | Overline:   | 42          |
|             |             |             | ON/OFF      |             |
+-------------+-------------+-------------+-------------+-------------+

Technical Specifications
========================

| **Output Type** PNG file 2-bit depth (4 grey levels) with lossless
  compression using LodePNG written by Lode Vandevenne
  (http://lodev.org/lodepng/)
| typical file size range is 30kB - 140kB

**Page size** 1984 x 2580

**Printable area size** 1920 x 2160 (80 PICA characters and 60 lines at
1/6”)

**Horizontal Resolution** 240 dpi

**Vertical Resolution** 216 dpi

**Physical ratio** A4 (21cm x 29,7cm)

| **Character matrix** 8V x 11H in draft mode
| 16V x 12H in NLQ mode

| **Print pitches** Pica, 10 char/in, 80 char/line
| Elite, 12 char/in, 96 char/line
| Micro, 15 char/in, 120 char/line
| Condensed, 17.1 char/in, 137 char/line
| Pica Compressed, 20 char/in, 160 char/line
| Elite Compressed, 24 char/in, 192 char/line
| Micro Compressed, 30 char/in, 240 char/line

| **Printing styles** Boldface
| Double width
| Superscript
| Subscript
| Double strike
| Underlined
| Italic
| Reversed
| Overlined

Print Sample
============

With Printer Ink Density set to Medium. Emulation is Commodore MPS.

|image127|

Document Revisions
==================

+-----------------+-----------------+-----------------+-----------------+
| Revision        | Date            | Author          | Description     |
+=================+=================+=================+=================+
| 1.0.0           | May 27, 2016    | René Garcia     | Initial release |
+-----------------+-----------------+-----------------+-----------------+
| 1.0.1           | May 30, 2016    | René Garcia     | Corrected       |
|                 |                 |                 | capabilities    |
|                 |                 |                 | table and       |
|                 |                 |                 | options         |
|                 |                 |                 | BIT IMG SUB     |
|                 |                 |                 | corrected       |
|                 |                 |                 | Ink Density     |
|                 |                 |                 | samples         |
+-----------------+-----------------+-----------------+-----------------+
| 1.1             | February 18,    | René Garcia     | Rename MPS      |
|                 | 2018            |                 | Printer         |
|                 |                 |                 | Emulation to    |
|                 |                 |                 | Virtual Printer |
|                 |                 |                 |                 |
|                 |                 |                 | New feature:    |
|                 |                 |                 | ASCII output    |
|                 |                 |                 | format          |
+-----------------+-----------------+-----------------+-----------------+

.. [1]
   Only in Ultimate-II Virtual Printer, not available on a real MPS-1230
   printer

.. [2]
   Only in Ultimate-II Virtual Printer, not available on a real MPS-1230
   printer

.. [3]
   Ignored in the Ultimate-II Virtual Printer

.. [4]
   Ignored in the Ultimate-II Virtual Printer

.. [5]
   Ignored in the Ultimate-II Virtual Printer

.. [6]
   Ignored in the Ultimate-II Virtual Printer

.. [7]
   Ignored in the Ultimate-II Virtual Printer

.. [8]
   Ignored in the Ultimate-II Virtual Printer

.. [9]
   Ignored in the Ultimate-II Virtual Printer

.. [10]
   Only in the Ultimate-II Virtual Printer, not in a real MPS-1230

.. [11]
   Ignored in the Ultimate-II Virtual Printer

.. [12]
   Ignored in the Ultimate-II Virtual Printer

.. [13]
   Only in the Ultimate-II Virtual Printer, not in a real MPS-1230

.. [14]
   Ignored in the Ultimate-II Virtual Printer

.. [15]
   Ignored in the Ultimate-II Virtual Printer

.. [16]
   Only in the Ultimate-II Virtual Printer, not in a real MPS-1230

.. [17]
   Ignored in the Ultimate-II Virtual Printer

.. [18]
   Ignored in the Ultimate-II Virtual Printer

.. [19]
   Only in the Ultimate-II Virtual Printer, not in a real MPS-1230

.. [20]
   Ignored in the Ultimate-II Virtual Printer

.. |image0| image:: media/media/image1.tiff
   :height: 0.11312in
.. |image1| image:: media/media/image2.tiff
   :height: 0.1086in
.. |image2| image:: media/media/image3.tiff
   :height: 0.12217in
.. |image3| image:: media/media/image4.tiff
   :width: 0.52083in
   :height: 0.61111in
.. |image4| image:: media/media/image5.tiff
   :width: 1.04861in
   :height: 0.92361in
.. |image5| image:: media/media/image6.tiff
   :width: 1.17361in
   :height: 1.15972in
.. |image6| image:: media/media/image7.tiff
   :width: 1.73303in
   :height: 0.13122in
.. |image7| image:: media/media/image8.tiff
   :width: 1.70136in
   :height: 0.11765in
.. |image8| image:: media/media/image9.tiff
   :width: 1.71041in
   :height: 0.12217in
.. |image9| image:: media/media/image10.tiff
   :width: 1.71493in
   :height: 0.13122in
.. |image10| image:: media/media/image11.tiff
   :width: 1.71946in
   :height: 0.13122in
.. |image11| image:: media/media/image12.tiff
   :width: 1.72398in
   :height: 0.14027in
.. |image12| image:: media/media/image13.tiff
   :width: 0.76018in
   :height: 0.1267in
.. |image13| image:: media/media/image14.tiff
   :width: 0.76018in
   :height: 0.13575in
.. |image14| image:: media/media/image15.tiff
   :width: 0.76471in
   :height: 0.13122in
.. |image15| image:: media/media/image16.tiff
   :width: 0.78281in
   :height: 0.15385in
.. |image16| image:: media/media/image17.tiff
   :width: 0.79185in
   :height: 0.14027in
.. |image17| image:: media/media/image18.tiff
   :width: 0.80091in
   :height: 0.14932in
.. |image18| image:: media/media/image19.tiff
   :width: 1.35294in
   :height: 0.32127in
.. |image19| image:: media/media/image20.tiff
   :width: 1.47964in
   :height: 0.16742in
.. |image20| image:: media/media/image21.tiff
   :width: 2.68326in
   :height: 0.17647in
.. |image21| image:: media/media/image22.tiff
   :width: 0.8371in
   :height: 0.15837in
.. |image22| image:: media/media/image23.tiff
   :width: 1.0362in
   :height: 0.1629in
.. |image23| image:: media/media/image24.tiff
   :width: 0.47964in
   :height: 0.14027in
.. |image24| image:: media/media/image25.tiff
   :width: 0.65611in
   :height: 0.12217in
.. |image25| image:: media/media/image26.tiff
   :width: 3.63348in
   :height: 1.15837in
.. |image26| image:: media/media/image27.tiff
   :width: 1.89593in
   :height: 0.13575in
.. |image27| image:: media/media/image28.tiff
   :width: 1.66516in
   :height: 0.14027in
.. |image28| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image29| image:: media/media/image20.tiff
   :width: 1.47964in
   :height: 0.16742in
.. |image30| image:: media/media/image21.tiff
   :width: 2.68326in
   :height: 0.17647in
.. |image31| image:: media/media/image22.tiff
   :width: 0.8371in
   :height: 0.15837in
.. |image32| image:: media/media/image23.tiff
   :width: 1.0362in
   :height: 0.1629in
.. |image33| image:: media/media/image24.tiff
   :width: 0.47964in
   :height: 0.14027in
.. |image34| image:: media/media/image25.tiff
   :width: 0.65611in
   :height: 0.12217in
.. |image35| image:: media/media/image26.tiff
   :width: 3.63348in
   :height: 1.15837in
.. |image36| image:: media/media/image27.tiff
   :width: 1.89593in
   :height: 0.13575in
.. |image37| image:: media/media/image28.tiff
   :width: 1.66516in
   :height: 0.14027in
.. |image38| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image39| image:: media/media/image30.tiff
   :width: 0.38009in
   :height: 0.34389in
.. |image40| image:: media/media/image31.tiff
   :width: 2.14027in
   :height: 0.34389in
.. |image41| image:: media/media/image30.tiff
   :width: 0.38009in
   :height: 0.34389in
.. |image42| image:: media/media/image31.tiff
   :width: 2.14027in
   :height: 0.34389in
.. |image43| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image44| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image45| image:: media/media/image20.tiff
   :width: 1.47964in
   :height: 0.16742in
.. |image46| image:: media/media/image21.tiff
   :width: 2.68326in
   :height: 0.17647in
.. |image47| image:: media/media/image23.tiff
   :width: 1.0362in
   :height: 0.1629in
.. |image48| image:: media/media/image24.tiff
   :width: 0.47964in
   :height: 0.14027in
.. |image49| image:: media/media/image25.tiff
   :width: 0.65611in
   :height: 0.12217in
.. |image50| image:: media/media/image27.tiff
   :width: 1.89593in
   :height: 0.13575in
.. |image51| image:: media/media/image28.tiff
   :width: 1.66516in
   :height: 0.14027in
.. |image52| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image53| image:: media/media/image20.tiff
   :width: 1.47964in
   :height: 0.16742in
.. |image54| image:: media/media/image21.tiff
   :width: 2.68326in
   :height: 0.17647in
.. |image55| image:: media/media/image23.tiff
   :width: 1.0362in
   :height: 0.1629in
.. |image56| image:: media/media/image24.tiff
   :width: 0.47964in
   :height: 0.14027in
.. |image57| image:: media/media/image25.tiff
   :width: 0.65611in
   :height: 0.12217in
.. |image58| image:: media/media/image27.tiff
   :width: 1.89593in
   :height: 0.13575in
.. |image59| image:: media/media/image28.tiff
   :width: 1.66516in
   :height: 0.14027in
.. |image60| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image61| image:: media/media/image32.tiff
   :width: 1.20815in
   :height: 0.37557in
.. |image62| image:: media/media/image33.tiff
   :width: 0.63348in
   :height: 0.37557in
.. |image63| image:: media/media/image34.tiff
   :width: 0.35294in
   :height: 0.37557in
.. |image64| image:: media/media/image32.tiff
   :width: 1.20815in
   :height: 0.37557in
.. |image65| image:: media/media/image33.tiff
   :width: 0.63348in
   :height: 0.37557in
.. |image66| image:: media/media/image34.tiff
   :width: 0.35294in
   :height: 0.37557in
.. |image67| image:: media/media/image20.tiff
   :width: 1.47964in
   :height: 0.16742in
.. |image68| image:: media/media/image21.tiff
   :width: 2.68326in
   :height: 0.17647in
.. |image69| image:: media/media/image23.tiff
   :width: 1.0362in
   :height: 0.1629in
.. |image70| image:: media/media/image24.tiff
   :width: 0.47964in
   :height: 0.14027in
.. |image71| image:: media/media/image25.tiff
   :width: 0.65611in
   :height: 0.12217in
.. |image72| image:: media/media/image26.tiff
   :width: 3.63348in
   :height: 1.15837in
.. |image73| image:: media/media/image27.tiff
   :width: 1.89593in
   :height: 0.13575in
.. |image74| image:: media/media/image28.tiff
   :width: 1.66516in
   :height: 0.14027in
.. |image75| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image76| image:: media/media/image20.tiff
   :width: 1.47964in
   :height: 0.16742in
.. |image77| image:: media/media/image21.tiff
   :width: 2.68326in
   :height: 0.17647in
.. |image78| image:: media/media/image23.tiff
   :width: 1.0362in
   :height: 0.1629in
.. |image79| image:: media/media/image24.tiff
   :width: 0.47964in
   :height: 0.14027in
.. |image80| image:: media/media/image25.tiff
   :width: 0.65611in
   :height: 0.12217in
.. |image81| image:: media/media/image26.tiff
   :width: 3.63348in
   :height: 1.15837in
.. |image82| image:: media/media/image27.tiff
   :width: 1.89593in
   :height: 0.13575in
.. |image83| image:: media/media/image28.tiff
   :width: 1.66516in
   :height: 0.14027in
.. |image84| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image85| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image86| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image87| image:: media/media/image20.tiff
   :width: 1.47964in
   :height: 0.16742in
.. |image88| image:: media/media/image21.tiff
   :width: 2.68326in
   :height: 0.17647in
.. |image89| image:: media/media/image23.tiff
   :width: 1.0362in
   :height: 0.1629in
.. |image90| image:: media/media/image24.tiff
   :width: 0.47964in
   :height: 0.14027in
.. |image91| image:: media/media/image27.tiff
   :width: 1.89593in
   :height: 0.13575in
.. |image92| image:: media/media/image28.tiff
   :width: 1.66516in
   :height: 0.14027in
.. |image93| image:: media/media/image35.tiff
   :width: 0.9095in
   :height: 0.13575in
.. |image94| image:: media/media/image20.tiff
   :width: 1.47964in
   :height: 0.16742in
.. |image95| image:: media/media/image21.tiff
   :width: 2.68326in
   :height: 0.17647in
.. |image96| image:: media/media/image23.tiff
   :width: 1.0362in
   :height: 0.1629in
.. |image97| image:: media/media/image24.tiff
   :width: 0.47964in
   :height: 0.14027in
.. |image98| image:: media/media/image27.tiff
   :width: 1.89593in
   :height: 0.13575in
.. |image99| image:: media/media/image28.tiff
   :width: 1.66516in
   :height: 0.14027in
.. |image100| image:: media/media/image35.tiff
   :width: 0.9095in
   :height: 0.13575in
.. |image101| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image102| image:: media/media/image29.tiff
   :width: 2.11765in
   :height: 0.32127in
.. |image103| image:: media/media/image36.tiff
   :width: 3.95023in
   :height: 3.10407in
.. |image104| image:: media/media/image37.tiff
   :width: 3.97285in
   :height: 3.11312in
.. |image105| image:: media/media/image38.tiff
   :width: 3.9095in
   :height: 3.04072in
.. |image106| image:: media/media/image39.tiff
   :width: 3.93213in
   :height: 3.06335in
.. |image107| image:: media/media/image40.tiff
   :width: 3.90045in
   :height: 3.04072in
.. |image108| image:: media/media/image41.tiff
   :width: 3.89593in
   :height: 3.04072in
.. |image109| image:: media/media/image42.tiff
   :width: 3.95023in
   :height: 3.03167in
.. |image110| image:: media/media/image43.tiff
   :width: 3.90498in
   :height: 3.08145in
.. |image111| image:: media/media/image44.tiff
   :width: 3.9276in
   :height: 3.05882in
.. |image112| image:: media/media/image45.tiff
   :width: 3.95023in
   :height: 3.06335in
.. |image113| image:: media/media/image46.tiff
   :width: 3.91855in
   :height: 3.04072in
.. |image114| image:: media/media/image47.tiff
   :width: 3.94118in
   :height: 3.0362in
.. |image115| image:: media/media/image48.tiff
   :width: 3.91855in
   :height: 3.04525in
.. |image116| image:: media/media/image49.tiff
   :width: 3.91403in
   :height: 3.07692in
.. |image117| image:: media/media/image50.tiff
   :width: 3.88235in
   :height: 3.01358in
.. |image118| image:: media/media/image51.tiff
   :width: 3.88688in
   :height: 3.00453in
.. |image119| image:: media/media/image52.tiff
   :width: 5.17717in
   :height: 1.91732in
.. |image120| image:: media/media/image53.tiff
   :width: 3.49213in
   :height: 2.72441in
.. |image121| image:: media/media/image54.tiff
   :width: 3.47638in
   :height: 2.68898in
.. |image122| image:: media/media/image55.tiff
   :width: 3.46063in
   :height: 2.71654in
.. |image123| image:: media/media/image56.tiff
   :width: 3.47638in
   :height: 2.70866in
.. |image124| image:: media/media/image57.tiff
   :width: 3.49213in
   :height: 2.70472in
.. |image125| image:: media/media/image58.tiff
   :width: 3.47638in
   :height: 2.69685in
.. |image126| image:: media/media/image59.tiff
   :width: 3.47638in
   :height: 2.72047in
.. |image127| image:: media/media/image60.tiff
   :width: 6.69375in
   :height: 7.925in
