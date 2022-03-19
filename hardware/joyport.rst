Joystick Ports
==============

Pinout  
------

===  ============
Pin  Description
===  ============
1    Up
2    Down
3    Left
4    Right
5    POT Y
6    Fire
7    +5V
8    GND (0V)
9    POT X
===  ============

Joystick Swap
--------------

With the introduction of the Elite boards, the pins are no longer directly attached to the same 6526 CIA pins as the keyboard, like on a C64.
Instead, these signals are combined in the Xilinx PLD. This makes it possible to switch the joystick ports from software.

To switch the joystick ports, enter the menu and press C= + J.

Paddle Support
--------------
The POT-X and POT-Y pins support reading analog values from a controller, like a paddle. The original paddles are simply potentiometers with a knob
and can function as a simple control for a race game steering wheel or paddle control in Pong.

On the original C64, the paddle ports are sampled by the SID chip. Because the Ultimate 64 does not require a real SID chip to operate, the POT-X
and POT-Y signals are handled locally on the board itself and are therefore NOT connected to the SID sockets.

How do the paddle sampling work?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This aforementioned potentiometer (variable resistor) of a paddle controller connects between the +5V and the POT-X or POT-Y input pins.
This external resistor charges a capacitor. This capacitor is discharged by for 256 machine cycles and is enabled to charge during another 256 cycles.
Once the voltage on the POT-X pin crosses a certain threshold, the counter value is latched. When this counter reaches 255, the capacitor is again
discharged for 256 cycles. This delivers a readout value every 512 machine cycles (PHI2) (~2 kSPS).

Because of a large leakage current in the original SID from these pins, the voltage observed on the POT pins raises relatively fast for the first volt or so.
Above this voltage, the potentiometer becomes dominant in charging the capacitor. The latch-threshold is about 2.25V. 

On te U64, the charge on the capacitor depends predominantly on the external resistor in the paddle. To get a reasonable match of the readout values,
a lower threshold was chosen. However, this gives issues with external devices like Koalapad, because Koalapad lets the POT-X and POT-Y pins sit just
below the threshold (of a SID), and pulls it over the threshold at a defined time after it recognizes the discharge of the capacitor, depending on
where the drawing pen presses the pad. The result is that the U64 does not read the Koalapad position, but just reads a low value, because the comparator trips too early.

In order to fix this, some resistors need to be changed on the U64 board near the keyboard connector, on the very lower right (before serial number ~3000):


