Turbo Control registers
=======================

+-------------+----------------------------------------------------------------+
| Address     | Description                                                    |
+=============+================================================================+
| 53297/$D031 |	Turbo Control                                                  |
|             |                                                                |
|             | =============                                                  |
|             | OFF / Manual: value = 255                                      |
|             |                                                                |
|             | U64 turbo register & Turbo Enable Bit:                         |
|             |                                                                |
|             | * bit #0-#3: CPU Speed (index)                                 |
|             | * bit #7: Badline timing, 0 = Enabled, 1 = Disabled            |
|             |                                                                |
|             | CPU Speed (index)                                              |
|             | =================                                              |
|             | 0  = 1MHz                                                      |
|             | 1  = 2MHz                                                      |
|             | 2  = 3MHz                                                      |
|             | 3  = 4MHz                                                      |
|             | 4  = 5MHz                                                      |
|             | 5  = 6MHz                                                      |
|             | 6  = 8MHz                                                      |
|             | 7  = 10MHz                                                     |
|             | 8  = 12MHz                                                     |
|             | 9  = 14MHz                                                     |
|             | 10 = 16MHz                                                     |
|             | 11 = 20MHz                                                     |
|             | 12 = 24MHz                                                     |
|             | 13 = 32MHz                                                     |
|             | 14 = 40MHz                                                     |
|             | 15 = 48MHz                                                     |
+-------------+----------------------------------------------------------------+
| 53296/$D030 |	Turbo Enable Bit                                               |
|             |	=================                                              |
|             |	* bit 0:                                                       |
|             |	  0 = 1 MHz + Badlines                                         |
|             |	  1 = Use settings from menu                                   |
+-------------+----------------------------------------------------------------+
| 53370/$D07A |	SuperCPU compatible enable/disable registers                   |
|             |	============================================                   |
|             | * Software Speed Select - Normal                               |
|             |	                                                               |
|             |	see: https://www.c64-wiki.com/wiki/SuperCPU                    |
+-------------+----------------------------------------------------------------+
| 53371/$D07B |	SuperCPU compatible enable/disable registers                   |
|             |	============================================                   |
|             | * Software Speed Select - Turbo (20 MHz)($079)                 |
|             |	                                                               |
|             |	see: https://www.c64-wiki.com/wiki/SuperCPU                    |
+-------------+----------------------------------------------------------------+
| 53424/$D0B0 |	SuperCPU Detect ($D0BC)                                        |
|             |	=======================                                        |
|             | * SuperCPU Mode Detect Register                                |
|             |	                                                               |
|             |	see: https://www.c64-wiki.com/wiki/SuperCPU                    |
+-------------+----------------------------------------------------------------+
