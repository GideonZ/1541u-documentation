REST API Calls
==============

Starting from Ultimate firmware 3.11, the application supports API calls by means of the HTTP protocol. This simplifies the integration of remote control
functionality in external applications, as it follows a well defined standard.

The format of the URL is as follows:

``/v1/<route>/<path>:<command>?<arguments>``

The 'verb' depends on the kind of operation. In general:

.. list-table:: URL Verbs
   :widths: 10 50
   :header-rows: 1

   * - Verb
     - Meaning
   * - GET
     - Retrieves information without changing state
   * - PUT
     - Sends information, or performs an action, using the information in the URL or in a file referenced by the URL.
   * - POST
     - Perform an action using the information that is attached to the request.

What is returned with the request depends on the command. In most cases the command returns a valid JSON message, using
the *Content-Type: application/json* string in the header. The JSON contains at least one entry, called *errors*. This is
a list (array) of strings with things that went wrong during the execution of the command. A complete response could, for
instance, look like this:

.. code-block::

  HTTP/1.1 200 OK
  Connection: close
  Content-Type: application/json
  Content-Length: 22
   
  {
    "errors": []
  }



Routes
------

About
~~~~~
.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - URL
     - Parameters
     - Action
   * - ``GET /v1/version``
     - 
     - Returns the current version of the ReST API:
       .. code-block::
        {
            "version": "0.1",
            "errors": []
        }


Runners
~~~~~~~

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - URL
     - Parameters
     - Action
   * - ``PUT /v1/runners:sidplay``
     - | *file*
       | *[songnr]*
     - This command requests the Ultimate to play a SID file. The *file* argument points to an existing file in the file system of the Ultimate.
       It plays the default song, unless the optional *songnr* argument is given. The player will attempt to open the song lengths file in the
       subdirectory 'SONGLENGTHS'.
   * - ``POST /v1/runners:sidplay``
     - *[songnr]*
     - This command requests the Ultimate to play a SID file that is attached as a file to the request. It plays the default song,
       unless the optional *songnr* argument is given. An optional second attachment can be sent that contains the song lengths.
   * - ``PUT /v1/runners:modplay``
     - *file*
     - This command requests the Ultimate to play an Amiga MOD file. The *file* argument points to an existing file in the file system of the Ultimate.
   * - ``POST /v1/runners:modplay``
     -
     - This command requests the Ultimate to play the Amiga MOD file that is attached as a file to the request.
   * - ``PUT /v1/runners:load_prg``
     - *file*
     - With this command a progam can be loaded into memory. The *file* argument points to an existing file in the file system of the Ultimate.
       The machine resets, and loads the designated program into memory using DMA. It does not automatically run the program.
   * - ``POST /v1/runners:load_prg``
     - 
     - With this command a progam can be loaded into memory. The machine resets, and loads the attached program into memory
       using DMA. It does not automatically run the program.
   * - ``PUT /v1/runners:run_prg``
     - *file*
     - With this command a progam can be loaded into memory. The *file* argument points to an existing file in the file system of the Ultimate.
       The machine resets, and loads the designated program into memory using DMA. Then it automatically runs the program.
   * - ``POST /v1/runners:run_prg``
     - 
     - With this command a progam can be loaded into memory. The machine resets, and loads the attached program into memory
       using DMA. Then it automatically runs the program.
   * - ``PUT /v1/runners:run_crt``
     - *file*
     - With this command a cartridge file can be started. The *file* argument points to an existing file in the file system of the Ultimate.
       The machine resets, with the specified cartridge active. It does not alter the configuration of the Ultimate.
   * - ``POST /v1/runners:run_crt``
     - 
     - This command starts a supplied cartridge file. The 'crt' file is attached to the POST request. The machine
       resets, with the attached cartridge active. It does not alter the configuration of the Ultimate.

