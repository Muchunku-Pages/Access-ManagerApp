import random
import string
class Credentials:
  """
  The Class from which new Credential object instances
  are to be generated.

  """

    credentials_object_list = [] #An Empty list to hold credential objects
    

    def __init__(self, account, username, password):
      """
       Method that generates the account credentials object to hold 
       the details of each user instance

      """

      self.account = account
      self.username = username
      self.password = password

    def save_credentials(self):
      '''
      Saves a credentials account instance to our application

      '''
      Credentials.credentials_object_list.append(self)


    def delete_credentials(self):
      '''
      Deletes a saved account credentials instance from the 
      credentials object list
      
      '''

      Credentials.credentials_object_list.remove(self)

