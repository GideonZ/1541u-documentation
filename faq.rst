
FAQ for the Ultimate II and Ultimate II Plus cartridges
=======================================================

The **Ultimate** cartridge is a storage solution for your Commodore 64 home
computer and will give you an excellent experience using this great machine.
Some people even enjoy using the Ultimate cartridge with their Commodore 128
computer.

.. contents:: **CONTENTS**
   :depth: 2

Information and resources for the Ultimate devices
--------------------------------------------------

Please read `Gideon's story <https://ultimate64.com/AboutUs>`_ about the
Ultimate products. Read the `specifications of the original Ultimate-II Plus cartridges
<http://www.1541ultimate.net/content/index.php?option=com_content&view=article&i
d=42&Itemid=20>`_. Read the `announcement of the Ultimate-64 device
<https://web.archive.org/web/20180121022242/http://www.1541ultimate.net/content/index.php?option=com_content&view=article&id=74&catid=9&Itemid=127>`_ and the `update
<https://web.archive.org/web/20180107211536/http://www.1541ultimate.net/content/index.php?option=com_content&view=article&id=75&Itemid=127>`_. Also read the Ultimate-64 `project status <https://ultimate64.com/ProjectStatus>`_.

You can buy Gideon's products in his `web
shop <https://ultimate64.com/Main_products>`_. You can also buy
`accessories <https://ultimate64.com/Accessories>`_.

Make sure you have the latest firmware installed
------------------------------------------------
Pleaes make sure you have the latest firmware installed. This F.A.Q. only covers subjects relating
to the latest firmware.


Where can I find the latest firmware?
-------------------------------------
You can find an overview the firmware releases for the Ultimate products
on this page: `firmware overview <https://ultimate64.com/Firmware>`_.\
If for any reason the ultimate64.com website is down, you can also `download the firmware
<https://github.com/GideonZ/ultimate_releases>`_ on `github <https://github.com>`_.


I am still running firmware 2.6k or lower on my 1541U-II/U2. How can I upgrade?
-------------------------------------------------------------------------------
Upgrading from 2.6k to 3.x is a bit different from what you're used to. You
will first need to upgrade to version 1541U-II Update 3.0 beta 7 using the
update.bin in the root of your microSD card.

Once you've done this, you can download latest firmware and run the file that
ends with .u2u to upgrade.

To revert to version 2.6k, use the revert.u2u that's included in the 3.0 beta 7
archive.

You can find the `3.0 beta 7 firmware <https://github.com/GideonZ/ultimate_releases/raw/master/1541u2_3.0beta7.zip>`_ on 
`GitHub <https://github.com/GideonZ/ultimate_releases>`__.

How can I use the emulated SID as second SID for 2SID tunes?
------------------------------------------------------------
**The question:** `link to facebook
<https://www.facebook.com/groups/1541ultimate/permalink/101556178971577
53/?comment_id=10155617970787753&comment_tracking=%7B%22tn%22%3A%22R3%22%7D>`_
posting.

I'm looking for information on how to use the emulated SID of the U2+ together
with a real one to play 2SID files, but so far haven't found enough to make it
happen. I've fiddled with the settings and read the Sidplayer instructions but
all I get is one (the C64 mainboard) Sid. Anyone know where I should look?

1. Find out what address the second SID is using for the 2SID you'd like to
   listen to. The ultimate sid player that's included shows the second sid
   address since firmware 3.2.
2. Go to the Ultimate menu and press F2 (shift + F1) to enter the configuration
   menu.
3. Select 'Audio Output settings'
4. Enable SID Left
5. Change the address at SID Left Base to the address you saw in the ultimate
   sid player. Probably something like $D420 or so
6. Go to 'SID Left Combined Waveforms' and choose the model the 2SID tune was
   composed for. Most likely 8580 since there are not many 6581 2SIDs.
7. Go to the Left Channel Output and Right Channel Output and select for both
   'Left SID'.