Configuration
~~~~~~~~~~~~~

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - URL
     - Parameters
     - Action
   * - ``GET /v1/configs``
     - 
     - This command obtains a list of all the configuration categories in the Ultimate application. Note that there
       is no path specified after 'configs'. An example result is:
       .. code-block::
          HTTP/1.1 200 OK
          Connection: close
          Content-Type: application/json
          Content-Length: 405
          
          {
            "categories": [
              "Audio Mixer",
              "SID Sockets Configuration",
              "UltiSID Configuration",
              "SID Addressing",
              "C64 and Cartridge Settings",
              "U64 Specific Settings",
              "Clock Settings",
              "Network settings",
              "WiFi settings",
              "Modem Settings",
              "LED Strip Settings",
              "Data Streams",
              "Software IEC Settings",
              "User Interface Settings",
              "Tape Settings",
              "Drive A Settings",
              "Drive B Settings"
            ],
            "errors": []
          }        

   * - ``GET /v1/configs/<category>``
     - 
     - This command obtains a list of all the configuration items in the category specified in the URL.
       Wildcards are allowed. Note that the depth of the specified path is 1. It specifies the category.
       Example: ``GET /v1/configs/drive%20a*`` results in:
       .. code-block::
           HTTP/1.1 200 OK
           Connection: close
           Content-Type: application/json
           Content-Length: 414
           
           {
             "Drive A Settings": {
               "Drive": "Enabled",
               "Drive Type": "1541",
               "Drive Bus ID": 8,
               "ROM for 1541 mode": "1541.rom",
               "ROM for 1571 mode": "1571.rom",
               "ROM for 1581 mode": "1581.rom",
               "Extra RAM": "Disabled",
               "Disk swap delay": 1,
               "Resets when C64 resets": "Yes",
               "Freezes in menu": "Yes",
               "GCR Save Align Tracks": "Yes",
               "Leave Menu on Mount": "Yes"
             },
             "errors": []
           }
 
   * - ``GET /v1/configs/<category>/<item>``
     - 
     - This command returns information about the specific item(s). Wildcards are allowed. Note that the depth
       of the path is 2. Both the category as well as the item is specified.
       Example: ``GET /v1/configs/drive%20a*/*bus*`` results in: .. code-block::
         HTTP/1.1 200 OK
         Connection: close
         Content-Type: application/json
         Content-Length: 154
         
         {
           "Drive A Settings": {
             "Drive Bus ID": {
               "current": 8,
               "min": 8,
               "max": 11,
               "format": "%d",
               "default": 8
             }
           },
           "errors": []
         }

   * - ``PUT /v1/configs/<category>/<item>``
     - *value*
     - | This command sets a specific configuration item to the value specified in the URL, using the *value* argument.
         It is required to specify the full path to the item, although wildcards are allowed.
       | Example: ``PUT /v1/configs/drive%20a*/*bus*?value=9`` will set the 'Drive Bus ID' of 'Drive A Settings' to 9.

   * - ``POST /v1/configs``
     - 
     - With this command, many configuration settings can be changed at once. The format of the data that is passed should be JSON.
       It follows the same format as what is returned with the GET verb with at least one level in the path. The JSON should
       be an object, with the category strings at its first level, the configuration items in the second level, followed by the value.
       For instance:
       .. code-block::
         POST http://192.168.178.232/v1/configs
         Content-Type: application/json
 
         {
           "Drive A Settings": {
             "Drive": "Enabled",
             "Drive Type": "1581",
             "Drive Bus ID": 8
           },
           "Drive B Settings": {
             "Drive": "Disabled"
           } 
         }          
        
   * - ``PUT /v1/configs:load_from_flash``
     - 
     - With this command, the complete configuration is restored to what is currently written in non-volatile memory.
       In other words: the 'saved' values are loaded into the current configuration.
   * - ``PUT /v1/configs:save_to_flash``
     - 
     - With this command, the complete configuration is written to non-volatile memory.
       In other words: the current configuration settings are 'saved' and will be loaded once the machine boots.
   * - ``PUT /v1/configs:reset_to_default``
     - 
     - This command resets the current settings to the factory default. This does *not* clear or reset the values
       stored in non-volatile memory.

