import jwt
from decouple import config
import re



def checkemailforamt(Email):
    emailregix = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.match(emailregix, Email)):
        return True

    else:
        return False


def PasswordLenghtValidator(Password):
    if len(Password)>= 8 and len(Password)<= 20:
        return True

    else:
        return False          


def requireKeys(reqArray,requestData):
    try:
        for j in reqArray:
            if not j in requestData:
                return False
            
        return True

    except:
        return False




# def allfieldsRequired(reqArray,requestData):
#     try:
#         for j in reqArray:b
#             # if len(requestData[j]) == 0:
#                 return False

        
#         return True

#     except as Exception:
#         return False