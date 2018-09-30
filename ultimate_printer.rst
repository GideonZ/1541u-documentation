Ultimate-II Virtual Printer
___________________________

By René Garcia
Version: February 18\ :sup:`th` 2018
All rights reserved.

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

+-------------+--------------------+-------------+-------------+-------------+
|             | Commodore          | Epson FX-80 | IBM         | IBM         |
|             | MPS                |             | Graphics    | Proprinter  |
|             |                    |             | Printer     |             |
+=============+====================+=============+=============+=============+
| Draft       | •                  | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| Double      | •                  | •           | •           | •           |
| strike      |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| Bold        | •                  | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| Italic      | •                  | •           | •           |             |
| (draft      |                    |             |             |             |
| only)       |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| NLQ         | •                  | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| Underline   | •                  | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| Double      | •                  | •           | •           | •           |
| width       |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| Superscript | •                  | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| Subscript   | •                  | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| Reverse     | •                  |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| Overline    |                    |             |             | •           |
+-------------+--------------------+-------------+-------------+-------------+
| Backspace   |                    | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| Reverse     |                    | •           |             |             |
| page feed   |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| CR=CR+LF    | •                  |             |             | *optional*  |
+-------------+--------------------+-------------+-------------+-------------+
| LF=CR+LF    | •                  | •           |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| 7 dot BIM   | •                  |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| 8 dot BIM   |                    | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| 9 dot BIM   |                    | •           |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| HT Program  |                    | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| VT Program  |                    | •           |             | •           |
+-------------+--------------------+-------------+-------------+-------------+
| 60 dpi BIM  | • *(double width)* | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| 75 dpi BIM  |                    | •           |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| 80 dpi BIM  |                    | •           |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| 90 dpi BIM  |                    | •           |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| 120 dpi BIM |                    | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| 240 dpi BIM |                    | •           | •           | •           |
+-------------+--------------------+-------------+-------------+-------------+
| Pica        | •                  | •           | •           | •           |
| (10cpi)     |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| Elite       | •                  | •           | •           | •           |
| (12cpi)     |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| Micro       | •                  |             |             |             |
| (15cpi)     |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| Condensed   | •                  | •           | •           | •           |
| (17.1cpi)   |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| Pica        | •                  |             |             |             |
| Compressed  |                    |             |             |             |
| (20cpi)     |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| Elite       | •                  |             |             |             |
| Compressed  |                    |             |             |             |
| (24 cpi)    |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+
| Micro       | •                  |             |             |             |
| Compressed  |                    |             |             |             |
| (30 cpi)    |                    |             |             |             |
+-------------+--------------------+-------------+-------------+-------------+

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

For a detailed description of all commands, please refer to the PDF version of this document.


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


.. |image0| image:: media/printer/image1.png
   :height: 0.11312in
.. |image1| image:: media/printer/image2.png
   :height: 0.1086in
.. |image2| image:: media/printer/image3.png
   :height: 0.12217in
.. |image3| image:: media/printer/image4.png
   :width: 0.52083in
   :height: 0.61111in
.. |image4| image:: media/printer/image5.png
   :width: 1.04861in
   :height: 0.92361in
.. |image5| image:: media/printer/image6.png
   :width: 1.17361in
   :height: 1.15972in
.. |image6| image:: media/printer/image7.png
   :width: 1.73303in
   :height: 0.13122in
.. |image7| image:: media/printer/image8.png
   :width: 1.70136in
   :height: 0.11765in
.. |image8| image:: media/printer/image9.png
   :width: 1.71041in
   :height: 0.12217in
.. |image9| image:: media/printer/image10.png
   :width: 1.71493in
   :height: 0.13122in
.. |image10| image:: media/printer/image11.png
   :width: 1.71946in
   :height: 0.13122in
.. |image11| image:: media/printer/image12.png
   :width: 1.72398in
   :height: 0.14027in
.. |image12| image:: media/printer/image13.png
   :width: 0.76018in
   :height: 0.1267in
.. |image13| image:: media/printer/image14.png
   :width: 0.76018in
   :height: 0.13575in
.. |image14| image:: media/printer/image15.png
   :width: 0.76471in
   :height: 0.13122in
.. |image15| image:: media/printer/image16.png
   :width: 0.78281in
   :height: 0.15385in
.. |image16| image:: media/printer/image17.png
   :width: 0.79185in
   :height: 0.14027in
.. |image17| image:: media/printer/image18.png
   :width: 0.80091in
   :height: 0.14932in
.. |image18| image:: media/printer/image19.png
   :width: 1.35294in
   :height: 0.32127in
.. |image19| image:: media/printer/image20.png
   :width: 1.47964in
   :height: 0.16742in
.. |image20| image:: media/printer/image21.png
   :width: 2.68326in
   :height: 0.17647in
.. |image21| image:: media/printer/image22.png
   :width: 0.8371in
   :height: 0.15837in