Machine
~~~~~~~

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - URL
     - Parameters
     - Action
   * - ``PUT /v1/machine:reset``
     -
     - This command sends a reset to the machine. The current configuration is not changed.
   * - ``PUT /v1/machine:reboot``
     -
     - This command restarts the machine. It re-initializes the cartridge configuration and sends a reset to the machine.
   * - ``PUT /v1/machine:pause``
     -
     - When issuing this command, the machine is paused by pulling the DMA line low at a safe moment. This stops the CPU. Note that this does not stop any timers.
   * - ``PUT /v1/machine:resume``
     -
     - With this command, the machine is resumed from the paused state. The DMA line is released and the CPU will continue where it left off.
   * - ``PUT /v1/machine:poweroff``
     -
     - This U64-only command causes the machine to power off. Note that it is likely that you won't receive a valid response.
   * - ``PUT /v1/machine:writemem``
     - | *address*
       | *data*
     - | With this command, data can be written to C64 memory. To be more exact: this command writes data through DMA, so the
         memory map that is currently selected is used. Writing to the I/O registers of the 6510 is not possible.
       | Data bytes are written in consequetive memory locations. 
         The *address* argument specifies the memory location in hexadecimal format. The *data* argument contains a string of bytes
         in hexadecimal format. The maxmimum number of bytes written with this method is 128.
       | Example: ``PUT /v1/machine:writemem?address=D020&data=0504``
       | This results in 05 being written to $D020 and 04 being written to $D021. In other words: the border will be green and the
         main screen will turn purple.
   * - ``POST /v1/machine:writemem``
     - *address*
     - | With this command, data can be written to C64 memory. The data, passed as a binary attachment, will be written to
         memory starting from the location indicated by the *address* argument, which shall be formatted in hexadecimal.
         The data should not wrap around $FFFF.
   * - ``GET /v1/machine:readmem``
     - | *address*
       | *[length]*
     - This command performs a DMA read action on the cartridge bus and returns the result as a binary attachment.
       The *address* argument specifies the memory location in hexadecimal format. The optional
       argument *length* specifies the number of bytes being read. When not specified, 256 bytes are returned.
   * - ``GET /v1/machine:debugreg``
     -
     - This command reads the debug register ($D7FF) and returns it in the "value" field of the JSON response. The value is in
       hexadecimal format. *This is currently an U64-only call.*
   * - ``PUT /v1/machine:debugreg``
     - *value*
     - This command writes the value specified by the *value* argument (in hexadecimal) into the debug register ($D7FF), and 
       then reads the debug register ($D7FF) and returns it in the "value" field of the JSON response. *This is currently an U64-only call.*
    
Floppy Drives
~~~~~~~~~~~~~

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - URL
     - Parameters
     - Action
   * - ``GET /v1/drives``
     - 
     - With this command, the information about all the (internal) drives on the IEC bus is returned. In addition to the presence,
       it also shows the image files and paths of the mounted disks or referenced paths. An example follows:
       .. code-block::
         {
            "drives":[
               {
                  "a":{
                     "enabled":true,
                     "bus_id":8,
                     "type":"1581",
                     "rom":"1581.rom",
                     "image_file":"",
                     "image_path":""
                  }
               },
               {
                  "b":{
                     "enabled":false,
                     "bus_id":9,
                     "type":"1541",
                     "rom":"1541.rom",
                     "image_file":"",
                     "image_path":""
                  }
               },
               {
                  "softiec":{
                     "enabled":false,
                     "bus_id":11,
                     "type":"DOS emulation",
                     "last_error":"73,U64IEC ULTIMATE DOS V1.1,00,00",
                     "partitions":[
                        {
                           "id":0,
                           "path":"/Temp/"
                        }
                     ]
                  }
               }
            ],
            "errors":[
               
            ]
         }
   * - ``PUT /v1/drives/<drive>:mount``
     - | *image*
       | *[type]*
       | *[mode]*
     - This command can be used to mount an existing image onto the drive specified in the path. The *image* argument
       points to the file in the file system of the Ultimate. The optional *type* argument specifies the type of the
       image, and could be one of the following: **d64**, **g64**, **d71**, **g71** or **d81**. If this argument is omitted, it will use
       the file extension of the file specified. The optional *mode* argument can be one of the following: **readwrite**,
       **readonly** or **unlinked**. In *readwrite* mode, the drive can write to the image file; in *readonly* mode the
       disk is write protected and in *unlinked* mode the disk is not write protected, but the changes are not written
       back to the disk image.
   * - ``POST /v1/drives/<drive>:mount``
     - | *[type]*
       | *[mode]*
     - This command can be used to mount a disk image that is sent along as an attachment onto drive specified in the path.
       The optional *type* argument specifies the type of the image, and could be one of the following: **d64**, **g64**, **d71**, **g71** or **d81**.
       If this argument is omitted, it will use the file extension of the file that was uploaded, if this name
       is given in the Content-Deposition. The optional *mode* argument can be one of the following: **readwrite**,
       **readonly** or **unlinked**. In *readwrite* mode, the drive can write to the image file; in *readonly* mode the
       disk is write protected and in *unlinked* mode the disk is not write protected, but the changes are not written
       back to the disk image.
   * - ``PUT /v1/drives/<drive>:reset``
     - 
     - Issuing this command causes the selected drive to be reset.
   * - ``PUT /v1/drives/<drive>:remove``
     - 
     - With this command the mounted disk can be removed from the drive. 
   * - ``PUT /v1/drives/<drive>:remove``
     - 
     - Use this command to break the link between the drive and the mounted disk image file. Further writes will no longer
       be reflected in the image file.
   * - ``PUT /v1/drives/<drive>:on``
     - 
     - This command turns on the selected drive. When the drive was already on it is reset.
   * - ``PUT /v1/drives/<drive>:off``
     - 
     - This command turns the selected drive off. It will no longer be accessible on the serial bus.
   * - ``PUT /v1/drives/<drive>:load_rom``
     - *file*
     - With this command a new drive ROM can be loaded into the selected drive. The *file* argument points to a file
       that is already present on the file system of the Ultimate. The size of the ROM file needs to be 16K or 32K,
       depending on the drive type. Loading the ROM is a temporary action, setting the drive type or rebooting the machine will load the default ROM.
   * - ``POST /v1/drives/<drive>:load_rom``
     - 
     - With this command a new drive ROM can be loaded into the selected drive. The ROM file is passed as a binary file
       attachment to the POST request. The size of the ROM file needs to be 16K or 32K,
       depending on the drive type. Loading the ROM is a temporary action, setting the drive type or rebooting the machine will load the default ROM.
   * - ``PUT /v1/drives/<drive>:set_mode``
     - *mode*
     - By sending this command, the drive mode is changed. The available values for the *mode* argument are **1541**, **1571** and **1581**.
       Note that this command will also load the drive ROM. A temporary ROM that was loaded with the 'load_rom' command will be lost.

