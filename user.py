class User:
    """
    The Class from which User host Object instances
    are to be generated 

    """
    user_object_list = [] #An empty list to hold user objects

  def __init__(self, username, password):#method for generating a class User object

    self.username = username
    self.password = password


  def save_user(self):
    '''
    Saves a new user instance to our application

    '''
    User.user_object_list.append(self)

  def delete_user(self):
    '''
    Deletes a saved user object instance from the user_object_list

    '''
  @classmethod
  def display_all_users(cls):

    '''
    Method to show User class instances added into the user object list
    '''
    return cls.user_object_list


  @classmethod
  def find_by_username(cls,username):
    '''
    Method which takes in a username argument and 
    returns a name match for that username
    
    Parameter: username- the user to search

    Return: the user with a matching username
    '''

    for user in cls.user_object_list:
      if user.username == username:
        return user

 


      