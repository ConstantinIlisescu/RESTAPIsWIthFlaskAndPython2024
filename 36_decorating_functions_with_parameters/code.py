import functools

user = {"username": "costa", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin persmissions for {user['username']}."
        
    return secure_function

@make_secure
def get_password(panel: str):
    if panel == "admin":
        return "1234"
    elif panel == 'biling':
        return "super_secured_password"
        

print(get_password('biling'))