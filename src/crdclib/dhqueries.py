
"""

Attributes:
  create_batch_query

  This mutation creates a batch for submission

  :param submissionID:  Required.  The submission ID.  Can be obtained from the interface or list_sub_query
  :type submissionID: ID 
  :param type: Required.  The type of the submission.  Can be "metatada and data" or "metadata"
  :type type: String
  :param file: Required.  CRDC FileInput object
  :return _id:
  :rtype: String
  :return fileName:  Name of the file
  :rtype: String
  :return signedURL: A signed URL that can be used to update the file object
  :rtype: URL

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
