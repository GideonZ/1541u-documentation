Ultimate DOS Target
===================

*Source basis: Ultimate DOS*

.. _introduction-1:

Introduction
------------

The “Ultimate DOS” provides a way to programmatically access the
file-system of the Ultimate cartridge or Ultimate 64 main board.

“Ultimate DOS” is a target of the “Ultimate command interface”, and
is thus accessible from the cartridge port, through some I/O registers.
The document “Ultimate Command Interface – Register API” describes
how commands are sent over this interface.

This document describes the commands that can be sent to this target,
and their expected behavior and response.

The “Ultimate-DOS” target is accessible through target $01 and $02. This
shall be the first byte of the command. Note that these two targets are
instances of the DOS. They have their own state. This enables to have
two directories and two files open at a given time; one on each target.
In the examples in this chapter, target $01 is used.

The following paragraphs describe each of the commands of
“Ultimate-DOS”.

Command Summary
---------------

DOS_CMD_IDENTIFY (0x01)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $01``

The “Identify” command sends back an identification string, such as
“ULTIMATE-II DOS V1.0”. The user software can use this function to query
which targets exist, or to obtain version information.

The status channel will report ``00,OK`` as this command cannot fail.

DOS_CMD_OPEN_FILE (0x02)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $02 <attrib> <filename>``

The “Open File” command takes two arguments: an attribute byte; directly
followed by the filename to be opened. The attribute byte contains flags
that tell the file system how, in which mode, to open the file. The
following table shows which flags are applicable:

+-----------------------------------+-----------------------------------+
| **Attribute**                     | **Value**                         |
+===================================+===================================+
| FA_READ                           | $01                               |
+-----------------------------------+-----------------------------------+
| FA_WRITE                          | $02                               |
+-----------------------------------+-----------------------------------+
| FA_CREATE_NEW                     | $04                               |
+-----------------------------------+-----------------------------------+
| FA_CREATE_ALWAYS                  | $08                               |
+-----------------------------------+-----------------------------------+

To open a file in read mode, only just use $01. To open a file in write
mode, use $02 if the file you write to already exists. This mode will
not clear the file. Add $04 if you would like to create a new file to
write; this mode will clear the file to 0 bytes first. Add $08 if the
file you open may overwrite a file that already exists. (So, in order to
open a file for writing that may always overwrite an existing file, use
$0E.)

The filename does not need to be null-terminated, as the length of the
command determines the length of the file name string.

Example: ``$01 $02 $01 MYFILE``

The command will never return data. Status will either be ``00,OK``, or a
status message from the file system.

DOS_CMD_CLOSE_FILE (0x03)
~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $03``

The “Close File” command closes the file that was last opened. It does
not take any arguments, neither will this command return any data. The
status channel will read:

- ``00,OK``
- ``84,NO FILE TO CLOSE``

DOS_CMD_READ_DATA (0x04)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $04 [len_lo] [len_hi]``

The “Read Data” command will start a read transfer from the opened file.
If there is no file open, the reply will be an empty data packet, and
the status channel will read “85,NO FILE OPEN”.

The third and fourth bytes of the command indicate the total number of
bytes that will be transferred by this command. The maximum is 65,535
bytes. However, data is always transferred in chunks of 512 bytes, max.
The receiving software shall ‘accept’ the 512-byte data packet before
more data is transferred. This is due to the maximum size of the message
in the data queue.

When something goes wrong, this will be reported through the status
channel. When everything is okay, the status channel will stay quiet.

DOS_CMD_WRITE_DATA (0x05)
~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $05 [dummy] [dummy] [data …]``

The “Write Data” command will write to the file that is currently open.
If there is no file open, the status channel will read “85,NO FILE
OPEN”. If the file is not opened for writing, the file system will
return “ACCESS DENIED” onto the status channel. The command will never
return data.

The two dummy bytes are there to align the data on a long-word boundary.
The suggested transfer size is 512 bytes at a time. This will give the
optimal performance, while keeping into consideration the maximum
command transfer size.

DOS_CMD_FILE_SEEK (0x06)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $06 [posL] [posML] [posMH] [posH]``

The “File Seek” command places the pointer into the currently opened
file at a user-defined position. The command takes one argument: a 32
bit value, which is transferred LSB first.

The command never returns any data. When the seek is successful, status
returns “00,OK”, or else a message from the file system. If there is no
file open, the status channel will read “85,NO FILE OPEN”.

DOS_CMD_FILE_INFO (0x07)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $07``

