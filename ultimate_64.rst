Ultimate 64
===========

This is the documentation for the Ultimate 64. Info about the hardware
and ordering can be found at https://ultimate64.com/Ultimate-64 where you also
can find QUMA(Questions You May Ask).

Getting Started
---------------

What do I need to get started

Prerequisites
.............

- Ultimate 64 motherboard
- Power adapter 12V DC (included)
- A case to put your Ultimate 64 in.
- HDMI cable or standard C64 video cable
- USB Pen drive
- Kernal ROM (extract from your Commodore 64 or download online)
- Basic ROM (extract from your Commodore 64 or download online)

Optional
........
- One or two SID chip
- Keyboard risers (for the C64C model case, you want this)
- Char ROM (the Ultimate 64 comes with a default char ROM)


Installing
----------

Connect your Ultimate 64 to the wall and your TV/monitor. If you start with
HDMI your TV/monitor have to be DVI capable over HDMI. You can change this to
HDMI later.

First you have to flash your Kernal and Basic ROM to the Ultimate 64. Power on
and wait for picture, where it explains how to do.

Basically you stick your USB drive in the back of the Ultimate 64 and push shortly on the power button
to bring up the Menu.

#. Browse to your Kernal image and press Enter.
#. Choose ``Flash as Orig. Kernal ROM``.
#. Browse to your Basic image and press Enter.
#. Choose ``Flash as Orig. Basic ROM``.
#. Push ``F5`` and choose ``Reboot C64``.

Real SID
........

If you're installing real SID chips, you have to set the jumpers accordingly.
If you don't have or don't want to install SID chips you can use the built in
fpgaSID.

::

    Voltage Jumpers:
    P1: SID 1 Voltage
    P2: SID 2 Voltage
    On/Closed: 9V (8580)
    Off/Open: 12V (6581)

    Filter Select Jumpers:
    On/Closed: 8580
    Off/Open: 6581


Now you have to set your SID types in the Ultimate-II+ menu:

| ``Short press on power button ->``
| ``F2 ->``
| ``U64 specific settings ->``
| Set your types at
| ``SID in socket 1``
| and
| ``SID in socket 2``


Menu Settings
-------------

To enter the Ultimate-II+ menu:

``Short push on the power button``

For Ultimate 64, Cartridge, SID, Drive settings etc:

``F2`` when you are in the Ultimate-II+ menu

For reset, power off, reboot etc:

``F5`` brings up options

For navigation help:

``F3`` will show navigation keys

``run/stop`` takes you back to the browser from sub-menus
or out of the Ultimate-II+ menu


Links
-----

- `Ultimate 64 homepage`_
- `Facebook group`_  - This is where discussions about the Ultimate products takes place
- `1541 Ultimate`_  - The 1541 Ultimate I, II, and II+ homepage

Contributing
------------

Okay, I have stuff to contribute. Now, tell me how?

| Great!
| Either of these will do:

- Open a pull request at github.
- Open an issue at github.


.. _Ultimate 64 homepage: https://ultimate64.com/
.. _Facebook group: https://www.facebook.com/groups/1541ultimate
.. _1541 Ultimate: http://www.1541ultimate.net/content/index.php
