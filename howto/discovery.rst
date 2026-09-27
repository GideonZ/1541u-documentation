Finding an Ultimate on the Network
----------------------------------

The Ultimate answers a small UDP request that reports what it is and what it is called. This is the
supported way for an external tool to find a device on the local network, without knowing its IP
address in advance and without scanning the subnet.

The service listens on **UDP port 64**. It answers both direct requests and broadcasts.

Availability
============

The service was introduced in firmware 3.11 and is present on every Ultimate product: the
Ultimate II, II+ and II+L cartridges, the Ultimate 64 and 64 Elite, and the Ultimate 64-II.

From firmware 3.12 it can be switched off. The setting is *Ultimate Ident Service*, under
*Network Settings* in the *Services* group, and it is enabled by default. A change to this setting
takes effect at the next restart.

Making a Request
================

Send any UDP datagram to port 64. The reply comes back to the address and port the request was sent
from, so an ordinary client socket receives it without further setup.

The first four bytes of the request select the format of the reply:

+----------------------+--------------------------------------------------------------+
| Request begins with  | Reply                                                        |
+======================+==============================================================+
| ``json``, lower case | a JSON object                                                |
+----------------------+--------------------------------------------------------------+
| anything else        | a single comma separated line                                |
+----------------------+--------------------------------------------------------------+

Whatever else the request contains is sent back in the reply. This is intended to be used as a token
to match a reply to the request that caused it, which matters when a broadcast produces several
replies, or when more than one program is querying the same device.

**A token is limited to 32 bytes.** Anything longer is silently cut at 32 bytes, so a program that
compares the returned token against what it sent must keep the token within that limit or the
comparison will fail.

The Comma Separated Reply
=========================

Any request that does not begin with ``json`` produces one line, containing the request token, the
host name and the menu header:

.. code::

    send:   ident
    reply:  ident,Ultimate-64-Elite-C89085,*** Ultimate 64 Elite (V1.49) 3.14d ***

The JSON Reply
==============

A request beginning with ``json`` produces a JSON object. The token, if any, follows the four
characters ``json``:

.. code::

    send:   json7f3a1c

    reply:  {
              "product" : "Ultimate 64 Elite (V1.49) 3.14d",
              "firmware_version" : "3.14d",
              "fpga_version" : "122",
              "core_version" : "1.49",
              "hostname" : "Ultimate-64-Elite-C89085",
              "menu_header" : "*** Ultimate 64 Elite (V1.49) 3.14d ***",
              "your_string" : "7f3a1c",
              "unique_id" : "D09B96"
            }

+----------------------+--------------------------------------------------------------+
| Field                | Meaning                                                      |
+======================+==============================================================+
| ``product``          | Product name with its version, as shown in the menu          |
+----------------------+--------------------------------------------------------------+
| ``firmware_version`` | Application version, for example ``3.14d``                   |
+----------------------+--------------------------------------------------------------+
| ``fpga_version``     | FPGA version                                                 |
+----------------------+--------------------------------------------------------------+
| ``core_version``     | C64 core version. Ultimate 64 family only; the cartridges    |
|                      | leave this field out                                         |
+----------------------+--------------------------------------------------------------+
| ``hostname``         | Host name from *Network Settings*                            |
+----------------------+--------------------------------------------------------------+
| ``menu_header``      | Title line as it appears at the top of the menu              |
+----------------------+--------------------------------------------------------------+
| ``your_string``      | The request token, cut at 32 bytes                           |
+----------------------+--------------------------------------------------------------+
| ``unique_id``        | Unique identifier, present when *Unique ID* is set in        |
|                      | *Network Settings*                                           |
+----------------------+--------------------------------------------------------------+
| ``password_protected`` | Present and true only when a *Network Password* is set     |
+----------------------+--------------------------------------------------------------+

A program reading this should ignore fields it does not recognise, and should not assume that every
field is present. ``core_version`` is absent on the cartridges, and ``unique_id`` and
``password_protected`` depend on configuration.

Discovering Every Device at Once
================================

Sending the request to the broadcast address makes every Ultimate on the network answer, each from
its own address:

.. code:: python

    import socket, json

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(2.0)
    sock.sendto(b"json" + b"scan01", ("255.255.255.255", 64))

    while True:
        try:
            data, address = sock.recvfrom(4096)
        except socket.timeout:
            break
        reply = json.loads(data)
        if reply.get("your_string") == "scan01":
            print(address[0], reply["product"], reply["hostname"])

A broadcast reaches the local network segment. It does not normally cross a router into another
subnet, so a device on a separate network or on an isolated guest WiFi will not answer a broadcast
and has to be addressed directly.

The same device can answer more than once. An Ultimate 64 with both Ethernet and WiFi connected has
two addresses and can be reached on either, and a computer with more than one network adapter on the
same network may send the broadcast out of each of them. A program that collects the replies should
therefore expect duplicates and should treat ``unique_id`` rather than the address as the identity
of a device.

Notes
=====

The service answers whether or not a *Network Password* has been set. The password protects the
REST API, the FTP server and the Telnet menu; it does not apply here, so that a tool can find a
device before it authenticates to it. When a password is set, the JSON reply says so in
``password_protected``, which lets a tool prompt for the password rather than fail.

The reply is larger than the request, so a program should send one request and wait, rather than
repeat the request rapidly.

The request should not be empty. A datagram with no contents does not select a format reliably.
