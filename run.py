import getpass
import string
from user import User
from credentials import Credentials

"""
Begin by formulating the User class dependent 
executable run functions 

"""
def create_user(username, password):
  '''
  A function for generating a new user instance
  
  '''
  new_user = User(username,password)

  return new_user

def save_user(user):
  '''
  A function used to save a new user instance
  by calling the User class save_user() method property

  '''
  User.save_user()

def delete_user(user):
  '''
  A function used to delete a user instance by calling
  the User class delete_user() method property

  '''
  User.delete_user()

def find_user(username):
  '''
  A function used to find a user instance by calling 
  the User class find_by_username() method property

  '''
  return User.find_by_username(username)

def check_existing_users(username):
  '''
  A function used to check whether a user instance exists 
  by calling the User class user_presence() method property 
  
  '''
  return User.user_presence(username)


def display_all_users():
  '''
  A function used to display all the users 
  saved in the User class user_object_list
  
  '''

  return User.user.display_all_users()


"""
Next formulate the Credential class dependent 
executable run functions 

"""

def create_credentials(self, account, username, password):
  '''
  A function to generate new account credentials

  '''

  new_credentials = Credentials(account, username password)
  return new_credentials


def save_credentials(new_credentials):
  '''
  A function to save credentials by calling the 
  Credentials class save_credentials method property

  '''
  Credentials.save_credentials()


def delete_credentials(credentials):
  '''
  A function to remove an account credential instance by calling 
  the Credentials class delete credentials method property

  '''
  Credentials.delete_credentials()

def find_credentials(username):
  '''
  A Function which searches for an account credential 
  by its username and returns the associated instance 
  by calling the Credential class method find credentials

  '''
  return Credentials.find_credentials(username)


def check_existing_credentials(username):
  '''
  A Function to check whether an account credential 
  with the username argument value already exists 
  and return a boolean result by calling the  
  Credential class method property credential_confirmation

  '''
  return Credentials.credential_confirmation(username)


def display_credentials();
  '''
  A Function which returns instances of all the 
  saved account credentials by calling the 
  Credential class method property display credentials

  '''

  return Credentials.display_credentials()

