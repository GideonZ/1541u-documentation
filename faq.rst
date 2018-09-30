=======================================================
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
Ultimate products. Read the `specifications of the Ultimate-II Pluscartridges
<http://www.1541ultimate.net/content/index.php?option=com_content&view=article&i
d=42&Itemid=20>`_. Read the `announcement of the Ultimate-64 device
<http://www.1541ultimate.net/content/index.php?option=com_
content&view=article&id=74&Itemid=127>`_ and the `update
<http://www.1541ultimate.net/content/index.php?option=com
_content&view=article&id=75&Itemid=127>`_. Also read the Ultimate-64 `project
status <https://ultimate64.com/ProjectStatus>`_.

You can buy Gideon's products in his `web
shop <https://ultimate64.com/Main_products>`_. You can also buy
`accessories <https://ultimate64.com/Accessories>`_.


Where can I find the latest firmware?
-------------------------------------
You can find an overview of almost all firmware releases on this page: `firmware
overview
<https://ammo.home.xs4all.nl/Ultimate_Carts/firmware_ultimate_carts.html>`_ 
(including the latest).


I am still running firmware 2.6k or lower on my U2. How can I upgrade?
----------------------------------------------------------------------
Upgrading from 2.6k to 3.x is a bit different from what you're used to. You
will first need to upgrade to version 1541U-II Update 3.0 beta 7 using the
update.bin in the root of your microSD card.

Once you've done this, you can download latest firmware and run the file that
ends with .u2u to upgrade.

To revert to version 2.6k, use the revert.u2u that's included in the 3.0 beta 7
archive.

You can find the `3.0 beta 7 on 1541ultimate.net.
<http://www.1541ultimate.net/content/index.php?option=com_content&view=article&i
d=67:1541u-ii-update-30b7&catid=4&Itemid=19>`_ and the latest firmware is
available in the pinned post at the top of the 1541 Ultimate facebook group or
`on this page
<https://ammo.home.xs4all.nl/Ultimate_Carts/firmware_ultimate_carts.html>`_.


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
   composed for. Most likely 8580.
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
autmatically. You can save it by "F5", "Save Easyflash crt" in the filebrowser
(and optionally renaming the saved file).


Which USB2LAN adapters are supported by the 1541Utlimate 2?
-----------------------------------------------------------
Any USB2LAN adapter that uses an AX88772/-A/-B chip should work.


Can I control the Utlimate using a USB keyboard?
------------------------------------------------
Yes you can!

You can connect a USB keyboard to the Ultimate cart and use that to control the
Ultimate instead of using the buttons. Use the **scroll lock** key to enter the
Ultimate menu and **ESC** will bring you back to the basic screen. You can use
the keyboard to navigate the Ultimate menu, just like when you're using the
remote interface via telnet, or using the C64 keyboard.


Can I play SID files from the High Voltage Sid Collection?
----------------------------------------------------------
Yes, the **Ultimate** comes with a built-in SID Player called


How do I use the built-in SID player
------------------------------------
The new Sidplayer in firmware 3.2 has now keyboard support for the following
keys:

========  ===========
key       description
========  ===========
??        fast forward
1 - 0     sub tune selection for tune 1 - 10
\+        play next sub tune
\ -       play previous sub tune
run/stop  go to Ultimate menu
========  ===========

Keyboard support only works for PSID tunes and for RSID tunes that don't run in
a loop and when there is enough memory for the player. If the keyboard doesn't
work for a particular tune, then press the cartridge button (default middle
button) to go to the Ultimate menu for selecting another SID or sub tune.


Can I play SID tunes using the network interface?
-------------------------------------------------
There are several ways to play SID tunes using the ethernet interface:

* Use the remote interface using telnet;
* Use the `Acid 64 Player Pro <https://acid64.com/>`_ SID player by Wilfred Bos.

This SID player has the ability to play SID tunes over the netwerk on the
Ultimate devices. It is built to run on the Microsoft Windows Operating System.
When using `Wine <https://www.winehq.org/>`_, Acid 64 Player Pro will also run on macOS and Linux.

* Use `Ultimate1541 Sid Remote 1.1 <https://csdb.dk/release/?id=157085>`_ by
  `L.A. Style of Genesis Project <http://csdb.dk/scener/?id=673>`_. This
  software runs on Microsoft Windows Operating system.


How do I use T64 files?
-----------------------
T64 is a file format, or rather a container, just like D64 disk image.
Unfortunately the U2 and U2+ does not recognise it as such. This means that you
cannot open this container using the return key and then choose enter.