Data Streams (U64 only)
~~~~~~~~~~~~~~~~~~~~~~~

The U64 supports streaming video and audio over its LAN port. The following API commands are available to control these streams.

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - URL
     - Parameters
     - Action
   * - ``PUT /v1/streams/<stream name>:start``
     - | *ip*
     - Use this command to start one of the available streams. Valid stream names are **video**, **audio** and **debug**.
       The IP number parameter is required for the U64 to know where to send the stream to. The default port number that the
       data stream is sent to is 11000 for the video stream, 11001 for the audio stream and 11002 for the debug stream. A
       custom port number can be added to the IP address, after a colon separator; e.g. *192.168.178.224:6789* .
       Note that turning on the video stream will automatically turn off the debug stream. 
   * - ``PUT /v1/streams/<stream name>:stop``
     - 
     - With this command a data stream can be turned off. Valid stream names are **video**, **audio** and **debug**.


File Manipulation
~~~~~~~~~~~~~~~~~

This section lists the API commands for file manipulation. This is the current state of V3.11 alpha. It is not yet finished.

.. list-table::
   :widths: 25 10 65
   :header-rows: 1

   * - URL
     - Parameters
     - Action
   * - ``GET /v1/files/<path>:info``
     -
     - This command returns basic information about a file, like size and extension. It simply performs an 'fstat'. Supports wildcards. *Unfinished*
   * - ``PUT /v1/files/<path>:create_d64``
     - | *[tracks]*
       | *[diskname]*
     - With this command a .d64 file can be created. The full path shall be specified from the root of the file system, including the file
       to be created. The default number of tracks is 35, but it can also be set to 40. The optional *diskname* argument overrides the name
       to be used in the header of the disk. When not given, it is taken from the name of the file that is being created.
   * - ``PUT /v1/files/<path>:create_d71``
     - *[diskname]*
     - With this command a .d71 file can be created. The full path shall be specified from the root of the file system, including the file
       to be created. The number of tracks is fixed at 70. The optional *diskname* argument overrides the name
       to be used in the header of the disk. When not given, it is taken from the name of the file that is being created.
   * - ``PUT /v1/files/<path>:create_d81``
     - *[diskname]*
     - With this command a .d81 file can be created. The full path shall be specified from the root of the file system, including the file
       to be created. The number of tracks is fixed at 160 (80 on each side). The optional *diskname* argument overrides the name
       to be used in the header of the disk. When not given, it is taken from the name of the file that is being created.
   * - ``PUT /v1/files/<path>:create_dnp``
     - | *tracks*
       | *[diskname]*
     - With this command a .dnp file can be created. The full path shall be specified from the root of the file system, including the file
       to be created. The number of tracks is a required argument to this function. Each track will have 256 sectors. The maximum number of
       tracks is 255, which makes the maximum DNP size almost 16 Megabytes. The optional *diskname* argument overrides the name
       to be used in the header of the disk. When not given, it is taken from the name of the file that is being created.

