from user import User
from credentials import Credentials

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





















