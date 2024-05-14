import re

def checkEmpty (str):
    if (len (str.strip()) == 0):
        return True
    return False

def checkName(name):
    if (len (name) < 2):
        return False
    for x in name:
        tmp = ord (x)
        if (tmp < 32 
            or tmp > 32 and tmp < 65 
            or tmp > 89 and tmp < 97 
            or tmp > 121 and tmp < 192):
            return False
    return True

    
def checkPhone(phone_number):
    pattern = r"^\d{10}$"
    if re.match(pattern, phone_number):
        return True
    else:
        return False
    
def checkBirthday(birthday):
    # YYYY-MM-DD
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(pattern, birthday):
        return True
    else:
        return False
def checkPort (listport) :
    patttern =r"^\d+(\s+\d+)*$"
    if re.match (patttern,listport):
        return True
    else:
        return False
def checkUserName (userName) :
    regex_username = r"^[a-zA-Z]{3,16}$"
    return bool(re.match(regex_username, userName))

def checkPassword (password):
    return len(password.strip())>8