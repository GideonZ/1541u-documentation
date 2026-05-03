FTP Client in the File Browser
------------------------------

The FTP client feature makes a remote FTP server available directly in the Ultimate file browser. After a server has
been added, it appears under the ``/ftp`` entry and can be browsed much like a directory on a USB stick or SD card.
Files can be opened, copied from the server, copied to the server, renamed and deleted from the normal file browser
menus.

Requirements
============

The Ultimate needs a working network connection through Ethernet or WiFi. The FTP server must allow passive FTP
connections. The connection is plain FTP; it is not FTPS or SFTP, so passwords and file data are not encrypted on the
network.

Adding a Server
===============

Open the file browser and navigate to the ``ftp`` root entry. Press enter and select context menu item ``New Host``. The form
contains the following fields:

Alias
  The name that will be shown in the file browser.

Host
  The host name or IP address of the FTP server.

Port
  The TCP port of the FTP server. The usual FTP port is ``21``.

User
  The user name for the FTP server. For anonymous FTP, use ``anonymous`` if the server expects that.

Password
  The password for the FTP account.

Path
  The start directory on the FTP server, for example ``/`` or ``/pub/c64``.

After the host has been added, enter it from the ``/ftp`` directory to connect and browse the configured start
directory.

Editing or Removing a Server
============================

Select the server entry in the ``/ftp`` directory and press F5. Use ``Edit`` to change the connection details, or
``Remove`` to delete the server entry from the list.

Using Files
===========

Remote directories are listed when they are opened. Files are downloaded to the temporary cache when first opened. This
means that opening a large file may take a while before the selected action continues. Once cached, the local temporary
copy may be reused.

Copying a file to an FTP directory uploads it to the server. Creating directories, renaming files and deleting files are
performed on the remote server.

Configuration File
==================

The server list is stored in ``/flash/config/ftp_servers``. This file is managed by the Ultimate menu and normally does
not need to be edited manually. It can be backed up or removed if you want to copy or reset the FTP server list.

Limitations
===========

- Only plain passive FTP is supported. FTPS and SFTP are different protocols and are not supported.
- File data is cached in the temporary storage area before it is opened by the file browser.
- If the remote file changes while an older copy is still cached, the cached copy may be used until the temporary cache
  is cleaned or replaced.

*Applies to: Ultimate-II+, Ultimate-II+L and all variants of the Ultimate 64, starting from Firmware version 3.15

