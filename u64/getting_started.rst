
Getting Started
===============

What do I need to get started?

Prerequisites
-------------

- Ultimate 64 motherboard
- Power adapter 12V DC (included)
- A case to put your Ultimate 64 in
- A C64 keyboard
- HDMI cable or standard C64 video cable
- USB Pen drive
- Kernal ROM (extract from your Commodore 64 or download online)
- Basic ROM (extract from your Commodore 64 or download online)
- Char ROM (extract from your Commodore 64 or download online)

Optional
........
- One or two SID chips
- Keyboard risers (for the C64C model case)


Installing
----------

Mounting the Ultimate 64 in a Case
..................................

If you have a spare Commodore 64C case, or bought a new case (which is 
the C64C model as well), you will need keyboard risers. Some of these have
loose metal keyboard risers already in them, others have them mounted with pop
rivets to a metal shield. If you have the latter, it is recommended to drill
the pop rivets to get the risers loose, otherwise they will interfere with
the keyboard connector on the Ultimate 64.

A few C64C have the keyboard clipped onto the top of the case. For those you
don't need keyboard risers.

*If you buy a new case online, be aware that you will need a keyboard as well.*

If you have an older case (the breadbin model), the keyboard is mounted in the
top of the case, and therefore you don't need keyboard risers.

#. Mount the risers to your keyboard. The left can be farthest to the edge, but
   the right riser you have to mount a bit to the left of the right edge, so it 
   won't interfere with the keyboard connector.
#. There are some places online where you can find risers that are supposed to
   fit perfectly with the Ultimate 64. Here is one model that should work: 
   https://www.thingiverse.com/thing:3051450 You can 3D-print them yourself or
   ask someone to do it for you. These can be screwed directly onto the bottom
   of the case as well.
#. Set the keyboard aside for now.
#. Now gently slide the Ultimate 64 board in your case, and fit it to the right
   side of the case first. The joystick connectors should slide in easy.
#. Push it gently against the back of the case, and let the connectors on the back
   of the board fit through the holes.
#. Adjust the board so you can see the mounting holes on the bottom of the case
   through the Ultimate 64 board mounting holes.
#. Fasten the board with suitable screws. Don't tighten too much.
#. Put the keyboard in the case, and connect it to the connector to the right.
   It will only fit one way, as there are a key pin on the connector.
#. Attach the top of the case.


Accessories
...........

If you have a 3D printer, or you know someone who has, you can find many nice
accessories at thingiverse. Here are a few of them:

- `Ultimate64 Keyboard Mounting Brackets <https://www.thingiverse.com/thing:3051450>`_
- `Ultimate64 & C64 Reloaded power connector cover <https://www.thingiverse.com/thing:2882271>`_
- `Ultimate64 Multi-Button (Power Button) cap <https://www.thingiverse.com/thing:2881034>`_
- `Ultimate64 board support clips <https://www.thingiverse.com/thing:2882274>`_


Connecting your Ultimate 64
...........................

Connect your Ultimate 64 to the wall and your TV/monitor. If you start with
HDMI, your TV/monitor have to be DVI capable over HDMI. You can change this to
HDMI later.

Flashing ROM
............

Before you can use your Ultimate 64, you have to flash your Kernal and Basic ROM 
to the Ultimate 64. Power on and wait for picture, where it explains how to do.

Basically you stick your USB drive in the back of the Ultimate 64 and push shortly on the power button
to bring up the Menu.

#. Browse to your Kernal ROM image and press Enter.
#. Choose ``Flash as Orig. Kernal ROM``.
#. Browse to your Basic ROM image and press Enter.
#. Choose ``Flash as Orig. Basic ROM``.
#. Browse to your Character ROM image and press Enter.
#. Choose ``Flash as Orig. Character ROM``.
#. Push ``F5`` and choose ``Reboot C64``.

Real SID
........

If you're installing real SID chips, you have to set the jumpers accordingly.
If you don't have or don't want to install SID chips you can use the built in
'EmuSID'.

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

| ``Short press on power button``
| ``F2``
| ``U64 specific settings``
| Set your types at
| ``SID in socket 1``
| and
| ``SID in socket 2``

Setting the SID type in the configuration enables the bus access to the chip,
and also allows the auto-configurator to choose the right chip when playing
a SID tune with the provided player from Wilfred Bos.

