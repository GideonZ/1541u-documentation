Cartridge Emulation
-------------------

Since firmware version 3.10, the way cartidges are emulated in the Ultimate has changed. While previously there were built-in cartridges, all cart roms are now optional. These previously built-in cartridges were stored in a flash chip on the board. These ROMs were taking up a lot of space; especially because nobody used all built-in cartridges much of that space was wasted. These built-in ROMs have been removed and the freed space was reassigned to the *flash drive*. The *flash drive* is now a permanent entry in the root of the file system and therefore always accessible. As a consequence, you can now use this space for your own cartridge of your liking, or one that is patched for your own needs. This chapter describes how to run and install your own cartridge roms, and how to switch between them.

Cartridge File Format
=====================
The file format that is used by the Ultimate is the standardized '.crt' format. This file format is defined and maintained by the VICE team. ".crt"-files do not only contain the raw ROM data, but also some meta data which is required to know how the ROM data needs to be interpreted. One of the important fields in this meta data is the "Hardware Type" field, which describes what type of cartridge it is. There is a long list of hardware types. Note that not all of them have been implemented in the Ultimate hardware.

Running a Cartridge ROM
=======================
At times, you may want to simply run a cartridge ROM temporarily, e.g. when you want to play a game. In this case, the cartridge can be started by simply navigating to the .CRT file and select "Run Cartridge" from the context menu. The cartridge will be loaded and 'attached' to the C64, and the machine is reset to start the cartridge. Resetting the machine will restart the cartridge again, just like what would happen with a real cartridge. To disable the cartridge, press the Task Menu key (F5), and select "C64 Machine" and then "Reboot". A reboot will install the permanently selected cartridge, if any, and reset the machine.

Installing a Cartridge ROM
==========================
For utility cartridges that need to start when the machine is turned on, the CRT file should be loaded at boot. This can be done by placing the CRT file onto the *flash drive*, in the **/flash/carts** directory. Note that this directory is hard coded and cannot be changed. There are two ways to get your CRT file in that directory:

1) Browse to the .crt file on your USB stick, and open the context menu by pressing RETURN. Then select 'Copy to Flash'. This will copy the ROM file to **/flash/carts** *and* automatically set the filename in the configuration. When the filename is too long, it will be truncated (prior to copying) to fit in the configuration field.

.. image:: ../media/config/copy_crt.png

2) Copy the .crt file on your USB stick manually to **/flash/carts**, by selecting it (press SPACE), then CTRL-C, navigate to **/flash/carts**, and then paste it there using CTRL-V. Then, go to the configuration menu (F2), go to *C64 and Cartridge Settings*, and use the drop-down context menu on the line 'Cartridge'. It will show you the files with the .crt extension that are currently in the **/flash/carts** directory.

.. image:: ../media/config/crt_selection.png

*Note that the size of the internal flash is very limited. On the 1541U2, the usable space is about 700 KiB, on the U2+ the size is roughly 1500 KiB, and on the U64 the usable size of the internal flash is about 3500 KiB. This may limit the use of the flash to utility cartridges, roms and some small configuration data, and maybe a disk image that you may use often.*

Supported Cartridge Types
=========================

Type# Description             1541U2 U2+ U64
===== ===========             ====== === ===
  0   Normal Cartridge           ⬤   ⬤  ⬤
  1   Action Replay              ⬤   ⬤  ⬤
