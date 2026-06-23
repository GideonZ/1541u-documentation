Software IEC Target
===================

*Source basis: UCI Software IEC Target*

.. _introduction-4:

Introduction
------------

The “UCI SoftwareIEC Target” provides an optimized interface to the
emulated disk drive that sits behind the SoftwareIEC interface. It
bypasses the IEC protocol completely and therefore allows higher
speed data transfers.

The “UCI SoftwareIEC Target” is a target of the “Ultimate Command Interface”
(UCI), and is thus accessible from the cartridge port, through some I/O
registers. The document “Ultimate Command Interface – Register API”
describes how commands are sent over this interface.

This document describes the commands that can be sent to this target,
their expected parameters, and the data returned to the C64. These
commands allow programs to interact with the Ultimate’s management
engine without leaving the C64 environment.

In the Ultimate products and the Commodore 64 Ultimate, the “Software
IEC Target” is accessible through target $05. This shall be the first
byte of the command.

The following paragraphs describe each of the commands of “Software IEC
Target”.

Status Codes
------------

Unless noted otherwise, the status returned by a command starts with a
single status byte. The following codes are defined:

.. list-table::
   :header-rows: 1
   :widths: 10 30 60

   * - Code
     - Name
     - Meaning
   * - ``$00``
     - OK
     - Command completed successfully.
   * - ``$01``
     - FILE NOT FOUND
     - The requested file could not be opened.
   * - ``$02``
     - SAVE ERROR
     - The file could not be created or a write error occurred while
       saving.
   * - ``$03``
     - NO INPUT CHANNEL
     - ``get_more_data`` was requested while no channel was prepared by
       a preceding CHKIN.
   * - ``$04``
     - UNKNOWN COMMAND
     - The command byte is not recognised by this target.
   * - ``$05``
     - IEC MODULE NOT LOADED
     - The SoftwareIEC drive is not active. **Every** command returns
       this code when the emulated drive behind the SoftwareIEC
       interface has not been loaded.
   * - ``$06``
     - INVALID PARAMETERS
     - The command was malformed (e.g. wrong length, or a required
       separator was missing).
   * - ``$07``
     - INVALID NAME
     - The supplied IEC name could not be parsed.
   * - ``$08``
     - INVALID PARTITION
     - The referenced partition number does not exist.
   * - ``$09``
     - INVALID DIRECTORY
     - The directory or file path could not be resolved.

For the LOAD command, a status byte of ``$80`` is used to signal a
verify failure (see SOFTIEC_CMD_LOAD_EX).

Command Summary
---------------

SOFTIEC_CMD_IDENTIFY (0x01)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $01``

Response: Returns the string: ``SOFTWARE IEC TARGET V1.0``.

Status: ``$00`` OK.

SOFTIEC_CMD_LOAD_SU (0x10)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $10 <SEC_ADDR> <VERIFY> <ADDR_LO> <ADDR_HI> <NAME>``

Description: Prepares a file for loading. It opens the file and
retrieves the 2-byte start address stored in the file.

Parameters:

- <SEC_ADDR>: Secondary address ($00 for load).
- <ADDR_LO/HI>: Override load address if SEC_ADDR is 0.

Response: Returns the 2-byte start address found in the file.

Status:

- ``$00`` OK
- ``$01`` FILE NOT FOUND

SOFTIEC_CMD_LOAD_EX (0x11)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $11 <SEC_ADDR> <VERIFY>``

Description: Executes the actual data transfer from the file opened by
LOAD_SU directly into C64 RAM using a DMA transfer.

Parameters: If <VERIFY> is $01, the Ultimate compares the file data
against C64 memory instead of writing it.

Response: None

Status: The first byte is the status byte: ``$00`` OK for success,
``$80`` when a verify failure occurs. When loading, the second and third
byte contain the end address of the load in little endian format.

SOFTIEC_CMD_SAVE (0x12)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $12 <VERIFY> <SEC_ADDR> <START_LO/HI> <END_LO/HI> <NAME>``

Description: Saves a block of C64 memory to a file.

Logic: The Ultimate creates the file, writes the 2-byte start address,
and then dumps the memory range before closing.

Status: ``$00`` OK or ``$02`` SAVE ERROR.

SOFTIEC_CMD_OPEN (0x13)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $13 <SEC_ADDR> $00 <NAME>``

Description: The OPEN command opens a file in the virtual file system
and attaches it to a channel indicated by the secondary address.

Data Response: None

Status: None

SOFTIEC_CMD_CLOSE (0x14)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $14 <SEC_ADDR>``

Description: The CLOSE command closes the file that is associated with
the channel indicated by the secondary address.

Data Response: none

Status: ``$00`` OK

SOFTIEC_CMD_CHKIN (0x15)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $15 <SEC_ADDR>``

Description: Equates to the Kernal CHKIN call. It prepares the specified
channel for reading data.

The target pre-fetches the first 32 bytes of data and places them in the
UCI Data Channel for immediate retrieval. Further data is fetched via
the get_more_data mechanism.

