Network Target
==============

*Source basis: UCI Network Target*

.. _introduction-2:

Introduction
------------

The “Network Target” exposes the network stack in the Ultimate
management application to be used by programs written on the C64 side.
This interface offloads the responsibility of setting up and managing a
TCP connection to a named host, allowing the C64 program to directly
exchange data with external servers.

The “Network Target” is a target of the “Ultimate Command Interface”
(UCI), and is thus accessible from the cartridge port, through some I/O
registers. The document “Ultimate Command Interface – Register API”
describes how commands are sent over this interface.

This document describes the commands that can be sent to this target,
and their expected behavior and response. These commands are used to set
up and close connections, and write and read from the network sockets.

In the Ultimate products and the Commodore 64 Ultimate, the “Network
Target” is accessible through target $03. This shall be the first byte
of the command.

The following paragraphs describe each of the commands of “Network
target”.

Command Summary
---------------

NET_CMD_IDENTIFY (0x01)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $01``

The “Identify” command sends back an identification string, such as:
“ULTIMATE-II NETWORK INTERFACE V1.0”. The user software can use this
function to query which targets exist, or to obtain version information.

The status channel will report ``00,OK``, as this command cannot fail.

To avoid repetition, all commands may return ``81,INVALID PARAMS`` if the
command length or format is incorrect.

NET_CMD_GET_INTERFACE_COUNT (0x02)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $02``

This command queries the Ultimate application for the number of
available network interfaces (e.g., Ethernet, Wi-Fi).

Response: A single byte in the data channel representing the count of
interfaces.

Status: ``00,OK``.

NET_CMD_GET_NETADDR (0x04)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $04 <INTERFACE_INDEX>``

Retrieves the physical Hardware Address (MAC address) of the specified
network interface.

Parameters: <INTERFACE_INDEX> is a single byte.

Response: 6 bytes representing the MAC address.

Status: ``00,OK``, or ``82,PARAMETER(S) OUT OF RANGE`` if the index is invalid.

NET_CMD_GET_IPADDR (0x05)
~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $05 <INTERFACE_INDEX>``

The “Get IPAddr” command retrieves the current IP address assigned to
the specified network interface.

Parameters: <INTERFACE_INDEX> is a single byte.

Response: 12 bytes representing the IP addresses in raw binary format.

- The first 4 bytes contain the used IP address, e.g. 192.168.1.146
- The second 4 bytes contain the local net mask, e.g. 255.255.255.0
- The last 4 bytes contain the local LAN gateway, e.g. 192.168.1.254

Status: ``00,OK``.

NET_CMD_SET_IPADDR (0x06)
~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $06 <INTERFACE_INDEX> <IP_DATA>``

This command manually sets the IP address for a specific interface.

Parameters: Requires a 1-byte index followed by 12 bytes of IP data.

- The first 4 bytes shall contain the used IP address, e.g. 192.168.1.146
- The second 4 bytes shall contain the local net mask, e.g. 255.255.255.0
- The last 4 bytes shall contain the local LAN gateway, e.g. 192.168.1.254

Status: ``00,OK``.

NET_CMD_OPEN_TCP (0x07)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $07 <PORT_LSB> <PORT_MSB> <HOSTNAME/IP_STRING>``

Opens a stream-based TCP connection to a remote host.

Parameters: The port is a 16-bit value (Little-Endian). The hostname is
a null-terminated string or IP address.

Response: A single byte representing the Socket Handle.

Status: ``00,OK``, or ``84,UNRESOLVED HOST`` if DNS lookup fails.

NET_CMD_OPEN_UDP (0x08)
~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $08 <PORT_LSB> <PORT_MSB> <HOSTNAME/IP_STRING>``

Opens a connectionless UDP socket for datagram exchange. Identical in
format to OPEN_TCP, but initializes a SOCK_DGRAM type socket.

Response: A single byte representing the Socket Handle.

