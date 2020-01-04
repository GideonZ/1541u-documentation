Setting up the MultiSID configuration on the Ultimate 64
========================================================

This page explains how to use the visual SID address editor to set the UltiSID in MultiSID mode, giving
you four or even eight SIDs.

In the following example, it is assumed that the settings are as follows:
* SID Socket 1 Address: Unmapped
* SID Socket 2 Address: Unmapped
* UltiSID 1 Address: $D400
* UltiSID 2 Address: $D420
* UltiSID Range Split: Off
* Auto Address Mirroring: Enabled

First step is to enter the visual editor and note that UltiSID 1 is mapped at $D400, UltiSID 2 is mapped at $D420 and auto mirroring is on, just like the settings we started with. Address mirroring means that the appearance of the available SIDs are mirrored in the address space, such that they fill up the $D400-$D7FF range. Also pay attention that the lower line shows “Socket 1”, which means that the controls (cursor and split) now have effect on socket 1.

We want to change the UltiSID settings, so we press “3” on the keyboard; the highlighted number next to the “USID1” label.
Press “M” to turn off auto mirroring, to have a better view of the settings. Note the lower line says
“UltiSid 1”, which we will modify.

When pressing “S”, the split function gets enabled. The line below shows the split is active on one
address line, being A6. This means the UltiSIDs (both of them) get split in two, and the second part of
it gets enabled with address line 6 set (thus $D440). Note that this instance gets a “B”, indicating the
second half of the split UltiSID1. The same goes for UltiSID2, which now appears at $D460.

Similarly for a split on A7; the second half appears with an offset of $80.

And last but not least, split on _two_ address lines, causing the UltiSID to be split into four SIDs. In
this case A7 and A8, such that the second part appears at $D480 (A7=1), the third part at $D500
(A8=1), and the fourth part at $D580 (A7=1, A8=1). Also note the letters A, B, C and D.

Since the split settings are shared for both UltiSIDs, UltiSID2 also gets split in the same way. But
because its base address was set at $D420 (A5=1), the splits appear also at offsets where A5=1, thus
$D420, $D4A0, $D520, $D5A0. In total 8 SIDs, thus 24 voices and 8 independent filters.
