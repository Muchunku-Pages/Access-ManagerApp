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

  new_credentials = Credentials(account, username, password)
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


def display_credentials():
  '''
  A Function which returns instances of all the 
  saved account credentials by calling the 
  Credential class method property display credentials

  '''

  return Credentials.display_credentials()

def main():
  print("Hello User! Welcome to the Access Account Credentials Manager App, enabling you manage your various Log-In Media Access Credentials")
  print("\n")
  print('Please make use of the following short codes to carry out its corresponding tasks, as you require: ca = create account,' )
  short_code = input().lower()
  if short_code == 'ca':
    print('Create  your new account details here')
    print('*' * 10)
    username = input('Enter a Username: ')
    while True:
        print('use :  ep = to  enter your own password')
        password_choice = input().lower()
        if password_choice == 'ep':
            password = input('Enter its associated Password: ')
            break
        else:
            print('Sorry! You have entered the wrong short code. Please try again')

        save_user(create_user(username, password))   
    print('*' * 10)
    print(f'Welcome {username} to the Access Account Manager. Your newly created account password is <--- {password} --->')
    print('*' * 10)
  while True:
      print('Please use the following short codes provided, to manage your account credentials: \n cc = create credentials, \n dc = display credentials,\n fc = find credentials  \n Dd = delete credentials, \n  EX = exit application')
      short_code = input().lower()

      if short_code == 'cc':
          print('Enter Your new User Account Credentials Here:')
          print('*' * 10)
          account = input('Account Name : ')
          username1 = input('Username : ')
          while True:
            print('Use the code: ep  To Enter Your Own Password?')
            password_choice = input().lower()
            if password_choice == 'ep':
                password = input('Enter Your Password : ')
                break
            else:
                print('You have entered an incorrect short code. kindly try again')
            print('*' * 10)
            save_credentials(create_credentials(account, username1, password, password))
            print('*' * 10)
            print(f'Your {account} access account details have been saved succesfully in the Access Manager application')
            print('*' * 10)

      elif short_code == 'dc':
        if display_credentials():
          print('Your access account credentials are as follows:')
          for account in display_credentials():
            print('-' * 10)
            print(f'Username: {username1} \n Password: {password}')
            print('-' * 10)
        else:
          print('*' * 10)
          print('You have no such user access account. Please go to the Create a new account short code menu option to create one')
          print('*' * 10)  

      elif short_code == 'dd':
        print('Enter the Account Name to be deleted...')
        name = input('Account Name : ')
        print('*' * 10)
        if find_credentials(name):
          name_result = find_credentials(name)
          name_result.delete_credentials()
          print(f'The Account {name} has been removed successfully ')
          print('*' * 10)
        else:
          print('You entered an Incorrect Account Name. Please type in a correct Account Name again')
          print('*' * 10)

        elif short_code == 'fc':
          print('Enter Account Name To Be Found...')
          search = input('Account Name : ')
          print('*' * 10)
          if find_credentials(search):
            search = find_credentials(search)
            print(f'Account Name: {search} ')
            print('*' * 10)
          else:
            print(' the Account Credentials you are looking for do not exist')
            print('*' * 10)

        elif short_code == 'ex':
          print('Thank You for choosing our Access Account Manager to Manage Your Access Credentials')
          print('*' * 10)
          break

        else:
          print(' You have entered an Invalid Short code. Please try again!')
          print('*' * 10)

if __name__ == '__main__':
  main()  