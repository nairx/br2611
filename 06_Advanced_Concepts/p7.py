def login_required(fnc):
    def wrapper(*args,**kwargs):
        print("Logging into the system....")
        result = fnc(*args,*kwargs)
        return result
    return wrapper

def log_activity(fnc):
    def wrapper(*args,**kwargs):
        print("Logging activity...")
        result = fnc(*args,**kwargs)
        return result
    return wrapper

@login_required
@log_activity
def view_profile():
    print("View Profile")


@log_activity
def view_products():
    print("View Products")

view_profile()

view_products()