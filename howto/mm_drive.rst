Multi Mode Disk Drive
---------------------

Introduction
============

Since version 3.10 of the firmware, the Ultimate-II+ and Ultimate 64 have full hardware emulation support for 1541, 1571 *and* 1581. Previously, only the 1541 was implemented in the FPGA. Now, this drive has been replaced by a so called 'multi mode drive'. This multi-mode drive is an implementation that shares properties of the 1541, 1571 and 1581, which can be switched on or off on the fly. In practice this means that the hardware-emulated disk drive can be set to act like a 1541, a 1571 or 1581. This switching is fully managed by the application that runs on your Ultimate product. This chapter explains how to use it.

Manual Drive Type Selection
===========================

In the configuration menu (F2) you will find two drives, indicated by *Drive A Settings* and *Drive B Settings* respectively. Each drive can be of any of the aforementioned types; 1541, 1571 or 1581. To change the drive type, simply enter the configuration item by pressing CRSR-Right or RETURN. The second line of the configuration shows the selection:

.. image:: media/config/drive_type.png

Press enter and select the preferred drive type from the drop down list, or cycle through the options with the + and - keys. (Note that CRSR-Right does the same as +.) Once the configuration screen is closed -- either by pressing RUN-STOP to leave the configuration screen entirely, or the CRSR-Left key combination to go up one level --, the drive mode is switched. The appropriate ROM is read into the drive, the sound samples are loaded, and the drive is reset. When the settings are saved in flash memory, this drive type is selected on boot.

Automatic Drive Type Selection
==============================
When browsing through your disk images, you may want to mount a .d81 while the current drive type is 1541. The .d81 format describes a 800kB 3.5" disk, intended to store a disk image of a 1581 disk. As you may know, a 3.5" disk does not fit into the 1541, so the drive needs to be changed into a 1581. Fortunately, it is not necessary to go to the configuration screen first. When trying to mount this disk, the application asks you if you like to change the drive type to 1581. When 'Yes' is chosen, the drive type is changed; the new ROM and appropriate sound samples are loaded and the drive is reset. Then the disk image is mounted.

Note that this is a temporary change. There is *no* change to the configuration settings.

Selecting Drive ROMs
====================
When installing the 3.10 firmware, one ROM for each of the drives is installed as well. These binary files of either exactly 16K or exactly 32K in size are saved to the internal flash drive, in **/flash/roms**, named '1541.rom', '1571.rom' and '1581.rom' respectively. Installing other drive ROMs, like SpeedDos, DolphinDos or JiffyDos can be done in two ways:

1) Browse to the .bin or .rom file on your USB stick, and open the context menu by pressing RETURN. Then select 'Set as 15x1 ROM'. This will copy the ROM file to **/flash/roms** and automatically set the filename in the configuration of Drive A; the drive likely to be used most often.

.. image:: media/config/drive_rom_set_as.png

2) Copy the .bin or .rom file on your USB stick manually to **/flash/roms**, by selecting it (press SPACE), then CTRL-C, navigate to **/flash/roms**, and then paste it there using CTRL-V. Then, go to the configuration menu (F2), go to Drive A or Drive B Settings, and use the drop-down context menu on the line 'ROM for ...'. It will show you the files that are currently in the **/flash/roms** directory.

.. image:: media/config/drive_rom_selection.png

Other Settings
==============

Drive Bus ID
~~~~~~~~~~~~
With this option, the hardware bus ID can be set. Only the options 8, 9, 10 and 11 are available, because those are the ones that can be set in the hardware of these drives.

Extra RAM
~~~~~~~~~
Some ROMs require the drive to have more RAM. Standard, the 1541 and 1571 come with 2K SRAM memory; and the 1581 comes with 8K of RAM. This is not enough to store an entire raw track, which is required for some of the ROMs to speed up disk read/write performance. By enabling the 'Extra RAM' option, all locations that are not occupied by I/O devices and ROM will be available as RAM. Note that the I/O mirroring that the 1541 has will be eliminated as well; VIA chips will then *only* be visible from $1800-$1FFF, and no longer on $3800-$3FFF, $5800-$5FFF and $7800-$7FFF. Note that $8000-$FFFF is *always* ROM, in any of the drive types.

Disk Swap Delay
~~~~~~~~~~~~~~~
The 1541 and 1571 use the write protect light sensor to know whether the disk has been changed. For proper detection, these light pulses should be of suffient length. By default 100ms is enough, but you can change it here.

Resets when C64 resets
~~~~~~~~~~~~~~~~~~~~~~
A reset signal is passed through the IEC (serial) cable. On some machines, this reset signal is triggered only when the C64 is turned on, while on others it triggers whenever the C64 is reset, e.g. by a button on the userport or expansion port. With this option, it is possible to reset the internal drives when a reset of the C64 occurs, regardless of the RESET# signal on the serial cable. When this option is turned off; only the RESET# signal on the serial cable is observed.

Freezes in menu
~~~~~~~~~~~~~~~
The C64 as well as the floppy drives have their own CPU. The Ultimate application enforces a full stop of the C64 CPU while displaying the menu on the VIC. (On the U64 this is only the case when the 'Freeze' mode is selected in the 'User Interface Settings' configuration menu.)  More often than not, the C64 CPU and the drive CPU are synchronized to a certain extent. If the drive CPU would continue to run, while the C64 CPU is stopped, this could mean that the game or demo crashes. With this option, which is enabled by default, the drive CPU *also* stops when the C64 CPU is halted.

GCR Save Align Tracks
~~~~~~~~~~~~~~~~~~~~~
The 1541 and 1571 use Group Code Recording, or GCR to store data. This code provides enough flux transitions to reliabily detect the data, even despite small speed variations. This is the raw data format that the drive uses internally. Disk images can be stored in this format as well, called .g64 or .g71. This allows the representation of disk data that does not fully follow the default formatting rules.

Because commodore does not use the 'index pulse' a track can start at any angle on the disk. This would mean that when saving a track into a .g64 (or .g71) disk image, the data may start somewhere in the middle of a sector, while the beginning of that sector is stored at the end of the data track. Although perfectly valid, this makes decoding of a .g64 (or .g71) disk somewhat more complex. For this reason, the Ultimate can align these tracks when writing them into the disk image, which causes each track to properly start between sectors.

This option has no effect on the 1581, nor on .d64 and .d71 images.
