import re
from decouple import config
import jwt

def superadmin(token):
    try:
        
        my_token = jwt.decode(token,config('superadminjwttoken'), algorithms=["HS256"])
        return my_token
        
    except jwt.ExpiredSignatureError:
        return False

    except:
        return False
