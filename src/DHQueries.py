"""
create_batch_query: A mutation to create a new batch
:param submissionID:  The submission ID the batch will be under
:type submissionID: ID object
:param type: The type of submission.  Valid values are 'metadata' or 'data file'.  'data file' is not used outside of the CLI Upload tool
:type type: String
:param file: A list of dictionarys with file names and sizes.  Ex. [{'fileName': 'PDXNet_diagnosis.tsv', 'size': 6439}]
:return: A JSON object wtih the requested fields
:rtype: dictionary
"""
create_batch_query = """
mutation CreateBatch(
    $submissionID: ID!, 
    $type: String!, 
    $file: [FileInput]) {
  createBatch(submissionID: $submissionID, type: $type, files: $file) {
    _id
    files {
      fileName
      signedURL
    }
  }
}
"""

"""
list_sub_query: A qeury that will list all the submissions visible
:param status: The status of the submissions to be returned.  Allowed values: 
- All
- New
- In Progress
- Submitted
- Released
- Completed
- Archived
- Canceled
- Rejected
- Withdrawn
- Deleted 
:type status: String
:return: A JSON object with the requested fields
:rtype: dictionary
"""
list_sub_query = """
query ListSubmissions($status: String!){
  listSubmissions(status: $status){
    submissions{
      _id
      name
      submitterID
      submitterName
      studyAbbreviation
      studyID
      dbGaPID
      createdAt
      updatedAt
      metadataValidationStatus
      fileValidationStatus
      status
    }
  }
}
"""

"""
create_submission_query: A mutation that creates a new submission.
:param studyID: The Study ID the submission will be located under
:type studyID: String
:param dbGaPID: The dbGaP identifier (phs nubmer) associated with the study
:type dbGaPID: String
:param dataCommons: The destination data commons.  Allowed values are "CDS", "CTDC", "ICDC"
:type dataCommons: String
:param name: A user generated name for the submission
:type name: String
:param intention: The purpose of the submission.  Allowed values are "New/Update" and "Delete"
:type intention: String
:param dataType: The kind of submission.  Allowed values are "Metadata Only" and "Metadata and Data Files"
:type: String
:return: A JSON object with the requested fields
:rtype: dictionary
"""
create_submission_query = """
mutation CreateNewSubmission(
  $studyID: String!,
  $dbGaPID: String!,
  $dataCommons: String!,
  $name: String!,
  $intention:String!,
  $dataType: String!,
){
  createSubmission(
    studyID: $studyID,
    dbGaPID: $dbGaPID,
    dataCommons: $dataCommons,
    name: $name,
    intention: $intention,
    dataType: $dataType
  ){
    _id
    studyID
    dbGaPID
    dataCommons
    name
    intention
    dataType
    status
  }
}"""

"""
org_query: A query that returns a list of the studies associated with your organization.  No parameters.
"""
org_query = """
{
  listApprovedStudiesOfMyOrganization{
    originalOrg
    dbGaPID
    studyAbbreviation
    studyName
    _id
  }
}
"""

"""
qc_check_query: A query that returns a list of all validation errors
:param id: The submission id for the submission that was validated
:type id: ID
:param severities: The severity of the errors. Allowed values are "All", "Error", and "Warnings"
:type severities: String
:param first: The number of records to return, used for pagination
:type first: Int
:param offset: The number of records to offset, used for pagination
:type offset: Int
"""
qc_check_query = """
query GetQCResults(
  $id: ID!
  $severities: String
  $first: Int
  $offset: Int
){
  submissionQCResults(_id:$id, severities:$severities, first:$first, offset:$offset){
    total
    results{
      submissionID
      severity
      type
      errors{
        title
        description
      }
      warnings{
        title
        description
      }
    }
  }
}
"""