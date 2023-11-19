REST API Calls
==============

Starting from Ultimate firmware 3.11, the application supports API calls by means of the HTTP protocol. This simplifies the integration of remote control
functionality in external applications, as it follows a well defined standard.

The format of the URL is as follows:

``/v1/<route>/<path>:<command>?<arguments>``

The 'verb' depends on the kind od operation. In general:

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

* - Verb
  - Meaning
* - GET
  - Retrieves information without changing state
* - PUT
  - Sends information, or performs an action, using the information in the URL or in a file referenced by the URL.
* - POST
  - Perform an action using the information that is attached to the request.


Route 'runners'
---------------


~~~~~~~~~~~~~~~~~~~
===================== =========== ================================ =============================================
URL                   Verb        Arguments                        Action
===================== =========== ================================ =============================================
/v1/runners/sidplay   PUT         file: Path to existing file      This command requests the Ultimate to play
                                  [songnr]: Requested song number  a SID file. It plays the default song,
                                                                   unless the [songnr] argument is given.
--------------------- ----------- -------------------------------- ---------------------------------------------
/v1/runners/sidplay   POST        [songnr]: Requested song number  This command requests the Ultimate to play
                                                                   the SID file that is attached to the request.
                                                                   It plays the default song, unless the
                                                                   [songnr] argument is given. An optional
                                                                   second attachment can be sent with the song
                                                                   lengths.
===================== =========== ================================ =============================================





API_CALL(PUT, runners, sidplay, NULL, ARRAY( { { "file", P_REQUIRED }, { "songnr", P_OPTIONAL } }))
API_CALL(POST, runners, sidplay, &attachment_writer, ARRAY( { { "songnr", P_OPTIONAL } }))
API_CALL(PUT, runners, load_prg, NULL, ARRAY( { { "file", P_REQUIRED } }))
API_CALL(PUT, runners, run_prg, NULL, ARRAY( { { "file", P_REQUIRED } }))
API_CALL(POST, runners, load_prg, &attachment_writer, ARRAY( { }))
API_CALL(POST, runners, run_prg, &attachment_writer, ARRAY( { }))
API_CALL(PUT, runners, run_crt, NULL, ARRAY( { { "file", P_REQUIRED } }))
API_CALL(POST, runners, run_crt, &attachment_writer, ARRAY( { }))
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
