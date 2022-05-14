#registration
# - username, password, email
# - generate userId

#login
# - username/email, password 

import logging
from pickle import TRUE


def registration():
    logging.info("this is registration")
    
    haveAccount = input("Do you have an account? (y/n)")
    
    if(haveAccount == 'y'):
        login()
    elif(haveAccount == 'n'):
        pass
    else :
        print("Invalid input")
        registration()

def login():
    logging.info("this is login")
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if(username == 'admin' and password == 'admin'):
        print("Welcome admin")
        bankOperation()
    elif():
        pass
    
    pass

def bankOperation():
    logging.info("this is bankOperation")
    pass

def generateAccountNumber():
    logging.info("this is generateAccountNumber")
    pass


def init():
    print("this is init")


init()