OpenAPI Specification
=====================

The REST API is also available as an OpenAPI 3.1 document:

:download:`Download rest_api_openapi.yaml <rest_api_openapi.yaml>`

The specification covers the Ultimate REST API for U64 and U2-family devices. It is based on the firmware REST API reference.

Why this is useful
------------------

YAML-based OpenAPI documentation is useful because it is both documentation and a machine-readable contract:

- Client libraries can be generated from it, reducing hand-written HTTP wrapper code.
- Test suites can validate that request and response shapes still match the documented firmware contract.
- Mock servers can use it to emulate the REST API during application development when no Ultimate device is available.
- API explorers and documentation tools can render it as an interactive reference.
- The exact path, method, parameter, request body, response body, header, and error shapes are kept in one structured file.
- Changes to the REST API can be reviewed as precise schema diffs, which makes omissions and incompatible changes easier to spot than in prose alone.
