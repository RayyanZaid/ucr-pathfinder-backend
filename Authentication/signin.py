import firebase_admin
from firebase_admin import auth
from firebase import cred



def createNewUser(email : str, password : str) -> str: 
  
    user = auth.create_user(
            email=email,
            email_verified=False,
            password=password
        )

    print(f"Successfully signed in user with user id of {user.uid}")

    return "Success"

def signInExistingUser(email : str, password : str) -> str:
    try:
        user = auth.get_user_by_email(email)
        # I need to verify the password
        
        print(f"Successfully signed in user with user id of {user.uid}")
        return "Success"
    except:
        return "User does not exist"