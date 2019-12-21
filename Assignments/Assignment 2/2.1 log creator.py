# 1. Create a log creator that will accept, following details as a parameter and log the details into the file with the time of logging.
#     a. a message
#     b. type of the message like INFO, WARNING, ERROR
# 2. Create a command line contact book that wll allow storing contact details of the user including phone no, email address and home address. The user should be able to efficiently search for contact details by phone no, email or name of the person. DO NOT USE ANY DATABASE.
# 3. Create a URL shortener that will create a short URL for the URL provided and will redirect to the original URL whenever a short URL is provided by the user.

import logging 
   
logging.basicConfig(filename="./Assignments/Assignment 2/2.1 output log.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='a')
 
logger=logging.getLogger()
   
logger.setLevel(logging.DEBUG) 
   
logger.info("Just an information.") 
logger.warning("Its a Warning.") 
logger.error("This is any logical error.") 