Instead, you can use the right cursor key to enter the T64 container and then
press return to have the contextual menu pop up and choose run to run the c64
programme.


How do I create a create a directory
------------------------------------
To create a directory on the file system browse to the location you would like
to create a directory. Press F5 and choose the 'Create Directory' from the
contextual menu.


How do I create a blank disk image
----------------------------------
To create a blank d64 or g64 disk image on the file system browse to the
location you would like to create a directory. Press F5 and choose the 'Create
D64' or 'Create G64' from the contextual menu.


How do I copy a disk image, directory or file to another location
-----------------------------------------------------------------
You can copy d64 disk images, directories and even files from inside a disk
image to the file system. Unfortunately you cannot (yet) copy a file from the
file system into a disk image. Also, if you copy a file from inside the disk
image to the file system, make sure to give it an appropriate extension. The U2
/ U2+ doest not (yet) do this by itself, unless you run `this unofficial
firmware
<https://github.com/markusC64/1541ultimate2/releases/tag/3.2a_180411%2B_v1>`_
by MarkusC64.

The keys to use are:

* use space bar to select the file(s) / dir(s) you'd like to copy
* use cbm + c to copy
* use cbm + v to paste.


Can I copy files from inside a disk image to the file system?
-------------------------------------------------------------
Yes, you can copy files from inside a disk image to the file system.

1.  Highlight the disk image;
2.  Press either return and then select 'enter' or use right arrow key to
    enter the disk image;
3.  Select one or more files you'd like to copy by pressing the space bar;
4.  Use cbm + c to copy the file(s);
5.  Leave the disk image by using the left cursor key;
6.  Go to the location you'd like to paste the file and use cbm + v to
    'paste' the file(s).

When using an old firmware, you will need to add the file extension yourself.
Just press return and choose 'rename' to do this.


Can I copy files from the file system to a disk image?
------------------------------------------------------
Unfortunately this is not possible. Perhaps in a distant future firmware
release this will be possible.


Can I copy files from a disk image to another disk image?
---------------------------------------------------------
Unfortunately this is not possible yet. If you try to copy a file either from
the file system or a disk image and paste it into another disk image, the
'paste' programme will crash and most likely you will need to reset or reboot
your C64.


How do I rename files and directories on the file system?
---------------------------------------------------------
To rename either a file or a directory simply select the file or directory and
press enter. A contextual menu will pop-up, select 'rename' to rename the file.


Where are the manuals for the Ultimate II and Ultimate II + carts?
------------------------------------------------------------------
Unfortunately there are no manuals in a sense that you can read about all
functions, settings etc. of the Ultimate cartridges.

For both the `Ultimate II
<https://github.com/GideonZ/1541ultimate/blob/master/doc/Quick%20guide%20to%2
0the%201541%20Ultimate%20II.docx>`_ and `Ultimate II+ <quick_guide.html>`_ a
quick start guide exists.

A resource for some documentation can be found here:
`http://rr.c64.org/wiki/1541_Ultimate#Documentation
<http://rr.c64.org/wiki/1541_Ultimate#Documentation>`_


Where are the manuals for the included emulated cartridge images?
-----------------------------------------------------------------
You will need to google for that. `Archive.org <https://archive.org>`_ seems to
have scans of several c64 cartridges.

The wiki `rr.c64.org <http://rr.c64.org/wiki/Main_Page>`_ is also a great place
to find some manuals.


Disabling the internal C128D drive
----------------------------------
source: `1541ultimate.net
forum <http://www.1541ultimate.net/content/index.php?option=com_kunena&view=topi
c&catid=11&id=14255&Itemid=147#16653>`_

Most of the games will only run from device #8. Even if you added a device
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


Flip/swap disk (mount the next disk without entering the Ultimate menu)
-----------------------------------------------------------------------
Since firmware 3.0e there is this nice feature implemented by Markus C64:
"seamless disk swap by pressing middle button at least 1 sec"

This allows you to mount the next disk when a game or a demo asks for it
without entering the Ultimate menu.

It only works on disk images for which it is obviously that those disk images
belong together E.g. "special game disk 1.d64" and "special game disk 2.d64" or
"special game A.d64" and "special games B.d64" or "special game S1.d64" and
"special game S2.d64". or "image 1.d64" and "image 2.d64", etc. etc. etc. It
even recognises roman numbers.

