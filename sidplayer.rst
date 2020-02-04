Ultimate SID player auto configuration
_________________________________

What this does, is to select the correct socket when the internal player is started. 
The autoconfig selects the socket based on what type of SID is found in the socket and for what type of SID the tune was written.
If the type of SID is not found, it may revert to UltiSID. This means that it will look for a 6581 if the SID header indicates this. This may lead to confusing results if the SID type installed is 8580.

If the SID types are correct, it will set the address(es) correctly, as well as the panning:

- Single SID tunes will pan to center. 
- 2SID (Stereo SID) will pan to L3/R3. 
- 3SID will pan to L4/Center/R4. 

So it is a best-effort algorithm that works best for single SID tunes and you have one 6581 and one 8580 installed. 

The SID autoconfig temporarily overrules the user configured audio mixer settings with the automatic configuration!
