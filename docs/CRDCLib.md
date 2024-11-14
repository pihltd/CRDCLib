# CRDCStuff
**A collection of random bits and bobs I use when working on CRDC projects**
## Required Python libraries
- requests
- yaml
- json
- re
- os
## Modules
### readYAML
- **Usage:** readYAML(yamlfile)
- **Description:** takes a yamlfile path as an argument, returns a JSON object of the file
- **Parameters**
-- *yamlfile*: Full path to a valid yaml file
- **Returns**
-- A JSON object/Python Dictionary from the provided YAML file

### writeYAML
- **Usage:** writeYAML(filename, json_object)
- **Description:** Takes a filename and a json object like a Python dictionary and writes a yaml file
- **Parameters**
-- *filename*: Full path to a file that will be used to write
-- *json_object*: A JSON object (like a Python dictionary) that will be converted to YAML and written to *filename*
- **Returns**
-- Not applicable

### getCDERecord
- **Usage:** getCDERecord(cde_id, cde_version)
- **Description:** Takes a CDE public ID and optional version and returns the full caDSR record.  If no version is provided, returns the latest version
- **Parameters**
-- *cde_id*: The caDSR public identifier for a CDE (Common Data Element)
-- *cde_version*: **OPTIONAL** The version number for the CDE
- **Returns**
-- If the query is successful (status code 200), the full JSON record from caDSR for the CDE and version.  The latest version is returned if no version number was supplied
-- If the query is unsuccessful (status code not 200), a string with the status code and error message
-- If HTTP eexception, the requests HTTPError object

### cleanSting
- **Usage:** cleanString(inputstring, leavewhitespace = False):
- **Description:** Removes non-ASCII and whitespaces characters from the inputstring.
- **Parameters**
-- *inputstring*: The string to be cleaned
-- *leavewhitespace* **Optional** Accepted values True/False (default is False).  If set to True, whitespace is left
- **Returns**
-- The original string with all non-ASCII characters and (optionally) all whitespace removed

### dhApiQuery
- **Usage:** dhApiQuery(url, apitoken, query, variables = None)
- **Description:** A method to run GraphQL queries and mutations against the Data Hub Submission Portal APIs.
- **Parameters**
-- *url* The Data Hub Submisison Portal API endpoint
-- *apitoken* The Data Hub API access token.
-- *query* The GraphQL query
-- *variables* **Optional**  The variables used in the query, if any.
- **Returns**
-- If query is successful (status code 200), a JSON object containing the elements specified in the query
-- If the query is unsuccessful (status code not 200), a string with the status code and error message
-- If HTTP eexception, the requests HTTPError object

### dhAPICreds
- **Usage:** dhAPICreds(tier)
- **Description:** A method to get the Data Hub API URL and API Crendentials
- **Parameters**
-- *tier*  The tier for which the URL and credentials should be returned.  Allowed values are 'prod', 'stage', 'qa', 'qa2', 'dev', 'dev2'
- **Returns**
-- A dictionary {'url': requested ULR, 'token': bearer token}