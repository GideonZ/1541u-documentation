
Supported file types
--------------------

The Ultimate application supports the following file types:

.. list-table:: Title
 :header-rows: 1

 * - Extension
   - Use
 * - .prg
   - C64 program files. These can be loaded directly into the memory of the C64 through DMA and started at will. It does not matter whether these PRG files are located on the filesystem directly, or within a .D64, .T64 or another container format.
 * - .d64 / .d71 / .d81
   - Disk images. .D64 files are for the 1541 and can be mounted onto the virtual floppy drives. .d71 and .d81 formats only function as containers and cannot be mounted, since there is no support for 1571 / 1581 emulation yet. 
 * - .g64
   - Disk images. .G64 files are a low-level floppy data format for the 1541. These files can be mounted onto the virtual floppy drives. Due to the raw binary disk format, they cannot be read as container format.
 * - .t64
   - Tape Archives. .T64 files function as containers for program files of the C64. They are actually not related to loading from tape in any way.
 * - .tap
   - Tape Files. .TAP files store magnetic flux changes of a tape, so basically they are an accurate representation of the digital signal found on a tape. These files can be attached to the tape emulation, so loading originals that are captured in .TAP file format can be loaded. An extension cable is required for the U2 / U2+ to route the tape signals to the tape port of the C64. For the U64, such a cable is not required.
 * - .crt
   - Cartridge Files. .CRT files contain the definitions of cartridges that are usually found in the cartridge port. There is such a multitide of cartidge types around that not all types are (fully) supported.
 * - .bin / .rom
   - Binary Files. These files, if of the correct size, are recognized as ROM files and can be flashed accordingly.
 * - .cfg
   - Configuration Files. Since version 3.6, the internal configuration can be saved to and loaded from a text file. These files have a format similar to .ini files. Parts of these files may be distributed with certain software if these titles require a specific setting of the Ultimate cartidge.
 * - .reu
   - RAM Expansion Files. Files with this extension can be loaded into the memory of the RAM Expansion Unit. Some titles require the pre-loading of these files.
 * - .sid
   - SID Tune. Starting a .SID file invokes the built-in SID player, written by Wilfred Bos.
 * - .mus
   - MUS Tune. Starting a .MUS file invokes the built-in MUS player, written by Wilfred Bos.
 * - .mod
   - Amiga Module. Starting a .MOD file invokes the built-in MOD player, written by Freshness (Diego). This will only work when the Ultimate Audio module is available in the FPGA. The player automatically enables the mapping of this module in I/O space, as well as the REU.
 * - .u64 / .u2p / .u2u
   - Update Files. Firmware updates are distributed with these file extensions. Basically these are embedded Ultimate applications by themselves, which are started after loading. These applications program a new version of the firmware into the Flash chip.
 * - .iso
   - ISO 9660 Container. This is a container file, which provides a read-only access to an CD/DVD ROM ISO image. This may be useful when software is distributed in this format. The files then don't need to be copied separately to the SD Card or USB stick.
 * - .fat
   - FAT File System Container. A complete FAT file system can be accessed through this file container type. Although originally added for testing, it can be used to store anything from 1.44MB diskette images to entire images of other memory devices.
   

*Applies to: 1541 Ultimate-II, Ultimate-II+, Ultimate 64*
