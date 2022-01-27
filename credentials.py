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

  @classmethod
  def find_credentials(cls,account):  
    '''
    A method that accepts an account value argument and returns 
    its corresponding credential details if a match is found

    '''  

    for Credentials in cls.credentials_object_list:
      if Credentials.account == account:
        return Credentials
  
  @classmethod
  def credential_confirmation(cls,username):
    '''
    A method for checking whether an account credential exists 
    in the credentials object list

    Parameters: username- the name value to be checked 

    Return: boolean- a true or false value depending on whether 
    the credentials exist
      
    '''
    for Credentials in cls.credentials_object_list:
      if Credentials.username == username:
        return True

    return False
  
  @classmethod
  def display_credentials(cls):
    '''
    A method to return all the account credential instances 
    contained in this classes credential object list.

    '''

    return cls.credentials_object_list



