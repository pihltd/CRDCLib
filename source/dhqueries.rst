crdclib package
================

crdclib.dhqueries module
------------------------

.. automodule:: dhqueries
  :members: create_batch_query, list_sub_query

    **dhqueries.create_batch_query : This mutation creates a batch for submission**
 

      Query Variables:
        - submissionID (ID):  Required.  The submission ID.  Can be obtained from the interface or list_sub_query
        - type (String): Required.  The type of the submission.  Can be "metatada and data" or "metadata"
        - file (FileInput): Required.  CRDC FileInput object

      Returned Fields
        - _id (String)
        - List of:

          - fileName (String):  Name of the file
          - signedURL (URL): A signed URL that can be used to update the file object

    **dhqueries.list_sub_query : A query that lists all submissions that are accessible**

      Query Variables:  None

      Returned fields:
        - _id
        - name
        - submitterID
        - submitterName
        - studyAbbreviation
        - studyID
        - dbGaPID
        - createdAt
        - updatedAt
        - metadataValidationStatus
        - fileValidationStatus
        - status
