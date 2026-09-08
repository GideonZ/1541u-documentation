# 1541 Ultimate Firmware 3.15

Firmware 3.15 is a major update for the Ultimate product family, bringing new remote-control and development features, improved disk-drive and USB compatibility, new cartridge and SID hardware support, and a large number of stability and networking fixes.

The release supports the Ultimate-II, Ultimate-II+, Ultimate-II+L, Ultimate 64 and Ultimate 64-II. Some features are hardware-specific, as noted below.

## Highlights

- New built-in machine-code monitor, assembler and disassembler
- REST API control of keyboard, joysticks and the Ultimate menu
- Generated OpenAPI description for easy REST API exploration and integration
- Major extensions to the Ultimate Command Interface (UCI)
- New FTP client for browsing remote servers
- Completely renewed software IEC subsystem
- Automatic per-title configuration files
- Improved USB mouse and keyboard support
- Support for larger cartridge images and Megabyter cartridges
- PDSID and SidKick daughterboard support
- New compatibility mode for timing-sensitive cartridges
- Significant networking, REST API and memory-management fixes
- FPGA-level timing fixes for DMA, REU and Ultimate Audio operation

## New machine-code monitor

A new built-in machine-code monitor allows you to inspect and modify C64 memory, assemble 6502 instructions and disassemble code directly on the Ultimate.

The monitor can be used from a USB keyboard, the C64 keyboard or through Telnet. It also includes memory transfer and relocation functions.

Available on Ultimate 64, Ultimate 64-II, Ultimate-II+ and Ultimate-II+L.

The original Ultimate-II does not include the monitor because of its more limited firmware flash capacity.

## REST API remote control and OpenAPI documentation

The REST API can now control the C64 keyboard and joysticks and can read back the contents of the Ultimate menu.

This makes it possible to automate much more of the machine, including entering commands, controlling software and navigating the Ultimate interface from external tools.

Keyboard and joystick injection are available on Ultimate 64 and Ultimate 64-II hardware.

The REST API now also comes with a generated **OpenAPI description**. This provides a machine-readable definition of the available REST endpoints, parameters and data structures and makes the interface much easier to explore and integrate.

For example, the OpenAPI file can be loaded into tools such as **Swagger Editor on swagger.io** to browse the available calls, inspect their parameters and experiment with the interface while developing software that communicates with the Ultimate.

## Ultimate Command Interface extensions

The Ultimate Command Interface has gained several new capabilities for software running on the C64:

- **Outbound HTTP requests** – C64 software can perform HTTP requests directly through the Ultimate.
- **Configuration loading** – software can immediately apply selected Ultimate settings from a configuration file.
- **IRQ completion signaling** – commands can signal completion through an interrupt instead of requiring continuous polling.
- **UCI unlock support** – cartridge software can enable the UCI directly.
- **Palette control** – programs can read, modify and restore the active C64 color palette at runtime.

Several UCI reply-handling and networking issues have also been fixed, including problems that could cause commands to hang.

## FTP client

The Ultimate can now connect to a remote FTP server and browse its contents alongside local storage and network shares.

The FTP client is available on Ultimate 64, Ultimate 64-II, Ultimate-II+ and Ultimate-II+L.

It is not available on the original Ultimate-II because of firmware flash limitations.

## Automatic per-title configuration

Disk images, tape images, cartridges and PRG files can now have their own configuration file.

When loading a D64, D71, D81, G64, G71, TAP, CRT or PRG, the firmware looks for a matching `.cfg` or `.usr` file and automatically applies the settings it contains.

This makes it possible to keep special cartridge, turbo or compatibility settings together with software that requires them.

Configuration files are also more tolerant of whitespace and of settings that are not available on the current hardware.

## Renewed software IEC subsystem

The software IEC implementation has been extensively rewritten, together with a new IEC status interface.

The new implementation improves compatibility with IEC devices and software, with particular attention to devices such as CMD-HD and SD2IEC.

## 1541/1571 drive emulation improvements

The 1541/1571 drive emulation gains a new **Track Twist** setting to compensate for GCR track-timing drift that can affect some software.

This is a drive-emulation timing correction and is independent of the software IEC rewrite.

Related fixes also ensure that track timing and length information is updated correctly for blank or absent tracks.

## USB mouse improvements

USB mouse handling now uses the mouse's HID report descriptor instead of relying mainly on basic boot-protocol behavior. This greatly expands compatibility with different USB mice.

Micromys wheel operation is also supported.

New mouse options include:

- Cursor, Mouse, Mouse+Cursor and Mouse+Wheel modes
- Sensitivity
- Adaptive acceleration
- Wheel sensitivity and direction
- Optional mouse navigation in the Ultimate menu

The firmware also shows the detected mouse and HID mode.

## USB keyboard improvements

USB keyboard auto-repeat now follows the actual report timing of the connected keyboard.

This fixes several cases where keys could appear to remain pressed, particularly when entering or leaving the Ultimate menu or when multiple USB keyboards are connected.

## Cartridge improvements

