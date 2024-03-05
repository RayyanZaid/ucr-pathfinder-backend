from firebase import auth, firebase_admin

def create_user(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print('Successfully created new user: {0}'.format(user.uid))
        return True , user
    except Exception as e:
        print('Error creating new user:', e.code)
        return False, e.code
    
def send_email_verification(uid):
    try:
        user = auth.get_user(uid)
        email = user.email
        link = auth.generate_email_verification_link(email)
        print("Email verification link:", link)
    except Exception as e:
        print("Error sending email verification:", e)