"""
Used structures and classes
"""
from os import path
import json
import pandas as pd

def create_LocalDatabaseServiceRoutines():
    return LocalDatabaseServiceRoutines()

class LocalDatabaseServiceRoutines(object):
    def __init__(self):
        self.name = 'Data base service routines'
        self.index = {}
        self.UsersDataFile = path.join(path.dirname(__file__), '..\\static\\Data\\users.csv')

    #This is the building function for the whole class that is used to create 'login' and 'register'.

    def ReadCSVUsersDB(self):
        df = pd.read_csv(self.UsersDataFile)
        return df
    #This function pulls out the users data and puts it in a DataFrame.



    def WriteCSVToFile_users(self, df):
        df.to_csv(self.UsersDataFile, index=False)

    #This function converts data from a DataFrame back to the users file.

    def IsUserExist(self, UserName):
        df = self.ReadCSVUsersDB()
        df = df.set_index('username')
        return (UserName in df.index.values)
    #Checks if a Username exits already in the system.


    def IsLoginGood(self, UserName, Password):
        df = self.ReadCSVUsersDB()
        df=df.reset_index()
        selection = [UserName]
        df = df[pd.DataFrame(df.username.tolist()).isin(selection).any(1)]

        df = df.set_index('password')
        return (Password in df.index.values)
    #Checks if the Username and the password the user has entered are correct.
     

    def AddNewUser(self, User):
        df = self.ReadCSVUsersDB()
        dfNew = pd.DataFrame([[User.FirstName.data, User.LastName.data, User.PhoneNum.data, User.EmailAddr.data, User.username.data, User.password.data]], columns=['FirstName', 'LastName', 'PhoneNum', 'EmailAddr',  'username', 'password'])
        dfComplete = df.append(dfNew, ignore_index=True)
        self.WriteCSVToFile_users(dfComplete)

    #Creates a new user in the system based on the user's input.

