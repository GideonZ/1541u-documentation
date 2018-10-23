LED Header
==========


.. figure:: ../media/hardware/hardware_led_01.png
   :alt: LED Header

Pinout  
------

===  ============
Pin  Description
===  ============
1    Power
2    Ground
3    Drive activity
===  ============


Technical information
---------------------

**Power LED**

The power pin is provided with a 260KHz PWM signal, the PWM signal makes the LED less bright.
The U64 has an onboard resistor to lower the current.

**Drive activity LED**

===  ==========================================
PWM  Description
===  ==========================================
Off  Drive Off
1/3  Drive On
2/3  Drive On + Floppy Mounted
3/3  Drive On + Floppy Mounted + Motor running	
===  ==========================================
*PWM = pulse width of the pwm signal.

