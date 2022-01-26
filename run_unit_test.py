import unittest
from credentials import Credentials 
from user import User 

class TestUser(unittest.TestCase):
  '''
  A Test Class which we formulate to provide test cases 
  to  evaluate the behaviour of the User Class methods

  Parameters: unittest.TestCase: A TestCase class that facilitates 
  the creation of test case instances

  '''

  def setUp(self):
    '''
    The Test's Set Up method used to provide test input 
    that may be used when carrying out test cases
  
    '''
    self.new_user = User("MuchunkuBrian","88888888")# Generates sample User Object instance test property values for our test case


  def tearDown(self):
    '''
    The Test's Tear Down method used to carry out the clean up 
    once each test case has completed its execution.

    '''

  def test_init(self):
    '''
    test_init test case to test whether the User object is properly initialized
            
    '''
    self.assertEqual(self.new_user.username,"MuchunkuBrian")
    self.assertEqual(self.new_user.password,"88888888")


  def test_save_user(self):
    '''
    test_save_user test case to test whether the user object is saved into
    the user list

    '''
    self.new_user.save_user() # method for saving the new user instance
    self.assertEqual(len(User.user_object_list),1)
                  


  def test_save_multiple_user(self):
    '''
    test_save_multiple_user test method to check whether we can save multiple user
    objects in our user_object_list

    '''
    self.new_user.save_user()
    test_user = User("Test","user")
    test_user.save_user()
    self.assertEqual(len(User.user_object_list),2)

  def test_delete_user(self):
      '''
      test_delete_user to test whether we can remove a user from our user list
      
      '''
      self.new_user.save_user()
      test_user = User("Test","user") # passes in these test user values to be deleted
      test_user.save_user()

      self.new_user.delete_user()# Removes a user object instance
      self.assertEqual(len(User.user_object_list),1)


class TestCredentials(unittest.TestCase):
  '''
  A Test Class which we formulate to provide test cases 
  to  evaluate the behaviour of the Ctredentials class methods

  Parameters: unittest.TestCase: A TestCase class that facilitates 
  the creation of test case instances
  
  '''

  def setUp(self):
      '''
      The Test's Set Up method used to provide test input 
      that may be used when carrying out test cases
      '''
      self.new_credentials = Credentials("gmail","brimwenda","moringa022")# Generates sample Credentials Object instance 
                                                                        # test property values for our test case


  def test_init(self):
      '''
      test_init test case to test if the object is initialized properly

      '''
      self.assertEqual(self.new_credentials.account,"gmail")
      self.assertEqual(self.new_credentials.username,"brimwenda")
      self.assertEqual(self.new_credentials.password,"moringa022")

  def test_save_credentials(self):
      '''
      test_save_credential test case to test if the account credentials object is saved in
      the credentials list

      '''
      self.new_credentials.save_credentials()
      self.assertEqual(len(Credentials.credentials_object_list),1)

  def tearDown(self):
      '''
      tearDown method that does clean up after each test case has run.
      
      '''
      Credentials.credentials_object_list = []

  def test_save_multiple_credentials(self):
      '''
      test_save_multiple_credentials to check if we can save multiple credential
      objects to our credential_list
      
      '''
      self.new_credentials.save_credentials()
      test_credentials= Credentials("gmail","brimwenda","moringa022") # new credential
      test_credentials.save_credentials()
      self.assertEqual(len(Credentials.credentials_object_list),2)

  def test_delete_credentials(self):
      '''
      test_delete_credentials to test whether we can delete a credential from credential list
      
      '''
      self.new_credentials.save_credentials()
      test_credentials = Credentials("gmail","brimwenda","moringa022") # new credential
      test_credentials.save_credentials()

      self.new_credentials.delete_credentials()# Removing a credential object instance 
      self.assertEqual(len(Credentials.credentials_object_list),1)#from our credentials objectlist

  def test_find_credentials_by_username(self):
      '''
      test to check whether we can find credentials by username and display information
      
      '''
      self.new_credentials.save_credentials()
      test_credentials = Credentials("gmail","brimwenda","moringa022") # a new credential object instance
      test_credentials.save_credentials()

      found_credentials = Credentials.credential_confirmation("brimwenda")

      self.assertEqual(found_credentials.username,test_credentials.username)


  def test_credential_exists(self):
      '''
      test method to check the Boolean value returned on searching for the specified credential.
      
      '''
      self.new_credentials.save_credentials()
      test_credentials = Credentials("gmail","brimwenda","moringa022")
      test_credentials.save_credentials()

      credential_exists = Credentials.credential_confirmation("brimwenda")

      self.assertTrue(credential_exists)


  def test_display_all_credentials(self):
      '''
      test method that returns a list of all the saved credentials

      '''

      self.assertEqual(Credentials.display_credentials(),Credentials.credentials_object_list)

if __name__ == '__main__':
  unittest.main()