===== ===========             ====== === ===  

    {  0, 0xFF, CART_NORMAL,    "Normal cartridge" },
    {  1, 0xFF, CART_ACTION,    "Action Replay" }, // max 4 banks of 8K
    {  2, 0xFF, CART_KCS,       "KCS Power Cartridge" },
    {  3, 0xFF, CART_FINAL3,    "Final Cartridge III" }, // max 16 banks (FC3+)
    {  4, 0xFF, CART_SBASIC,    "Simons Basic" },
    {  5, 0xFF, CART_OCEAN_8K,  "Ocean type 1" }, // max 64 banks of 8K, with the exception of the 16K carts, which are limited to 16 banks of 16K
    {  6, 0xFF, CART_NOT_IMPL,  "Expert Cartridge" },
    {  7, 0xFF, CART_NOT_IMPL,  "Fun Play" },
    {  8, 0xFF, CART_SUPERGAMES,"Super Games" },
    {  9, 0xFF, CART_NORDIC,    "Atomic Power" }, // max 8 banks of 8K
    { 10, 0xFF, CART_EPYX,      "Epyx Fastload" },
    { 11, 0xFF, CART_WESTERMANN,"Westermann" },
    { 12, 0xFF, CART_NOT_IMPL,  "Rex" },
    { 13, 0xFF, CART_FINAL12,   "Final Cartridge I" },
    { 14, 0xFF, CART_NOT_IMPL,  "Magic Formel" },
    { 15, 0xFF, CART_SYSTEM3,   "C64 Game System" },
    { 16, 0xFF, CART_NOT_IMPL,  "Warpspeed" },
    { 17, 0xFF, CART_NOT_IMPL,  "Dinamic" },
    { 18, 0xFF, CART_ZAXXON,    "Zaxxon" },
    { 19, 0xFF, CART_DOMARK,    "Magic Desk, Domark, HES Australia" }, // max 16 banks of 16K
    { 20, 0xFF, CART_SUPERSNAP, "Super Snapshot 5" },
    { 21, 0xFF, CART_COMAL80,   "COMAL 80" },
    { 32, 0xFF, CART_EASYFLASH, "EasyFlash" }, // max 64 banks
    { 33, 0xFF, CART_NOT_IMPL,  "EasyFlash X-Bank" },
    { 34, 0xFF, CART_NOT_IMPL,  "Capture" },
    { 35, 0xFF, CART_NOT_IMPL,  "Action Replay 3" },
    { 36, 0xFF, CART_RETRO,     "Retro Replay" }, // max 8 banks of 8K
    { 37, 0xFF, CART_NOT_IMPL,  "MMC64" },
    { 38, 0xFF, CART_NOT_IMPL,  "MMC Replay" },
    { 39, 0xFF, CART_NOT_IMPL,  "IDE64" },
    { 40, 0xFF, CART_NOT_IMPL,  "Super Snapshot V4" },
    { 41, 0xFF, CART_NOT_IMPL,  "IEEE 488" },
    { 42, 0xFF, CART_NOT_IMPL,  "Game Killer" },
    { 43, 0xFF, CART_NOT_IMPL,  "Prophet 64" },
    { 44, 0xFF, CART_EXOS,      "EXOS" }, // Currently max 1 bank
    { 45, 0xFF, CART_NOT_IMPL,  "Freeze Frame" },
    { 46, 0xFF, CART_NOT_IMPL,  "Freeze Machine" },
    { 47, 0xFF, CART_NOT_IMPL,  "Snapshot64" },
    { 48, 0xFF, CART_NOT_IMPL,  "Super Explode V5" },
    { 49, 0xFF, CART_NOT_IMPL,  "Magic Voice" },
    { 50, 0xFF, CART_NOT_IMPL,  "Action Replay 2" },
    { 51, 0xFF, CART_NOT_IMPL,  "MACH 5" },
    { 52, 0xFF, CART_NOT_IMPL,  "Diashow Maker" },
    { 53, 0xFF, CART_PAGEFOX,   "Pagefox" },
    { 54, 0xFF, CART_BBASIC,    "Kingsoft Business Basic" },
    { 55, 0xFF, CART_NOT_IMPL,  "Silver Rock 128" },
    { 56, 0xFF, CART_NOT_IMPL,  "Formel 64" },
    { 57, 0xFF, CART_NOT_IMPL,  "RGCD" },
    { 58, 0xFF, CART_NOT_IMPL,  "RR-Net MK3" },
    { 59, 0xFF, CART_NOT_IMPL,  "Easy Calc" },
    { 60, 0xFF, CART_GMOD2,     "GMod2" },
    { 61, 0xFF, CART_NOT_IMPL,  "MAX Basic" },
    { 62, 0xFF, CART_NOT_IMPL,  "GMod3" },
    { 63, 0xFF, CART_NOT_IMPL,  "ZIPP-CODE 48" },
    { 64, 0xFF, CART_BLACKBOX8, "Blackbox V8" },
    { 65, 0xFF, CART_BLACKBOX3, "Blackbox V3" },
    { 66, 0xFF, CART_BLACKBOX4, "Blackbox V4" },
    { 67, 0xFF, CART_NOT_IMPL,  "REX RAM-Floppy" },
    { 68, 0xFF, CART_NOT_IMPL,  "BIS-Plus" },
    { 69, 0xFF, CART_NOT_IMPL,  "SD-BOX" },
    { 70, 0xFF, CART_NOT_IMPL,  "MultiMAX" },
    { 71, 0xFF, CART_NOT_IMPL,  "Blackbox V9" },
    { 72, 0xFF, CART_NOT_IMPL,  "Lt. Kernal Host Adaptor" },
    { 73, 0xFF, CART_NOT_IMPL,  "RAMLink" },
    { 74, 0xFF, CART_NOT_IMPL,  "H.E.R.O." },
    { 0xFFFF, 0xFF, CART_NOT_IMPL, "" } };



Hardware Sub-Types
==================
In one of the latest refinements of the .CRT file format, a field has been defined that specifies the "sub type" of a cartridge. The Ultimate uses this field in some cases to know whether the ROM has been made compatible with other I/O functions, such as the RAM Expansion Unit. The following table shows these cases. For other cartridge types, this field has no effect.

