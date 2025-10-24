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

    :param status: Allowed values are: All \| New \| In Progress \| Submitted \| Released \|Completed \| Archived \| Canceled \| Rejected \| Withdrawn \| Deleted
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
    :param severities: The severity of the validation results. Can be All \| Error \| Warnings
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

.. function:: submission_stats_query

  Returns an overview of a high-level overview of the nodes that have been populated along with how many nodes have warnings and errors.  The goal of this query it so get some orientation before digging into the actual contents of any given node.

    :param _id:  The submission ID to report
    :rtype: | stats
      | nodeName
      | total
      | new
      | passed
      | warning
      | error

.. function:: submission_nodes_query

  Sometimes it can be useful to see what data have been submitted and this can be done with the **getSubmissionNodes** query.  This query will pull back all of the information added to each node in the submission.  This can allow submitters to double check that the data they're submitting is being processed properly and to spot any errors that may have gotten past validation.

  :param submissionID: The submission ID to use
  :param nodeType: The name of the node to query (file, sample, etc.)
  :param status: Allowed values are: All \| New \| In Progress \| Submitted \| Released \|Completed \| Archived \| Canceled \| Rejected \| Withdrawn \| Deleted
  :param first: The number of records to be returned.  If first is set to -1, the API will return all results.
  :param offset: The number of records to be skipped when returning results.
  :param orderBy: The field to order with the sortDirection
  :param sortDirection: Ascending/descending sort
  :rtype: |  total
    | IDPropName
    | properties
    | nodes 
    |     nodeID
    |     nodeType
    |     status
    |     props


.. function:: delete_datarecords_query

  If there are individual records in your submission that need to be removed from the submission, the **deleteDataRecords** mutation will remove them from your submission.  This query will take one or more nodeIDs (obtained from the **getSubmissionNodes** query) and remove them from the submission records.
  *Note*: To delete uploaded data files, set the **nodeType** field to 'data file'.  This will remove uploaded files from the S3 bucket.

  :param submissionID: The submission ID where the deletion should happen
  :param nodeType: The name of the node where the deletion will happen (file, sample, etc.)
  :param nodeIDs: A list of the specific node IDs to be deleted (can bo obtained from the submission_nodes_query)
  :rtype: | success
    | message
  
.. function:: study_query

  This returns information on the user's status and the studies they have access to.

  :param None:  This query takes no parameters
  :rtype: | userStatus
    | studies 
    |   _id
    |  controlledAccess
    |  createdAt
    |  dbGaPID
    |  studyName
    |  studyAbbreviation
