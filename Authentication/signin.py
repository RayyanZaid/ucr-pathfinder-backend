from firebase import auth, firebase_admin

def getUID(phone):

    try:
        user = auth.get_user_by_phone_number(phone)
        print('Successfully fetched user data: {0}'.format(user.uid))
        return True, user.uid
    
    except Exception as e:
        print(e)
        return False,e