8. Make sure to plug a mini-jack in the line-out mini-jack port and connect it
   to your powered/active speakers or an amplifier.
9. Run the 2SID file and have a listen ;-)

Btw, the address of the SID chip inside your c64 is $D400.


Does the U2 and U2+ support Easyflash Cartridge images?
-------------------------------------------------------
Yes, both carts support EF. Since firmware 3.2 there is also support for saving
to the EF cartridge image:

Technology Preview: EAPI Support for Easyflash, incl. but not limited to
writing support. Please note that the changed crt file is NOT saved
automatically. You can save it by "F5", "Save Easyflash crt" in the file browser. 
The file will be saved with the filelname "module.crt". Optionally rename the 
saved file to a more recognizable name.

Tip: turn off Ultimate Audio in the C64 and cartridge settings when using this feature.


Which USB2LAN adapters are supported by the 1541Ultimate 2?
-----------------------------------------------------------
Any USB2LAN adapter that uses an AX88772/-A/-B chip should work.


Can I control the Ultimate using a USB keyboard?
------------------------------------------------
Yes you can!

You can connect a USB keyboard to the Ultimate cart and use that to control the
Ultimate instead of using the buttons. Use the **scroll lock** key to enter the
Ultimate menu and **ESC** will bring you back to the basic screen. You can use
the keyboard to navigate the Ultimate menu, just like when you're using the
remote interface via telnet, or using the C64 keyboard.


Can I play SID files from the High Voltage Sid Collection?
----------------------------------------------------------
Yes, the **Ultimate** comes with a built-in SID Player called **The Ultimate C64 SID Player**.


How do I use the built-in SID The Ultimate C64 SID Player
---------------------------------------------------------
As of firmware 3.2 The Ultimate C64 SID Player has keyboard support.\

Use the following keys:

============ ===========
key          description
============ ===========
|left arrow| fast forward
1 - 0        sub tune selection for tune 1 - 10
\+           play next sub tune
\ –          play previous sub tune
run/stop     go back to Ultimate menu
space bar    pause / resume tune
============ ===========

Keyboard support only works for PSID tunes and for RSID tunes that don't run in
a loop and when there is enough memory for the player. If the keyboard doesn't
work for a particular tune, then press the cartridge button (default middle
button) to go to the Ultimate menu for selecting another SID or sub tune.


Can I play SID tunes using the network interface?
-------------------------------------------------
There are several ways to play SID tunes using the ethernet interface:

* Use the remote interface using telnet;
* Use the `Acid 64 Player Pro <https://acid64.com/>`_ SID player by Wilfred Bos.

This SID player has the ability to play SID tunes over the netwerk on one or more
Ultimate devices. It is built to run on the Microsoft Windows Operating System.
When using `Wine <https://www.winehq.org/>`_, Acid 64 Player Pro will also run on macOS and Linux. This for version 4.0 and higher it is unknown if it runs using Wine.

* Use `Ultimate1541 Sid Remote 1.1 <https://csdb.dk/release/?id=157085>`_ by
  `L.A. Style of Genesis Project <http://csdb.dk/scener/?id=673>`_. This
  software runs on Microsoft Windows Operating system.


How do I use T64 files?
-----------------------
T64 is a file format, or rather a container, just like the D64 disk image.
Unfortunately the U2 and U2+ do not recognise it as such. This means that you
cannot open this container using the return key and then choose enter.

Use the right cursor key to enter the T64 container and then press return
for the contextual menu to pop up and then choose run to run the c64 programme.


How do I create a create a directory
------------------------------------
To create a directory on the file system browse to the location you would like
to create a directory. Press F5 and choose the 'Create Directory' from the
contextual menu.


How do I create a formatted disk image
--------------------------------------
To create a formatted d64 or g64 disk image on the file system browse to the
location you would like to create a directory. Press F5 and choose the 'Create
D64' or 'Create G64' from the contextual menu. 


