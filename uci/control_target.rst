Control Target
==============

*Source basis: UCI Control Target*

.. _introduction-3:

Introduction
------------

The “UCI Control Target” provides a low-level interface to manage the
hardware state of the Ultimate cartridge or Ultimate 64 machines and its
emulated environment. This includes direct control over C64 execution
(freeze/reboot), power management for emulated disk drives, and advanced
utilities for REU and disk image handling.

The “UCI Control Target” is a target of the “Ultimate Command Interface”
(UCI), and is thus accessible from the cartridge port, through some I/O
registers. The document “Ultimate Command Interface – Register API”
describes how commands are sent over this interface.

This document describes the commands that can be sent to this target,
their expected parameters, and the data returned to the C64. These
commands allow programs to interact with the Ultimate’s management
engine without leaving the C64 environment.

In the Ultimate products and the Commodore 64 Ultimate, the “Control
Target” is accessible through target $04. This shall be the first byte
of the command.

The following paragraphs describe each of the commands of “Control
Target”.

Command Summary
---------------

CTRL_CMD_IDENTIFY (0x01)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $01

The “Identify” command sends back an identification string, such as:
“CONTROL TARGET V1.1”. The user software can use this function to query
which targets exist, or to obtain version information.

The status channel will report 00,OK, as this command cannot fail.

CTRL_CMD_FINISH_CAPTURE (0x03)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $03

Description: Finalizes an active tape capture session and closes the
associated file.

Status: 00,OK.

CTRL_CMD_FREEZE (0x05)
~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $05

Description: Triggers a hardware freeze, equivalent to pressing the
physical button on the Ultimate cartridge.

Status: 00, OK

Note that the command still needs to be acknowledged after the freeze
has completed. This might be problematic when the user selects something
else in the menu. To be fixed / addressed.

CTRL_CMD_REBOOT (0x06)
~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $06

Description: Triggers a full system reboot the C64. It corresponds to
the menu item “Reboot” in the actions menu. This command also
re-initializes the utility cartridge settings to the stored
configuration.

Response: None

Status: None

Because the C64 gets reset; the Ultimate Command Interface (UCI) gets
reset as well. Therefore no response is to be expected.

