
***Muchunku-Pages***

# Access-ManagerApplication

## Author
Brian Mwenda Muchunku

## Description
This is a basic Python application developed as an solution to manage the present day multiplicity of Digital Media Account Credentials which enables the user to keep track of thier Username and Passwords for for thier various digital media accounts respectively.

The Application enables its Users to store account Credential information for thier multiple digital media accounts and also enables the generation of a unique password for its User in the event they do not want to generate the new passwords themselves.

## Set-Up Instructions
### Installation Requirements
This Application was developed using Python3.8.1. 

In its executable form it can be run at a terminal from its own source code files at a Computer's Terminal regardless of the Python3.* version installed on your PC.

However, to be able to further develop and manipulate its code, ensure its either developed in a compatible version or that you convert this Python code version, into a version compatible with the Python version you wish to work with.

### Dowloading The Access Manager Application 
* Access Your Computer's Terminal prompt by pressing and holding{Ctrl+Alt+T} keys in succession

* Append the Application's Repository path in Git Hub at the terminal prompt to the git clone command as follows: 
 https://github.com/Muchunku-Pages/Access-ManagerApp.git

## Running the Application on Your Computer

* Change the directory path to the cloned repository using the following command: $ cd AccessManagerApp

* Enter the code to switch to and open your installed code editor such as VSCode or Atom:$ code . / $ atom .

* To execute the application, open the cloned file from the terminal prompt to the Application path as shown above and run the following commands:

      $ python3 run.py

To run the Application's unit test file *use $ python3.8 run_test.py or a compatible version

## User Story
As a user I want to be able to:

    1. Log into the Access Manager Application. 
    
    2.Create a User account in the Application or view my existing User Account Credentials.

    2. Store my Account Credentials for multiple existing digital media accounts that I have registered for.

    3. Generate a new password for an account that I haven't yet registered and store it with the account name.

    4. Remove any stored account credentials that I no longer require.

    5. Copy my User Account Credentials data to a clipboard.

## BDD
|               Behaviour              | Input                            | Output                                               |
|:------------------------------------:|----------------------------------|------------------------------------------------------|
| Open the application on the terminal | Run the command ***$ ./run.py*** | Welcome to the Access Manager Application enabling you manage your various Log-In Digital Media Access Credentials 
Use the following short code keys and corresponding instructions to proceed ... **ca** --- Create account details here |
|               Select ***ep***        | enter your own password     | Welcome ***username*** to password locker.
Your new account password is: ***password***|
|Store new credentials in your application|   Enter ***cc***              |   Enter Account, username, password 
Select ***tp*** to enter your password or ***gp*** for the application to generate one for you |
| Display all the saved Yser Account Credentials       |           Enter ***dc***         |Displays the list of all Account Credentials that have been stored or the information: You don't have any saved Account Credentials yet|
|Find stored credentials based on the account name|    Enter ***fc***        |Enter the Account Name you wish to search for and it returns its corresponding account credential details|
|Delete existing account credentials that you no longer require| Enter ***dd*** |Enter the Account name of the Credentials you wish to delete and it returns a true evaluation after the account has been deleted or a false evaluation if the account doesn't exist|
|  Exit the application                |              Enter ***ex***       | Exit application |


## Technology Used
* Python3.8.1

## Contact Info:
For any queries or comments about this application, please email me at []

## License
* MIT License

* Copyright (c) 2022 Brian Mwenda Muchunku