Usually, CHKIN is followed by consecutive calls to CHRIN to read the
data from the channel. It would be highly inefficient to send a UCI
command for every byte that is being read. Therefore, HyperSpeed kernal
simply allows data to be prefetched with the CHKIN command, and reads
from the data channel whenever the function CHRIN is called. This means
that the UCI command is still ‘open’ when this happens. When CHRIN is
called upon another channel, or any another command needs to be sent to
the UCI, the pending CHKIN command is terminated first. This termination
causes the exact number of bytes that was read from the response channel
to be flushed from the stream, such that subsequent calls to CHKIN will
prepare the next chunk of data from the file.

SOFTIEC_CMD_CHKOUT (0x16)
~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $16 <SEC_ADDR> $00 <DATA...>``

Description: Equates to the Kernal CHKOUT call. It sends data to the
specified channel.

- If SEC_ADDR is in the range of $F0-$FF, it performs an OPEN operation.
- If SEC_ADDR is in the range of $E0-$EF, it performs a CLOSE operation.
- Otherwise, it pushes the provided <DATA> bytes into the drive's write buffer.

SOFTIEC_CMD_ADD_PARTITION (0x20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $20 <INDEX> <IDENT> ':' <PATH> [$00]``

Description: Adds (or replaces) a partition in the SoftwareIEC virtual
file system. The partition number <INDEX> is mapped onto a host file
system <PATH> and given the IEC partition name <IDENT>.

Parameters:

- <INDEX>: The partition number to assign (single byte).
- <IDENT>: The IEC partition name (PETSCII), located before the colon.
- <PATH>: The host file system path, located after the colon.
- A trailing ``$00`` byte is optional and is stripped if present.

The remainder of the command (everything from byte 3 onward) is treated
as a single string of the form ``IDENT:PATH``; the first colon separates
the name from the path.

Example: ``$05 $20 $03 'NAME' ':' '/this/is/a/path'`` maps partition 3,
named ``NAME``, onto ``/this/is/a/path``.

Response: None

Status:

- ``$00`` OK
- ``$06`` INVALID PARAMETERS, returned when the command is shorter than 6
  bytes or when no colon separator is found.

SOFTIEC_CMD_DEL_PARTITION (0x21)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $21 <INDEX>``

Description: Removes the partition identified by <INDEX> from the
SoftwareIEC virtual file system.

Parameters:

- <INDEX>: The partition number to remove (single byte).

Response: None

Status:

- ``$00`` OK
- ``$06`` INVALID PARAMETERS, returned when the command length is not
  exactly 3 bytes.

SOFTIEC_CMD_GET_FATNAME (0x22)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $22 <CHANNEL> <IEC_NAME>``

Description: Resolves the host (FAT) path that *would* result from
opening <IEC_NAME> on the given channel, without actually opening any
file. This allows host-side tooling to discover where a given IEC name
maps in the underlying file system. The <IEC_NAME> is a CBM DOS open
string, exactly as it would be passed to an OPEN command (it may contain
a partition prefix, a path, a file type and an access mode).

Parameters:

- <CHANNEL>: The secondary address / channel number. Its low nibble is
  used to derive default file type and access mode (channel 0 defaults
  to PRG/read, channel 1 to PRG/write, other channels to SEQ for
  writes).
- <IEC_NAME>: The CBM DOS open string (PETSCII), null-termination is
  applied by the target.

Response: The resolved host path string. The exact content depends on
the type of stream the name resolves to:

- A buffer stream returns ``/buffer``.
- A partition-listing stream returns ``/partitions``.
- A directory stream returns the resolved host directory path.
- A regular file returns the fully constructed host file path.

Status:

- ``$00`` OK
- ``$06`` INVALID PARAMETERS, when the command is too short or exceeds
  the maximum command length.
- ``$07`` INVALID NAME, when the IEC name cannot be parsed.
- ``$08`` INVALID PARTITION, when the referenced partition does not
  exist.
- ``$09`` INVALID DIRECTORY, when the directory or file path cannot be
  resolved.

SOFTIEC_CMD_GET_IECNAME (0x23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$05 $23 <FAT_NAME>``

Description: Performs the reverse mapping of GET_FATNAME. Given a host
(FAT / long) filename, it determines the IEC (CBM) filename and file
type under which that file would be presented on the IEC bus. The file
type is derived from the file’s extension.

Parameters:

- <FAT_NAME>: The host filename (the extension is used to determine the
  file type).

Response: The first byte is the file type, followed by the IEC name
string. The file type byte uses the following encoding:

.. list-table::
   :header-rows: 1
   :widths: 15 30

   * - Value
     - File type
   * - ``$00``
     - (any / DEL)
   * - ``$01``
     - PRG
   * - ``$02``
     - SEQ
   * - ``$03``
     - USR
   * - ``$04``
     - REL
   * - ``$05``
     - folder

Status:

- ``$00`` OK
- ``$06`` INVALID PARAMETERS, when the command is too short or exceeds
  the maximum command length.

💡 Implementation Insights
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automatic Throttling: The prepare_data function in the CHKIN call
initially fetches 32 bytes to minimize latency, but will scale up to 256
bytes per request if the C64 continues to pull more data.

DMA Integration: The load/save/verify routines check is_dma_active(). If
the Ultimate is performing a DMA transfer, it pauses the C64 CPU to
ensure data integrity.

Kernal Emulation: This target is specifically designed to allow custom
Kernals or fast-loaders to avoid the IEC protocol entirely and access
the SoftwareIEC directly through an efficient cartridge I/O mechanism.
