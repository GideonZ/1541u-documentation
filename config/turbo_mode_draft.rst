
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

