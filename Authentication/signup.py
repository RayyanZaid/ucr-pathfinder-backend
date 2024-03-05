from firebase import auth

def create_user(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        print('Successfully created new user: {0}'.format(user.uid))
        return user
    except Exception as e:
        print('Error creating new user:', e.code)
        return None