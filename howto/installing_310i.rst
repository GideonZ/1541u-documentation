Installing Firmware 3.10i / Core 1.42
-------------------------------------

Instructions
============
Installing firmware 3.10i works in the same way as previous versions. You simply browse with the file browser in the Ultimate menu to the unzipped firmware file.
Move to the appropriate file with the cursor keys and press RETURN to bring up the context menu. Select 'Run Update', and the updater program will be loaded and started.

There are different files in the download package. Which one you need depends on your hardware, and for the 1541 Ultimate-II also on the intended use, as not all features
fit together in one firmware version.

It is important to note that the embedded processor of the 1541U2 will change from a Microblaze clone to my own implementation of RiscV. This means that older updaters
that were built for Microblaze will no longer run. And this means, that you cannot downgrade from 3.10i using these older ".u2u" files. To make sure you don't load
the wrong file, the filename extension that the firmware recognizes changes from ".u2u" to ".u2r". If you want to downgrade, you will first have to make sure your
unit runs on Microblaze. This can be done by loading the "revert_to_mb.u2r" firmware, which loads *an unsupported version of 3.10i*, based on Microblaze.
Using this unsupported version of the firmware, you can then load any ".u2u" file, including older versions. This is the *ONLY* reason that this unsupported version
is provided! See the table below:

1541 Ultimate-II Migration Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

================ =========== ================================ ==================== =====================
Current Firmware CPU Type    Upgrade Method                   Package / File       Updates to...
================ =========== ================================ ==================== =====================
Any 2.x          ZPU         'update.bin' on Root of SD Card  1541u2_3.0beta7.zip  Microblaze / 3.0beta7
Any 3.x          Microblaze  Select '.u2u' file from menu     1541u2_3.y.zip       Microblaze / 3.y
Any 3.x          Microblaze  Select '.u2u' file from menu     ultimate_3.10i.zip   RiscV / 3.10i
3.10i and up     RiscV       Select '.u2r' file from menu     update_yyy.u2r       RiscV / yyy
3.10i and up     RiscV       Select '.u2r' file from menu     revert_to_mb.u2r     Microblaze / 3.10i(*)
================ =========== ================================ ==================== =====================

*) Version only supplied to allow loading older firmware versions.

What is in the .zip package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

===================== =============================== ============ ==== ==== ==== === ======= ===== =========
Filename              Purpose                         Variant      1541 1571 1581 SID Sampler GMod2 ACIA-6551
===================== =============================== ============ ==== ==== ==== === ======= ===== =========
update_1.42.u64       Firmware for Ultimate 64                     ●●   ●●   ●●   ●     ●      ●       ●
update_3.10i.u2p      Firmware for Ultimate-II+                    ●●   ●●   ●●   ●     ●      ●       ●
update_3.10i.u2l      Firmware for Ultimate-II+L                   ●●   ●●   ●●   ●     ●      ●       ●
update_3.10i.u2u (*)  Firmware for 1541 Ultimate-II   Audio        ●    –    –    ●     ●      –       –
update_3.10i.u2u (*)  Firmware for 1541 Ultimate-II   Dual Drive   ●●   –    –    –     –      ●       ●
revert_to_mb.u2r (*)  Downgrade package to Microblaze Audio        ●    –    –    ●     ●      –       – 
revert_to_mb.u2r (*)  Downgrade package to Microblaze Modem        ●●   –    –    –     –      –       ●
revert_to_mb.u2r (*)  Downgrade package to Microblaze Gmod2        ●●   –    –    –     –      ●       –
uci_kernal_3.10.bin   Hyperspeed Kernal
changes.txt           Change Summary since 3.10
===================== =============================== ============ ==== ==== ==== === ======= ===== =========

*) Inside of the installer, you can choose which variant of the FPGA will be loaded

Changes in 3.10i, compared to 3.10
==================================

Background
~~~~~~~~~~

If you would take some time to check the commit history of the repository
at GitHub, you may find over 500 commits since the last released version, 3.10a.
This is a lotttt more than it usually takes to release a next firmware version.
The version is still 3.10, so there are not many functional changes. Yet, files
have been touched, updated, or just made compatible with the new Ultimate-II+L
hardware. It was more difficult than expected to get the Lattice FPGA to work
correctly and keep compatibility with the existing hardware platforms.

On top of the new introduction of the Ultimate-II+L, there is still a need to
support the "good old" 1541 Ultimate-II (or simply: U2). There have always
been issues with the Microblaze processor and the compiler from Xilinx. Every
version of the Xilinx compiler had different bugs that caused the Microblaze
based firmware to be broken in one way or another. Since the U2+L runs well
on the Risc-V, it was decided to upgrade the CPU inside of the U2 and ditch
the Microblaze forever. Unfortunately, the CPU that was chosen to run inside
of the U2+L did not fit in the same space as the Microblaze clone, so I
decided to write my own Risc-V compatible CPU. This is the CPU that will be
used from now on in the 1541 Ultimate-II.

General Fixes
~~~~~~~~~~~~~
- [Important] Fixed ExFAT filesystems with 128kB clusters (Fixes failing D64 mounts from some ExFAT thumbdrives)
- [Facebook Discussion] EasyFlash save function now saves all chip chunks to support incomplete CRT files
- [Issue-271] GEORAM at boot (MarkusC64)
- [Issue-279] Support for 2 MHz operation for any cartridge, including EasyFlash
- [Issue-246] Fixed: Virtual Printer crashes when file cannot be created.
- [Issue-234] Deleting last item in directory makes selection invisible
- [Issue-236] Confirmation modal asking a question only gives 'OK' instead of 'Yes/No'.
- [Issue-R17] Added mapping of ESC key to RUN/STOP.
- [Facebook Request] Added: Leave menu on mount (can be selected per drive)
- [Facebook Bug Report]: Fixed starting Kingsoft Business Basic cartridge
- [Facebook Bug Report]: Allow Maverick (and others?) to write wrong sector headers on MFM tracks.
- [Facebook Bug Report]: Unable to select GeoRAM. Is now a mode of the RAM Expansion Unit.
- [Facebook Bug Report]: Fixed color palette not loaded at boot (U64 only).
- [Facebook Bug Report]: Fixed USB sticks not recognized
- [Messenger Report]: Improvements to palette file read. Rejects faulty files. Fixes hang-up
- [Messenger Report]: Fixes 'Create DNP' when run from Telnet. Turned out to be a stack overflow.
- [Email Discussion]: Adds EEPROM segment to GMOD2 when it is missing in the CRT file

U64 core fixes
~~~~~~~~~~~~~~
- Multicolor graphics side border bug (core version V1.41 => V1.42)

Modem fixes
~~~~~~~~~~~
- ACIA NMI pulse extension to extend over bad line. This allows the 6502 to see it always.
- Performance optimization ACIA / Modem
- Allow spaces after ATDT command.
- Minor fixes in the modem emulation layer from Scott Hutter (xlar54)

Cartridge Support
~~~~~~~~~~~~~~~~~
- [Issue-314] Added support for Blackbox V9.
- Additional C128 cartridge variant that allows banking and offers some RAM (U2/U2+/U2+L only).

Additions
~~~~~~~~~
- Firmware target added: Ultimate-II+L; the Lattice version!
- System Information page (F4) now shows elaborate version info.
- GEOS support functions from MarkusC64
