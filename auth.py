#registration
# - username, password, email
# - generate userId

#login
# - username/email, password 

import logging


def registration():
    logging.info("this is registration")
    pass

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
    logging.info("this is init")

    print("Welcome to Le Bank")
    
    haveAccount = input("Do you have an account? (y/n)")
    
    if(haveAccount == 'y'):
        login()
    elif(haveAccount == 'n'):
        registration()
    else :
        print("Invalid input")
        init()
    

init()