The “File Info” command returns a data packet with information about the
currently open file. In fact, this command executes a file stat command.
The format of the data packet is as follows::

  uint32_t size; /\* File size \*/
  uint16_t date; /\* Last modified date \*/
  uint16_t time; /\* Last modified time \*/
  char extension[3];
  uint8_t attrib; /\* Attribute \*/
  char filename[ ];

The status response could either be:

- ``00,OK``
- ``85,NO FILE OPEN``
- ``88,NO INFORMATION AVAILABLE``

DOS_CMD_FILE_STAT (0x08)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $08 <filename>``

The “File Info” command returns a data packet with information about a file,
specified by the ‘filename’ parameter. The format of the data packet is the
same as for DOS_CMD_FILE_INFO (0x07).

The status response could either be:

- ``00,OK``
- ``88,FILE NOT FOUND``

DOS_CMD_DELETE_FILE (0x09)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $09 <filename>``

The “Delete File” command deletes the specified file.

This command does not return any data. The status channel will either
read ``00,OK`` or it will contain the appropriate filesystem error
message.

This command has been introduced in version 1.1.

DOS_CMD_RENAME_FILE (0x0a)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $0a <filename> $00 <newname>``

The “Rename File” command renames the file specified by <filename> to
<newname>.

This command does not return any data. The status channel will either
read ``00,OK`` or it will contain the appropriate filesystem error
message.

This command has been introduced in version 1.1.

DOS_CMD_COPY_FILE (0x0b)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $0b <source> $00 <destination>``

The “Copy File” command copies the file specified by <source> to the
file specified by <destination>.

This command does not return any data. The status channel will either
read ``00,OK`` or it will contain the appropriate filesystem error
message.

This command has been introduced in version 1.1.

DOS_CMD_CHANGE_DIR (0x11)
~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $11 <directory name>``

The ‘Change Directory” command is used to let the DOS enter a sub
directory. When the DOS starts, the current directory will be the root
of the SdCard. The parameter given is the name of the directory to
enter. Like Windows, Linux and MacOS, the names “.” and “..” have
special meaning: current and parent directory.

With this command, it is also possible to enter files that have
sub-entries, such as “.D64” files. These files are treated as sub file
systems, and therefore commands as “File Open” will also work on files
within.

This command does never return any data. The status channel will tell
whether the operation was successful. The two possible responses are:

- ``00,OK``
- ``83,NO SUCH DIRECTORY``.

DOS_CMD_GET_PATH (0x12)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $12``

The “Get Path” command will return the current path in the file system,
starting from the root. The path string is returned as a data packet.
The status channel reports ``00,OK``, as this command can never fail.

DOS_CMD_OPEN_DIR (0x13)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $13``

The “Open Directory” command will attempt to start reading the current
directory. The command will not return any data, but it will return
status information:

- ``00,OK``
- ``01,DIRECTORY EMPTY``
- ``86,CAN'T READ DIRECTORY``.

DOS_CMD_READ_DIR (0x14)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $14``

The “Read Directory” command will return the contents of the directory
to the data channel. Each entry of the directory is transmitted as a
data packet. The format is simple: The first byte gives the attribute of
the directory entry, followed by the file name. The attribute has the
following fields:

.. list-table::
   :header-rows: 1

   * - Bit 7
     - Bit 6
     - Bit 5
     - Bit 4
     - Bit 3
     - Bit 2
     - Bit 1
     - Bit 0
   * -
     -
     - ARCHIVE
     - DIR
     - VOLUME
     - SYSTEM
     - HIDDEN
     - READONLY

These fields are taken from the attribute byte as it exists in FAT
directories, and is reused for other non-FAT directories.

DOS_CMD_COPY_UI_PATH (0x15)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $15``

The “Copy User Interface Path” is issued to continue using the path that
was already opened in the file browser. This enables the use of relative
paths in the software.

The command is executed and then falls through to the “Get Path”
command; thus it will return the current path which the file browser is
at.

This command has been deprecated since firmware version 3.0 onwards and
will return ``99,FUNCTION NOT IMPLEMENTED``.

DOS_CMD_CREATE_DIR (0x16)
~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $16 <dirname>``

The “Create Dir” command creates the specified directory in the current
path.

This command does not return any data. The status channel will either
read ``00,OK`` or it will contain the appropriate filesystem error
message.

This command has been introduced in version 1.1.

DOS_CMD_COPY_HOME_PATH (0x17)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $17``

The “Copy Home Path” command changes into the user defined home
directory specified in the “Home Directory” setting under “User
Interface Settings”. If the directory does not exist, the appropriate
filesystem error message is reported on the status channel.

The command is executed and then falls through to the “Get Path”
command; thus it will return the current path which the file browser is
at.

This command has been introduced in version 1.1.

