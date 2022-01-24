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
  