.. |image22| image:: media/printer/image23.png
   :width: 1.0362in
   :height: 0.1629in
.. |image23| image:: media/printer/image24.png
   :width: 0.47964in
   :height: 0.14027in
.. |image24| image:: media/printer/image25.png
   :width: 0.65611in
   :height: 0.12217in
.. |image25| image:: media/printer/image26.png
   :width: 3.63348in
   :height: 1.15837in
.. |image26| image:: media/printer/image27.png
   :width: 1.89593in
   :height: 0.13575in
.. |image27| image:: media/printer/image28.png
   :width: 1.66516in
   :height: 0.14027in
.. |image28| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image29| image:: media/printer/image20.png
   :width: 1.47964in
   :height: 0.16742in
.. |image30| image:: media/printer/image21.png
   :width: 2.68326in
   :height: 0.17647in
.. |image31| image:: media/printer/image22.png
   :width: 0.8371in
   :height: 0.15837in
.. |image32| image:: media/printer/image23.png
   :width: 1.0362in
   :height: 0.1629in
.. |image33| image:: media/printer/image24.png
   :width: 0.47964in
   :height: 0.14027in
.. |image34| image:: media/printer/image25.png
   :width: 0.65611in
   :height: 0.12217in
.. |image35| image:: media/printer/image26.png
   :width: 3.63348in
   :height: 1.15837in
.. |image36| image:: media/printer/image27.png
   :width: 1.89593in
   :height: 0.13575in
.. |image37| image:: media/printer/image28.png
   :width: 1.66516in
   :height: 0.14027in
.. |image38| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image39| image:: media/printer/image30.png
   :width: 0.38009in
   :height: 0.34389in
.. |image40| image:: media/printer/image31.png
   :width: 2.14027in
   :height: 0.34389in
.. |image41| image:: media/printer/image30.png
   :width: 0.38009in
   :height: 0.34389in
.. |image42| image:: media/printer/image31.png
   :width: 2.14027in
   :height: 0.34389in
.. |image43| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image44| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image45| image:: media/printer/image20.png
   :width: 1.47964in
   :height: 0.16742in
.. |image46| image:: media/printer/image21.png
   :width: 2.68326in
   :height: 0.17647in
.. |image47| image:: media/printer/image23.png
   :width: 1.0362in
   :height: 0.1629in
.. |image48| image:: media/printer/image24.png
   :width: 0.47964in
   :height: 0.14027in
.. |image49| image:: media/printer/image25.png
   :width: 0.65611in
   :height: 0.12217in
.. |image50| image:: media/printer/image27.png
   :width: 1.89593in
   :height: 0.13575in
.. |image51| image:: media/printer/image28.png
   :width: 1.66516in
   :height: 0.14027in
.. |image52| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image53| image:: media/printer/image20.png
   :width: 1.47964in
   :height: 0.16742in
.. |image54| image:: media/printer/image21.png
   :width: 2.68326in
   :height: 0.17647in
.. |image55| image:: media/printer/image23.png
   :width: 1.0362in
   :height: 0.1629in
.. |image56| image:: media/printer/image24.png
   :width: 0.47964in
   :height: 0.14027in
.. |image57| image:: media/printer/image25.png
   :width: 0.65611in
   :height: 0.12217in
.. |image58| image:: media/printer/image27.png
   :width: 1.89593in
   :height: 0.13575in
.. |image59| image:: media/printer/image28.png
   :width: 1.66516in
   :height: 0.14027in
.. |image60| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image61| image:: media/printer/image32.png
   :width: 1.20815in
   :height: 0.37557in
.. |image62| image:: media/printer/image33.png
   :width: 0.63348in
   :height: 0.37557in
.. |image63| image:: media/printer/image34.png
   :width: 0.35294in
   :height: 0.37557in
.. |image64| image:: media/printer/image32.png
   :width: 1.20815in
   :height: 0.37557in
.. |image65| image:: media/printer/image33.png
   :width: 0.63348in
   :height: 0.37557in
.. |image66| image:: media/printer/image34.png
   :width: 0.35294in
   :height: 0.37557in
.. |image67| image:: media/printer/image20.png
   :width: 1.47964in
   :height: 0.16742in
.. |image68| image:: media/printer/image21.png
   :width: 2.68326in
   :height: 0.17647in
.. |image69| image:: media/printer/image23.png
   :width: 1.0362in
   :height: 0.1629in
.. |image70| image:: media/printer/image24.png
   :width: 0.47964in
   :height: 0.14027in
.. |image71| image:: media/printer/image25.png
   :width: 0.65611in
   :height: 0.12217in
.. |image72| image:: media/printer/image26.png
   :width: 3.63348in
   :height: 1.15837in
.. |image73| image:: media/printer/image27.png
   :width: 1.89593in
   :height: 0.13575in
.. |image74| image:: media/printer/image28.png
   :width: 1.66516in
   :height: 0.14027in
.. |image75| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image76| image:: media/printer/image20.png
   :width: 1.47964in
   :height: 0.16742in
