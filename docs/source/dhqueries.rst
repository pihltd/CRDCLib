CRDCLib DHQuery documentation
====================================

.. note:: These are python strings, not actual functions. Useage would be **dhqueries.queryname**, don't call them like functions.

.. function:: create_batch_query

    A mutation that creates a new batch for submission.

    :param submissionID:  The submission ID the batch will be created for.
    :param type:  The type of submission
    :param file: A Data Hub FileInput object
    :rtype: | _id
      | files
      |  fileName
      |  signedURL

.. function:: list_sub_query

    A query that lists all of the submisisons the account can access

    :param status: Allowed values are: All | New | In Progress | Submitted | Released |Completed | Archived | Canceled | Rejected | Withdrawn | Deleted
    :rtype: | _id
      | name
      | submitterID
      | submitterName
      | studyAbbreviation
      | studyID
      | dbGaPID
      | createdAt
      | updatedAt
      | metadataValidationStatus
      | fileValidationStatus
      | status

.. function:: create_submission_query
    
    Creates a new submission

    :param studyID:  This is the assigned Study ID that can be obtained from the **_id** field in the *getMyUser* query
    :param dbGaPID: Obtained when registering the study at dbGaP.  This is required for all controlled access studies
    :param dataCommons: This is the CRDC Data Commons the submissions will be deposited into
    :param name: This can be anything that allows you to identify this specific submission
    :param intention: Can be *New/Update* if you are adding information to the submission or  *Delete* if you are removing information from an earlier, completed submission
    :param dataType: Can be either *Metadata and Data Files* or *Metadata Only*.  Which one is selected depends on whether or not data files will be included in the submission
    :rtype: | _id
      | studyID
      | dbGaPID
      | dataCommons
      | name
      | intention
      | dataType
      | status

.. function::  org_query

    Returns information about the organization

.. function:: qc_check_query

    Returns detailed validation results

    :param id: The submission ID to be queried
    :param severities: The severity of the validation results. Can be All | Error | Warnings
    :param first: The number of records to be returned.  If first is set to -1, the API will return all results.
    :param offset: The number of records to be skipped when returning results.
    :rtype: | total
      | results
      |   submissionID
      |   severity
      |   type
      |   errors
      |     title
      |     description
      |   warnings
      |     title
      |     description