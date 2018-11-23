
USER PORT
---------

.. image:: ../media/hardware/hardware_userport_01.png
   :alt: User Port Extension Header
   :align: left
	
**User Port Extension Header**

=== ======= =====================================================================
Pin Name    Description
=== ======= =====================================================================
  1 GND     Ground
  2 +5V     +5 VDC (100 mA max)
  3 /RESET  Reset, will force a Cold Start. Also a reset output for devices.
  4 CNT1    Counter 1, from CIA #1
  5 SP1     Serial Port 1, from CIA #1
  6 CNT2    Counter 2, from CIA #2
  7 SP2     Serial Port 2, from CIA #2
  8 /PC2    Handshaking line, from CIA #2
  9 ATN     Serial Attention In
 10 12VDC   12VDC
 11 12VDC   12VDC
 12 GND     Ground 
  A GND     Ground (RS232: GND)
  B /FLAG2  Flag 2 (RS232: RxD=Both B+C) 
  C PB0     Data 0 (RS232: RxD=Both B+C)
  D PB1     Data 1 (RS232: RTS)
  E PB2     Data 2 (RS232: DTR)
  F PB3     Data 3 (RS232: RI)
  H PB4     Data 4 (RS232: DCD)
  J PB5     Data 5 
  K PB6     Data 6 (RS232: CTS)
  L PB7     Data 7 (RS232: DSR)
  M PA2     PA2    (RS232: TxD)
  N GND     Ground (RS232: GND) 
=== ======= =====================================================================
	
*Applies to: Ultimate 64*