.. |image77| image:: media/printer/image21.png
   :width: 2.68326in
   :height: 0.17647in
.. |image78| image:: media/printer/image23.png
   :width: 1.0362in
   :height: 0.1629in
.. |image79| image:: media/printer/image24.png
   :width: 0.47964in
   :height: 0.14027in
.. |image80| image:: media/printer/image25.png
   :width: 0.65611in
   :height: 0.12217in
.. |image81| image:: media/printer/image26.png
   :width: 3.63348in
   :height: 1.15837in
.. |image82| image:: media/printer/image27.png
   :width: 1.89593in
   :height: 0.13575in
.. |image83| image:: media/printer/image28.png
   :width: 1.66516in
   :height: 0.14027in
.. |image84| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image85| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image86| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image87| image:: media/printer/image20.png
   :width: 1.47964in
   :height: 0.16742in
.. |image88| image:: media/printer/image21.png
   :width: 2.68326in
   :height: 0.17647in
.. |image89| image:: media/printer/image23.png
   :width: 1.0362in
   :height: 0.1629in
.. |image90| image:: media/printer/image24.png
   :width: 0.47964in
   :height: 0.14027in
.. |image91| image:: media/printer/image27.png
   :width: 1.89593in
   :height: 0.13575in
.. |image92| image:: media/printer/image28.png
   :width: 1.66516in
   :height: 0.14027in
.. |image93| image:: media/printer/image35.png
   :width: 0.9095in
   :height: 0.13575in
.. |image94| image:: media/printer/image20.png
   :width: 1.47964in
   :height: 0.16742in
.. |image95| image:: media/printer/image21.png
   :width: 2.68326in
   :height: 0.17647in
.. |image96| image:: media/printer/image23.png
   :width: 1.0362in
   :height: 0.1629in
.. |image97| image:: media/printer/image24.png
   :width: 0.47964in
   :height: 0.14027in
.. |image98| image:: media/printer/image27.png
   :width: 1.89593in
   :height: 0.13575in
.. |image99| image:: media/printer/image28.png
   :width: 1.66516in
   :height: 0.14027in
.. |image100| image:: media/printer/image35.png
   :width: 0.9095in
   :height: 0.13575in
.. |image101| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image102| image:: media/printer/image29.png
   :width: 2.11765in
   :height: 0.32127in
.. |image103| image:: media/printer/image36.png
   :width: 3.95023in
   :height: 3.10407in
.. |image104| image:: media/printer/image37.png
   :width: 3.97285in
   :height: 3.11312in
.. |image105| image:: media/printer/image38.png
   :width: 3.9095in
   :height: 3.04072in
.. |image106| image:: media/printer/image39.png
   :width: 3.93213in
   :height: 3.06335in
.. |image107| image:: media/printer/image40.png
   :width: 3.90045in
   :height: 3.04072in
.. |image108| image:: media/printer/image41.png
   :width: 3.89593in
   :height: 3.04072in
.. |image109| image:: media/printer/image42.png
   :width: 3.95023in
   :height: 3.03167in
.. |image110| image:: media/printer/image43.png
   :width: 3.90498in
   :height: 3.08145in
.. |image111| image:: media/printer/image44.png
   :width: 3.9276in
   :height: 3.05882in
.. |image112| image:: media/printer/image45.png
   :width: 3.95023in
   :height: 3.06335in
.. |image113| image:: media/printer/image46.png
   :width: 3.91855in
   :height: 3.04072in
.. |image114| image:: media/printer/image47.png
   :width: 3.94118in
   :height: 3.0362in
.. |image115| image:: media/printer/image48.png
   :width: 3.91855in
   :height: 3.04525in
.. |image116| image:: media/printer/image49.png
   :width: 3.91403in
   :height: 3.07692in
.. |image117| image:: media/printer/image50.png
   :width: 3.88235in
   :height: 3.01358in
.. |image118| image:: media/printer/image51.png
   :width: 3.88688in
   :height: 3.00453in
.. |image119| image:: media/printer/image52.png
   :width: 5.17717in
   :height: 1.91732in
.. |image120| image:: media/printer/image53.png
   :width: 3.49213in
   :height: 2.72441in
.. |image121| image:: media/printer/image54.png
   :width: 3.47638in
   :height: 2.68898in
.. |image122| image:: media/printer/image55.png
   :width: 3.46063in
   :height: 2.71654in
.. |image123| image:: media/printer/image56.png
   :width: 3.47638in
   :height: 2.70866in
.. |image124| image:: media/printer/image57.png
   :width: 3.49213in
   :height: 2.70472in
.. |image125| image:: media/printer/image58.png
   :width: 3.47638in
   :height: 2.69685in
.. |image126| image:: media/printer/image59.png
   :width: 3.47638in
   :height: 2.72047in
.. |image127| image:: media/printer/image60.png
   :width: 6.69375in
   :height: 7.925in
