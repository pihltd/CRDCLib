
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