The available cartridge ROM area has been expanded from 1 MB to 4 MB on Ultimate 64 and Ultimate 64-II hardware.

Large multi-bank CRT images can therefore be loaded without exceeding the previous cartridge memory area.

Firmware 3.15 also adds support for Protovision **Megabyter** and **TwoMegabyter** cartridges, CRT types 86 and 87.

## PDSID and SidKick support

The firmware can now detect and configure **PDSID** and **SidKick** SID daughterboards installed in the SID socket.

Their configuration is integrated into the Ultimate menu.

A chip-selection problem affecting PDSID, where 6581 and 8580 selections were reversed, has also been fixed.

## New Compatibility bus mode

A new **Compatibility** setting has been added to Bus Operation Mode.

In this mode the C64 runs continuously at 1 MHz and every CPU cycle is exposed on the cartridge bus. This is intended for cartridges and hardware that depend on traditional C64 bus timing.

Bus Operation Mode changes now take effect immediately without requiring a restart.

## File browser and interface improvements

The built-in file viewer can now display files in hexadecimal form, making it easier to inspect binary files directly on the Ultimate.

File-browser windows now refresh when files are changed outside the current browser view.

Temporary files created by REST uploads and other operations are automatically cleaned up instead of accumulating in `/Temp`.

The web interface now includes a persistent dark theme, with improved Firefox compatibility.

A global master-volume control has also been added to the audio mixer.

## Ultimate 64-II power management

Ultimate 64-II gains configurable power-on behavior. After power is restored, the machine can remain switched off, switch on automatically or return to its previous power state.

Wake-on-LAN is also available through Wi-Fi, allowing a powered-off Ultimate 64-II to be started using a network magic packet.

These features are specific to Ultimate 64-II.

## Remote web player improvements

The standalone browser player can now mount dropped D64, D71 and D81 images directly into drive A.

On Ultimate 64-II it also shows the firmware version and provides a power-off button.

Several Live Monitor display and command-parsing issues have also been corrected.

## Network reliability and security

Firmware 3.15 contains a substantial reliability pass across HTTP, REST, FTP, Telnet and UDP services.

Stalled network sessions are cleaned up automatically, FTP and Telnet sessions now have sensible limits and timeouts, abandoned sockets are correctly closed, and large UDP packets are returned completely.

Malformed HTTP and REST requests are handled more safely, aborted uploads release their resources correctly, and several memory leaks and buffer-handling problems have been fixed.

Network services such as Telnet, FTP and HTTP now also start or stop immediately when changed in the configuration menu, without requiring a reboot.

Wi-Fi now automatically reconnects after losing its access point.

## Stability and memory fixes

Several memory leaks in the REST API, file browser, disk-image handling and Assembly 64 browser have been fixed.

REST memory operations now fail cleanly when insufficient memory is available instead of potentially hanging the Ultimate.

Loading long PRG filenames can no longer overflow the boot cartridge's filename buffer.

Large cartridge memory is also completely cleared when loading another cartridge, preventing data from a previously loaded image from remaining visible.

## Drive, REU and FPGA timing fixes

A number of lower-level timing problems have been corrected:

- REU transfers started while the CPU is running in turbo mode no longer risk returning stale data.
- VIC-II badline and external-DMA timing has been corrected.
- Cartridge-port DMA read/write timing has been improved.
- A hardware tag conflict between USB devices and Ultimate Audio has been fixed.
- The RISC-V processor used inside several Ultimate models now correctly accepts the `FENCE` instruction instead of becoming stuck.

These changes improve compatibility and stability without requiring changes to existing software.

## Other fixes

Firmware 3.15 also fixes virtual printer crashes with certain output filenames, a virtual modem busy-notification problem, incorrect UCI reply lengths for REU and SoftIEC commands, configuration values being unnecessarily reapplied during startup, and several web-interface display problems.

Composite and RF chroma output has also been increased, providing a stronger color signal on those analog outputs.

## Ultimate 64-II hardware support

Firmware 3.15 supports Ultimate 64-II boards using both the original 50T FPGA and the larger 100T FPGA variant.

Recovery scripts are also included for restoring an Ultimate 64-II through FT232H JTAG if the normal firmware cannot boot.

## Note for Ultimate-II owners

Firmware size on the original Ultimate-II has reached the limit of its available flash memory.

To keep firmware 3.15 available for this platform, the **machine-code monitor and FTP client are not included in the Ultimate-II build**.

All other supported Ultimate platforms retain these features.

## Summary

Firmware 3.15 brings a substantial set of new capabilities to the Ultimate family, particularly for remote control, software integration and hardware compatibility.

The new REST controls, OpenAPI description and expanded UCI make the Ultimate considerably easier to automate and integrate with external tools as well as software running directly on the C64.

At the same time, a large number of fixes improve USB input, networking, file handling, 1541/1571 drive emulation, cartridge operation and low-level hardware timing.

For everyday users, the biggest improvements are broader hardware compatibility, easier per-title configuration and a more robust system overall.
