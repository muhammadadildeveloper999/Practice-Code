import api.usable as uc
from .serializer import* 


def requireKeys(reqArray,requestData):
        
    try:
        for j in reqArray:
            if not j in requestData:
                return False
            
        return True

    except:
        return False


def allfieldsRequired(reqArray,requestData):
    
    try:
        for j in reqArray:
            if len(requestData[j]) == 0:
                return False

        
        return True

    except:
        return False

    ##both keys and required field validation

def keyValidation(keyStatus,reqStatus,requestData,requireFields):
    
    ##keys validation
    if keyStatus:
        keysStataus = requireKeys(requireFields,requestData)
        if not keysStataus:
            raise serializers.ValidationError({'status':False,'message':f'{requireFields} all keys are required', 'error' : "All Fields are Required"})

    ##Required field validation
    if reqStatus:
        requiredStatus = allfieldsRequired(requireFields,requestData)
        if not requiredStatus:
            raise serializers.ValidationError({'error' : "All Fields are Required"})