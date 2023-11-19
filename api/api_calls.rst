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
.. list-table:: Runners
   :widths: 20 40 40
   :header-rows: 1

   * - URL
     - Arguments
     - Action
   * - ``PUT /v1/runners:sidplay``
     - | *file*: Path to existing file in the file system of the Ultimate
       | *[songnr]*: Requested song number
     - This command requests the Ultimate to play a SID file. It plays the default song, unless the optional *songnr* argument is given.
   * - ``POST /v1/runners:sidplay``
     - *[songnr]*: Requested song number
     - This command requests the Ultimate to play a SID file that is attached as a file to the request. It plays the default song,
       unless the optional *songnr* argument is given.
       An optional second attachment can be sent that contains the song lengths.
   * - ``PUT /v1/runners:modplay``
     - *file*: Path to existing file in the file system of the Ultimate
     - This command requests the Ultimate to play an Amiga MOD file.
   * - ``POST /v1/runners:modplay``
     -
     - This command requests the Ultimate to play the Amiga MOD file that is attached as a file to the request.
   * - ``PUT /v1/runners:load_prg``
     - *file*: Path to existing file in the file system of the Ultimate
     - With this command a progam can be loaded into memory. The machine resets, and loads the designated program into memory
       using DMA. It does not automatically run the program.
   * - ``POST /v1/runners:load_prg``
     - 
     - With this command a progam can be loaded into memory. The machine resets, and loads the attached program into memory
       using DMA. It does not automatically run the program.
   * - ``PUT /v1/runners:run_prg``
     - *file*: Path to existing file in the file system of the Ultimate
     - With this command a progam can be loaded into memory. The machine resets, and loads the designated program into memory
       using DMA. Then it automatically runs the program.
   * - ``POST /v1/runners:run_prg``
     - 
     - With this command a progam can be loaded into memory. The machine resets, and loads the attached program into memory
       using DMA. Then it automatically runs the program.
   * - ``PUT /v1/runners:run_crt``
     - *file*: Path to existing file in the file system of the Ultimate
     - With this command a cartridge file can be started. The 'file' parameter points to an existing file. The machine
       resets, with the specified cartridge active. It does not alter the configuration of the Ultimate.
   * - ``POST /v1/runners:run_crt``
     - 
     - This command starts a supplied cartridge file. The 'crt' file is attached to the POST request. The machine
       resets, with the attached cartridge active. It does not alter the configuration of the Ultimate.





API_CALL(PUT, runners, modplay, NULL, ARRAY( { { "file", P_REQUIRED } }))
API_CALL(POST, runners, modplay, &attachment_reu, ARRAY( { }))
API_CALL(GET, configs, none, NULL, ARRAY ( { } ))
API_CALL(PUT, configs, none, NULL, ARRAY ( { {"value", P_REQUIRED }} ))
API_CALL(POST, configs, none, &attachment_writer, ARRAY ( { } ))
API_CALL(PUT, configs, load_from_flash, NULL, ARRAY ( {  } ))
API_CALL(PUT, configs, save_to_flash, NULL, ARRAY ( {  } ))
API_CALL(PUT, configs, reset_to_default, NULL, ARRAY ( {  } ))
API_CALL(GET, files, info, NULL, ARRAY({ }))
API_CALL(PUT, files, create_d64, NULL, ARRAY( { { "tracks", P_OPTIONAL }, { "diskname", P_OPTIONAL } } ))
API_CALL(PUT, files, create_d71, NULL, ARRAY( { { "diskname", P_OPTIONAL } } ))
API_CALL(PUT, files, create_d81, NULL, ARRAY( { { "diskname", P_OPTIONAL } } ))
API_CALL(PUT, files, create_dnp, NULL, ARRAY( { { "tracks", P_REQUIRED }, { "diskname", P_OPTIONAL } } ))
API_CALL(PUT, machine, reset, NULL, ARRAY( {  }))
API_CALL(PUT, machine, reboot, NULL, ARRAY( {  }))
API_CALL(PUT, machine, pause, NULL, ARRAY( {  }))
API_CALL(PUT, machine, resume, NULL, ARRAY( {  }))
API_CALL(PUT, machine, poweroff, NULL, ARRAY( {  }))
API_CALL(PUT, machine, writemem, NULL, ARRAY( { {"address", P_REQUIRED}, {"data", P_REQUIRED} }))
API_CALL(POST, machine, writemem, &attachment_writer, ARRAY( { {"address", P_REQUIRED} }))
API_CALL(GET, machine, readmem, NULL, ARRAY( { {"address", P_REQUIRED}, {"length", P_OPTIONAL} }))
API_CALL(GET, help, none, NULL, ARRAY({{"command", P_REQUIRED}}))
API_CALL(GET, version, none, NULL, ARRAY( { }))
API_CALL(GET, drives, none, NULL, ARRAY({ }))
API_CALL(PUT, drives, mount, NULL, ARRAY({{ "image", P_REQUIRED }, { "type", P_OPTIONAL }, { "mode", P_OPTIONAL } }))
API_CALL(POST, drives, mount, &attachment_writer, ARRAY({ { "type", P_OPTIONAL }, { "mode", P_OPTIONAL } }))
API_CALL(PUT, drives, reset, NULL, ARRAY({ }))
API_CALL(PUT, drives, remove, NULL, ARRAY({ }))
API_CALL(PUT, drives, on, NULL, ARRAY({ }))
API_CALL(PUT, drives, off, NULL, ARRAY({ }))
API_CALL(PUT, drives, unlink, NULL, ARRAY({ }))
API_CALL(PUT, drives, load_rom, NULL, ARRAY({{ "file", P_REQUIRED }}))
API_CALL(POST, drives, load_rom, &attachment_writer, ARRAY({ }))
API_CALL(PUT, drives, set_mode, NULL, ARRAY({{ "mode", P_REQUIRED }}))
API_CALL(help, empty, "This function is supposed to help you.", ARRAY({{"command", P_REQUIRED}, P_END}))
API_CALL(files, createDiskImage, "Create a disk image", ARRAY({{"type", P_REQUIRED}, {"format", P_OPTIONAL}, P_END }))