What does insert blank disk do?
-------------------------------
Inserting a blank disk in either drive A or B will insert a blank and unformatted
disk image in the drive. This means you need to format the disk before you can use it.
Please take note that the disk does not exist on the filesytem (yet). If you saved
files on the disk, then make sure you save the disk before turning off the computer.


How do I copy files using the Ultimate file browser?
----------------------------------------------------
**The Ultinate device allows you to:**

* copy files and directories accross the filesystem;
* copy files and directories accross the microSD card and USB thumb drives.
* copy files from the filesystem to disk images
* copy files form the disk images to the filesystem

**Use these keys for copy operations:**

* use space bar to select the file(s) / dir(s) you'd like to copy
* use cbm + c to copy
* use cbm + v to paste.


How do I rename files and directories on the file system?
---------------------------------------------------------
To rename either a file or a directory simply select the file or directory and
press enter. A contextual menu will pop-up, select 'rename' to rename the file.


Where are the manuals for the Ultimate II and Ultimate II + carts?
------------------------------------------------------------------
This FAQ is part of the current manual.

For both the `Ultimate II
<https://github.com/GideonZ/1541ultimate/blob/master/doc/Quick%20guide%20to%2
0the%201541%20Ultimate%20II.docx>`_ and :doc:`Ultimate II+ <quick_guide>` a
quick start guide exists.

Another resource for some (old) documentation can be found here:
`http://rr.c64.org/wiki/1541_Ultimate#Documentation
<http://rr.c64.org/wiki/1541_Ultimate#Documentation>`_


Where are the manuals for the included emulated cartridge images?
-----------------------------------------------------------------
You will need to google for that. `Archive.org <https://archive.org>`_ seems to
have scans of several c64 cartridges.

The wiki `rr.c64.org <http://rr.c64.org/wiki/Main_Page>`_ is also a great place
to find manuals.


Flip/swap disk (mount the next disk without using the Ultimate menu)
--------------------------------------------------------------------
Since firmware 3.0e there is this nice feature called:
"seamless disk swap by pressing middle button at least 1 sec"

This allows you to mount the next disk when a game or a demo asks for it
without entering the Ultimate menu.

It only works on disk images for which it is obviously that those disk images
belong together E.g. "special game disk 1.d64" and "special game disk 2.d64" or
"special game A.d64" and "special games B.d64" or "special game S1.d64" and
"special game S2.d64". or "image 1.d64" and "image 2.d64", etc. etc. etc. It
even recognises roman numbers.


How about the C128 and C128D(CR). Does the Ultimate cartridge work on these machines?
-------------------------------------------------------------------------------------
Yes, the Ultimate cartridges work on the C128, C128D(CR) but with some 
limitations. Bart was so kind to write down his findings and advice on how to 
get the most out of your C128 combined with the U2+:
`https://www.bartsplace.net/content/publications/1541ultimate128.shtml 
<https://www.bartsplace.net/content/publications/1541ultimate128.shtml>`_


Disabling the internal C128D drive
----------------------------------
source: `1541ultimate.net
forum <http://www.1541ultimate.net/content/index.php?option=com_kunena&view=topi
c&catid=11&id=14255&Itemid=147#16653>`_

Most of the games and demos will only run from device #8. Even if you added a device
number 8/9-Switch to your internal C128 drive, some games and demos do not like
if there is a 2nd drive on the bus.

So, the good news:
With `S.T.F.U. <https://csdb.dk/release/?id=160842>`_ you can disable your
internal drive by software:
`https://csdb.dk/release/?id=160842 <https://csdb.dk/release/?id=160842>`_)

1. Set your 1541-U drive emulation to device #9 or OFF
2. Start and run the file. (In my case I had to load it from disk - it does not
   seem to work if you DMA-start it from your 1541-U).
3. Select and deactivate your internal 1571.
4. Set your Drive A of your 1541-U to device #8 and use it as regular drive.

This did work on my C128D. It did not work on my SX64. However it might be of
interest for C128D users.


.. |left arrow| unicode:: U+2B05 U+FE0E .. LEFTWARDS BLACK ARROW