CTRL_CMD_LOAD_REU (0x08) / SAVE_REU (0x09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $08 <FILENAME> or $04 $09 <FILENAME>

Description: Loads an REU image from storage into the Ultimate’s REU
memory, or saves the current REU contents to a file.

Response: A 4-byte little-endian value representing number of bytes
transferred. Negative values indicate an error; see status reply.

Status:

00,OK

81,INVALID PARAMS

84,REU NOT ENABLED

85,REU FILE CANNOT BE OPENED.

CTRL_CMD_U64_SAVEMEM (0x0F)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $0F <FILENAME>

This command is only valid on the Ultimate 64, Ultimate 64 Elite,
Ultimate 64 Elite-II and the Commodore 64 Ultimate.

This command saves the entire RAM. It does not save any other state
information. When the filename is omitted, it will save by default to
“/temp/c64_memory.bin”

**Status:**

00,OK

87,DISK ERR: <error string>

CTRL_CMD_DECODE_TRACK (0x11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $11 <TRK> <MAX_SEC> <GCR_ADDR> <BIN_ADDR> <GCR_LEN>

Description: High-speed GCR to Binary sector conversion.

Parameters:

TRK is the expected track number.

MAX_SEC is the highest sector number expected.

GCR_ADDR is the offset in REU memory where the GCR data is located, LSB
first.

BIN_ADDR is the offset in REU memory where the decoded binary data will
be stored.

GCR_LEN is the length of the offered GCR track in bytes, LSB first.

Response: 1 byte (actual sectors) followed by 2 bytes of error flags per
sector.

Status:

00,OK

82,ERRORS ON TRACK.

CTRL_CMD_EASYFLASH_ERASE (0x20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $20 $00 <BANK> <BASEADDR>

Description: The EasyFlash Erase command emulates the sector-erase
function of an EasyFlash cartridge. This command erases a 64 KiB sector
of the emulated 1 MiB Flash chip.

**Parameters:**

Sub-command: Must be $00 (Erase)

Bank: The selected 16 KiB bank (bits 3-5 are used to determine the 64
KiB sector)

Base Address: The high byte of the C64 address. The Ultimate uses this
to determine if the Low ($8000-$9FFF) or High ($A000-$BFFF) ROM area is
targeted.

The Ultimate clears 8 banks of 8 KiB (64 KiB total) by setting all bytes
to $FF.

**Status:**

00,OK

81,INVALID PARAMS

CTRL_CMD_GET_HWINFO (0x28) - DEPRECATED
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $28 <SUB_CMD>

Description: Queries hardware information. This command has two
sub-commands, which violates the UCI concept. From firmware 3.15, when
the sub command is not given, it defaults to returning the hardware
model name in ASCII format.

Sub Command $00: Returns the hardware model name (e.g., “ULTIMATE 64”).

Sub Command $01: Returns SID configuration, including base addresses and
enable masks:

First byte contains the number of SID info frames follow.

Each SID info frame consists of 5 bytes:

Primary base address (2 bytes, LSB first)

Secondary base address (2 bytes, MSB first)

Type indicator, but unclear what it means; it seems not to match the
actual implementation of SID control.

CTRL_CMD_GET_DRVINFO ($29)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $29 <EFFECTIVE_ADDR_FLAG>

Description: This command returns the devices that the Ultimate

Response: Byte 0 is drive count, followed by 3-byte groups for each
drive: [Type] [IEC Bus Address] [Power State]. The drive types are as
follows:

+-----------------------------------+-----------------------------------+
| **Type**                          | **Value**                         |
+===================================+===================================+
| 1541                              | $00                               |
+-----------------------------------+-----------------------------------+
| 1571                              | $01                               |
+-----------------------------------+-----------------------------------+
| 1581                              | $02                               |
+-----------------------------------+-----------------------------------+
| Undecided                         | $03                               |
+-----------------------------------+-----------------------------------+
| Software IEC                      | $0F                               |
+-----------------------------------+-----------------------------------+
| Printer                           | $50                               |
+-----------------------------------+-----------------------------------+

The power state is either $00 or $01.

Status: 00,OK

CTRL_CMD_ENABLE_DRIVE_A (0x30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $30

Description: Controls the power state of emulated drive A: This command
turns the drive ON.

Status: 00,OK

CTRL_CMD_DISABLE_DRIVE_A (0x31)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $31

Description: Controls the power state of emulated drive A: This command
turns the drive OFF.

Status: 00,OK

CTRL_CMD_ENABLE_DRIVE_B (0x32)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $32

Description: Controls the power state of emulated drive B: This command
turns the drive ON.

Status: 00,OK

CTRL_CMD_DISABLE_DRIVE_B (0x33)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $33

Description: Controls the power state of emulated drive B: This command
turns the drive OFF.

Status: 00,OK

CTRL_CMD_GET_DRIVE_A_POWER (0x34)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $34

Description: With this command the power state of drive A can be
queried.

Response: “off” or “on ”

Status: 00,OK

CTRL_CMD_GET_DRIVE_B_POWER (0x35)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $35

Description: With this command the power state of drive B can be
queried.

Response: “off” or “on ”

Status: 00,OK

CTRL_CMD_GET_MP3_RAMDISKINFO (0x40)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: $04 $40

Description: This is a command specifically made for Geos MegaPatch 3.
It returns the configuration of the RAM disks found in the REU image.

Response: An 8-byte status block (2 bytes per drive) indicating RAM disk
types (1541, 1571, 1581, or Native) and their sizes. The first of the
two bytes indicates the type (0x41, 0x71, 0x81 or 0xDD). For native
partitions, the second byte indicates the size expressed in blocks of 64
KiB, otherwise it’s zero.

Status: 00,OK
