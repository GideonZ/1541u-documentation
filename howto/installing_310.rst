Installing Firmware 3.10 / Core 1.41
------------------------------------

Instructions
============
Installing firmware 3.10 works in the same way as previous versions. You simply browse with the file browser in the Ultimate menu to the unzipped firmware file. The extension for 1541 Ultimate-II is ".u2u", for the Ultimate-II+ the extension is ".u2p", and for the U64 the extension is ".u64". Move to the appropriate file with the cursor keys and press RETURN to bring up the context menu. Select 'Run Update', and the updater program will be loaded and started. Note for 1541U2 users: *You need to have at least 3.x firmware to do this.*

It is important to know that the organization of the data in the Flash chip changes when installing 3.10. Even when the installer runs, previously stored data may be lost. This is especially the case if you have already used the "/flash" drive (e.g. on the U2+ with the factory installed version 3.9a). So once again, please assume that all user data will be lost. Backup this data if it is important to you. For those who have never seen the "/flash" directory in the file browser; this is a relatively new feature whereby the on board flash chip can be accessed as if it were a disk with files. From 3.10 and onward, non-volatile user data is stored as files on the "/flash" drive.

What is in the .zip package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

=========================== =============================== ==== ==== ==== === ======= ===== =========
Filename                    Purpose                         1541 1571 1581 SID Sampler GMod2 ACIA-6551
=========================== =============================== ==== ==== ==== === ======= ===== =========
update_1.41.u64             Firmware for Ultimate 64         ●●   ●●   ●●   ●     ●      ●       ●
update_3.10.u2p             Firmware for Ultimate-II+        ●●   ●●   ●●   ●     ●      ●       ●
update_3.10_audio.u2u       Firmware for 1541 Ultimate-II    ●    –    –    ●     ●      –       –
update_3.10_dual_drive.u2u  Firmware for 1541 Ultimate-II    ●●   –    –    –     –      –       ●
update_3.10_gmod2.u2u       Firmware for 1541 Ultimate-II    ●●   –    –    –     –      ●       –
uci_kernal_3.10.bin         Updated Hyperspeed Kernal 
changes.txt                 Change Summary since 3.9 / 1.37
=========================== =============================== ==== ==== ==== === ======= ===== =========

Below, as a reference, is a list of the most important changes since the previous official release 3.9. Documentation for the most prominent new features or changes in user interface can be found here:

* `Multi Mode Disk Drive <mm_drive.html>`_
* `Updated Cartridge System <cartridge.html>`_
* `Programmable U64 Palette <palette.html>`_


Changes since official release (3.9 / 1.37)
===========================================

Added features
~~~~~~~~~~~~~~
- Hardware emulation of 1571 and 1581 drives (U2+ / U64 only)
- MFM support on 1571, with enhanced G71 format to store MFM tracks 
- Added audio samples for insert / remove floppy disk
- Added second drive sound to speaker output
- Possiblity to use your own drive sound samples
- Custom U64 palettes
- SystemInfo Page, showing drive, cartridge and storage status (under F4 key)
- Flash Disk, to store drive roms, sounds, cartridges and such
- Cartridges are now always CRT files. Selected by filename in the config
- Cartridge compatibility check and reporting
- GMOD2 support, including EEPROM (U2+ / U64 only)
- Zaxxon Cartridge support
- Implemented writing CVT files back to a disk image (enables copying CVT files across disks.)

Various UI Improvements
~~~~~~~~~~~~~~~~~~~~~~~
- Select & Delete, using Shift-DEL
- Recursive delete from context menu
- Long filename truncation (thanks to 'naali' / Antti Svenn)
- Scrollable string edit box
- Adds save function for all cartridges, including EasyFlash and GMOD2
- Full Clear function of configuration in Flash
- Added 'F3' Help screen to config menu

Technical Fixes
~~~~~~~~~~~~~~~
- Fixed RGB mode (U64 only)
- Fixed block read command
- Fixed access of files with special chars in CBM disk images, accessed from IEC
- Fixed UCI issues with SidPlay and others
- Fixed colon issue in Ultimate Kernal ROM
- Fixed crash on invalid file chain CBM filesystems
- Fixed check order DIR / VOLUME; fixes some issues with exFAT directories
- Added M and V commands in modem emulation layer, V now supporting numeric responses. Thanks Scott Hutter
- Fixed the root cause of the VOLUME bit set in exFAT directories
- Fixed missing 'probe' for filesystems on multi-partition disks
- Fixed loading from wrong device ID when issuing the 'run disk' command
- Fixed many little bugs in the generation of CVT files (copying GEOS files from a disk image)
- Adopted changes to U64 Kernal to set default loading ID, as submitted by Leif Bloomquist
- Adopted USB modifier key handling, as submitted by Peter de Schrijver
- Corrected bug in extended partition table reading
- Relaxed C128 cartridge timing (for C128 carts)
- Extended UCI I/O bytes to support Hyperspeed Kernal properly
- Check for file copy onto itself
- Increased robustness against loading faulty disk images
- Fixed VIA latch mode in 1541/1571.
- [Issue 227] Fixes 'get sensible name' function for Ulticopy
- Fix for .d71 sector allocation - format should give 1328 blocks free, not 1347.
- Fixes possible crash when decoding a GCR track to binary
- [Issue 160]: SpeedDOS / DolphinDOS loading errors

