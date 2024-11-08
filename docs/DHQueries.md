# Data Hub Sumbmission API Queries

## create_batch_query: A mutation to create a new batch
### Parameters
- submissionID:  The submission ID the batch will be under
-- datatype: ID object
- type: The type of submission.
-- Allowed Values
--- metadata
--- data file  **(not used outside of the CLI Upload Tool)**
-- datatype: String
- file: A list of dictionarys with file names and sizes.  Ex. [{'fileName': 'PDXNet_diagnosis.tsv', 'size': 6439}]
### Returns
- A JSON object wtih the requested fields
-- datatype: dictionary

## list_sub_query: A qeury that will list all the submissions visible
### Parameters
- status: The status of the submissions to be returned.  
-- Allowed values: 
--- All
--- New
--- In Progress
--- Submitted
--- Released
--- Completed
--- Archived
--- Canceled
--- Rejected
--- Withdrawn
--- Deleted 
--datatype: String
### Returns
- A JSON object with the requested fields
-- datatype: dictionary

## create_submission_query: A mutation that creates a new submission.
### Parameters
- studyID: The Study ID the submission will be located under
-- datatype: String
- dbGaPID: The dbGaP identifier (phs nubmer) associated with the study
-- datatype: String
- dataCommons: The destination data commons.  
-- Allowed values
--- CDS
--- CTDC
--- ICDC
-- datatype: String
- name: A user generated name for the submission
-- datatype: String
-  intention: The purpose of the submission.  
-- Allowed values 
--- New/Update
--- Delete
-- datatypen: String
- dataType: The kind of submission.  
--Allowed values
--- Metadata Only
--- Metadata and Data Files
-- datatype: String
### Returns
- A JSON object with the requested fields
-- datatype: dictionary

## org_query: A query that returns a list of the studies associated with your organization.  
- No parameters.

## qc_check_query: A query that returns a list of all validation errors
### Parameters
- id: The submission id for the submission that was validated
-- datatype: ID
- severities: The severity of the errors. 
-- Allowed values 
--- All
--- Error
--- Warnings
-- datatype: String
-  first: The number of records to return, used for pagination
-- datatype: Int
- offset: The number of records to offset, used for pagination
-- datatype: Int
"""