DOS_CMD_LOAD_REU (0x21)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $21 [addrL] [addrML] [addrMH] [addrH] [lenL] [lenML] [lenMH] [lenH]``

The “Load REU” command can be used to read data from the currently
opened file into the REU memory. The command takes two 32-bit
parameters, both LSB first. The first argument is the REU address at
which the data is loaded, the second gives the total number of bytes
that shall be read. The load function does not wrap around; the load is
truncated when the start address plus the length exceeds the end address
of the REU memory. The upper bytes of both the address as well as the
length are masked out, thus effectively these bytes are dummy bytes.

Note: This function assumes a 16 MB REU configuration.

The status message is either ``00,OK``, ``02,REQUEST TRUNCATED``, or a
message directly from the file system.

The data that is returned is a more detailed string, indicating the
number of bytes read at which address, such as: “$003000 BYTES LOADED TO
REU $126800”.

DOS_CMD_SAVE_REU (0x22)
~~~~~~~~~~~~~~~~~~~~~~~

Command format:

``$01 $22 [addrL] [addrML] [addrMH] [addrH] [lenL] [lenML] [lenMH] [lenH]``

The “Save REU” command can be used to write data to the currently opened
file from the REU memory. The command takes two 32-bit parameters, both
LSB first. The first argument is the REU address from which the data is
saved; the second gives the total number of bytes that shall be written.
The save function does not wrap around; it is truncated when the start
address plus the length exceeds the end address of the REU memory. The
upper bytes of both the address as well as the length are masked out,
thus effectively these bytes are dummy bytes.

Note: This function assumes a 16 MB REU configuration.

The status message is either ``00,OK``, ``02,REQUEST TRUNCATED``, or a
message directly from the file system.

The data that is returned is a more detailed string, indicating the
number of bytes written from which address, such as: “$008000 BYTES
SAVED FROM REU $852000”.

DOS_CMD_MOUNT_DISK (0x23)
~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $23 <id> <filename>``

The “Mount Disk” command mounts the disk image specified by the
<filename> argument on the drive using the IEC-ID specified by the
single byte argument <id>.

If there is no drive using the specified id, then the drive last mounted
on will be used. If there is no such drive, the status channel reports
``90,DRIVE NOT PRESENT``.

If the file denoted by <filename> is not a disk image, the status
channel reports ``89,NOT A DISK IMAGE``.

On successful mount the status channel reports ``00,OK``. This command
never returns any data.

This command has been introduced in version 1.1.

DOS_CMD_UMOUNT_DISK (0x24)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $24 <id>``

The “Umount Disk” command unmounts the disk currently mounted on the
drive using the IEC-ID specified by the single byte argument <id>.

If there is no drive using the specified id, then the drive last mounted
on will be used. If there is no such drive, the status channel reports
“90,DRIVE NOT PRESENT”.

On successful unmount the status channel reports ``00,OK``. The command is
considered successful even if no disk was mounted beforehand. This
command never returns any data.

This command has been introduced in version 1.1.

DOS_CMD_SWAP_DISK (0x25)
~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $0x25 <id>``

The “Swap Disk” command is equivalent to the disk swap function executed
by holding the menu button for more than one second, performed on the
drive using the IEC-ID specified by the single byte argument <id>.

If there is no drive using the specified id, then the drive last mounted
on will be used. If there is no such drive, the status channel reports
``90,DRIVE NOT PRESENT``.

This command never returns any data, and the status channel will read
``00,OK`` on success.

This command has been introduced in version 1.1.

DOS_CMD_GET_TIME (0x26)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $26 [fmt]``

This command returns the current date and time and the status channel
will read ``00,OK`` on success.

If no argument [fmt] is given or if the argument [fmt] is zero, the format
is ``yyyy/mm/dd hh:mm:ss``. If the argument [fmt] is one, the format is
``www yyyy/mm/dd hh:mm:ss``, i. e. it contains the day of the week, too.

This command has been introduced in version 1.2.

DOS_CMD_SET_TIME (0x27)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $0x27 <Y> <M> <D> <h> <m> <s>``

This command sets the current date and time and the status channel will
read ``00,OK`` on success. The year has to be reduced by 1900 in order to
fit in a single byte.

This function may be enabled or disabled by the ultimate settings. In
the latter case the status will read ``98,FUNCTION PROHIBITED``.

This command has been introduced in version 1.2.

DOS_CMD_ECHO (0xF0)
~~~~~~~~~~~~~~~~~~~

Command format: ``$01 $F0``

This command will simply echo the command back as a data packet. The
status channel will return ``00,OK``, as this command cannot fail.