NET_CMD_CLOSE_SOCKET (0x09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $09 <SOCKET_HANDLE>``

Closes the specified socket and frees the associated internal resources.

Status: ``00,OK``.

NET_CMD_OPEN_UDP_LOCAL (0x0A)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $0A <REMOTE_PORT_LSB> <REMOTE_PORT_MSB> <LOCAL_PORT_LSB> <LOCAL_PORT_MSB> <HOSTNAME/IP_STRING>``

Opens a UDP socket like OPEN_UDP, but from a local port of your choice.

Parameters: Both ports are 16-bit values (Little-Endian). A local port of
0 means any free port. The remote port must not be 0. The host is a hostname or a dotted IPv4 address of 1 to 253
characters, optionally followed by one ``$00``; nothing may follow the
``$00``. The command cannot be sent with the no-reply flag set, because a
program that does not see the reply cannot close the socket, and the port
would stay in use.

The host name is resolved before the local port is bound, so a host that
cannot be resolved leaves the port free.

Response: Three bytes: the Socket Handle, followed by the local port
that was bound (Little-Endian). A local port of 0 yields a port in the
range 49152 to 65535.

Status: ``00,OK``, or one of:

- ``81,INVALID PARAMS`` for a malformed command
- ``82,PARAMETER(S) OUT OF RANGE`` if the remote port is 0
- ``84,UNRESOLVED HOST`` if DNS lookup fails
- ``85,ERROR OPENING SOCKET`` if no socket is available
- ``89,PORT IN USE`` if the local port is already in use
- ``86,INTERNAL ERROR`` if the bound port cannot be read back
- ``11,ERROR ON CONNECT: <errno>``

Status 89 means something else in other targets. The numbering of status
codes is per target.

The socket is filtered to the remote host and port, like a socket from
OPEN_UDP: it only receives datagrams that come from that address and
port. It is read, written and closed with the same commands as any other
socket.

The one exception is a remote host of ``0.0.0.0``. The socket then accepts
datagrams from any sender whose source port equals the remote port; datagrams
from other source ports are dropped. Use such a socket only to receive. A
WRITE on it goes out as a link-layer broadcast to ``0.0.0.0``. To send, use a
socket opened to the subnet broadcast address or to the peer. This describes
how the firmware behaves today.

Sending to the subnet broadcast address needs no socket option, because
lwIP's broadcast filters (``IP_SOF_BROADCAST`` and
``IP_SOF_BROADCAST_RECV``) are off, which is lwIP's default. A broadcast
is received like any other datagram: it passes the filter above, so a
socket opened to the subnet broadcast address does not receive it, and a
socket opened to ``0.0.0.0`` with the sender's port does.

The port is in use if another UDP socket holds it, whether opened by your
program or by the Ultimate itself, for example the ident service on UDP
port 64 while it is enabled, or the DHCP client on UDP port 68 while the
Ultimate uses DHCP. TCP sockets do not use UDP
ports, so they never conflict. The port stays in use until the socket is
closed, and it can be opened again as soon as CLOSE_SOCKET returns. A C64
reset closes the socket and frees the port.

To find out whether the firmware has this command, send it with a remote
port of 0 and a host of at least one character. Firmware that has it answers
``82,PARAMETER(S) OUT OF RANGE`` and opens nothing; firmware that does not
answers ``21,UNKNOWN COMMAND``.

NET_CMD_READ_SOCKET (0x10)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $10 <SOCKET_HANDLE> <LEN_LSB> <LEN_MSB>``

With this command a block of data can be read from an open socket.

Parameters: The length requested is a 16-bit value (Little-Endian).

Response: The data channel begins with a 2-byte header indicating the
actual number of bytes read, LSB first, followed immediately by the data
payload.

Status: ``00,OK``, or ``01,CONNECTION CLOSED BY HOST`` if the remote side
terminated the session.

NET_CMD_WRITE_SOCKET (0x11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Command format: ``$03 $11 <SOCKET_HANDLE> <DATA...>``

With this command, data can be sent through an open socket.

Parameters: The data to be sent follows the handle. The command length
determines the payload size.

Response: A 2-byte value indicating the number of bytes successfully
sent, LSB first.

Status: ``00,OK``.
