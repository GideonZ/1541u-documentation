
Turbo mode settings
===================

Turbo control
............. 

.. image:: ../media/config/config_turbo_02_control.png
   :alt: Turbo control
   :align: left
   
+----------------------+----------------------------------------------------------------+
| Option               | Description                                                    |
+======================+================================================================+
| Off                  | Turbo control is off                                           |
+----------------------+----------------------------------------------------------------+
| Manual               | Turbo control uses settings from U64.                          |
|                      |                                                                |
|                      | Settings **CANNOT** be controlled with registers programmable. |
+----------------------+----------------------------------------------------------------+
| U64 Turbo Registers  | Turbo control uses settings from U64.                          |
|                      |                                                                |
|                      | Settings **CAN** be controlled with registers programmable.    |
|                      |                                                                |
|                      | *See Turbo Control registers.*                                 |
+----------------------+----------------------------------------------------------------+
| TurboEnable Bit      | Turbo control uses settings from U64.                          |
|                      |                                                                |
|                      | Settings **CAN** be controlled with registers programmable.    |
|                      |                                                                |
|                      | *See Turbo Control registers.*                                 |
+----------------------+----------------------------------------------------------------+



CPU Speed
......... 

.. image:: ../media/config/config_turbo_03_cpu_speed.png
   :alt: Turbo cpu speed
   :align: left
   
   
|**Set CPU Speed.**
|
|Default C64 speed: 1MHz (1x)
|Maximum speed: 48MHz (48x)
   

Badline Timing
..............

.. image:: ../media/config/config_turbo_04_badline_timing.png
   :alt: Turbo badline timing
   :align: left   
   
   
SuperCPU Detect ($D0BC)
.......................


Turbo Control registers
=======================

+-------------+----------------------------------------------------------------+
| Address     | Description                                                    |
+=============+================================================================+
| 53297/$D031 |	**U64 Turbo Control**                                          |
|             |                                                                |
|             | This register is only available when the Turbo Mode selector   |
|             | is set to 'U64 Turbo Registers' or 'Turbo Enable Bit'.         |
|             | Otherwise it simply reads $FF.                                 |
|             |                                                                |
|             | * bit 0-3: CPU Speed (index)                                   |
|             | * bit 7: Badline timing, 0 = Enabled, 1 = Disabled             |
|             |                                                                |
|             | CPU Speed (index)                                              |
|             |                                                                |
|             | * 0  = 1 MHz                                                   |
|             | * 1  = 2 MHz                                                   |
|             | * 2  = 3 MHz                                                   |
|             | * 3  = 4 MHz                                                   |
|             | * 4  = 5 MHz                                                   |
|             | * 5  = 6 MHz                                                   |
|             | * 6  = 8 MHz                                                   |
|             | * 7  = 10 MHz                                                  |
|             | * 8  = 12 MHz                                                  |
|             | * 9  = 14 MHz                                                  |
|             | * 10 = 16 MHz                                                  |
|             | * 11 = 20 MHz                                                  |
|             | * 12 = 24 MHz                                                  |
|             | * 13 = 32 MHz                                                  |
|             | * 14 = 40 MHz                                                  |
|             | * 15 = 48 MHz                                                  |
+-------------+----------------------------------------------------------------+
| 53296/$D030 |	**Turbo Enable Bit**                                           |
|             |                                                                |
|             | This register is only available when the Turbo Mode selector   |
|             | is set to 'Turbo Enable Bit'.                                  |
|             | Otherwise it simply reads $FF.                                 |
|             |                                                                |
|             |	* bit 0 (Write):                                               |
|             |                                                                |
|             |	  0 = 1 MHz + Badlines                                         |
|             |                                                                |
|             |	  1 = Use settings from menu                                   |
|             |                                                                |
|             |	* bit 0 (Read):                                                |
|             |                                                                |
|             |	  0 = Turbo Off                                                |
|             |                                                                |
|             |	  1 = Turbo On                                                 |
+-------------+----------------------------------------------------------------+
| 53370/$D07A |	**SuperCPU compatible enable/disable registers**               |
|             |                                                                |
|             | This register is only available when the Turbo Mode selector   |
|             | is set to 'U64 Turbo Registers' or 'Turbo Enable Bit'.         |
|             | This register is **write only**                                |
|             |                                                                |
|             | * Software Speed Select - Normal                               |
|             |	                                                               |
|             |	see: https://www.c64-wiki.com/wiki/SuperCPU                    |
+-------------+----------------------------------------------------------------+
| 53371/$D07B |	**SuperCPU compatible enable/disable registers**               |
|             |                                                                |
|             | This register is only available when the Turbo Mode selector   |
|             | is set to 'U64 Turbo Registers' or 'Turbo Enable Bit'.         |
|             | This register is **write only**                                |
|             |                                                                |
|             | * Software Speed Select - Turbo (20 MHz)($079)                 |
|             |	                                                               |
|             |	see: https://www.c64-wiki.com/wiki/SuperCPU                    |
+-------------+----------------------------------------------------------------+
| 53424/$D0B0 |	**SuperCPU Detect ($D0BC)**                                    |
|             |                                                                |
|             | * SuperCPU Mode Detect Register                                |
|             |	                                                               |
|             | This register is only available when it is separately enabled. |
|             | This register is **read only**                                 |
|             |                                                                |
|             |	see: https://www.c64-wiki.com/wiki/SuperCPU                    |
+-------------+----------------------------------------------------------------+




Applies to: Ultimate 64

\*) Setting is only available on the Ultimate 64, firmware >= 1.33*
