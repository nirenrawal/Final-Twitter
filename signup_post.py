from bottle import post, request, redirect
import uuid
<<<<<<< HEAD
<<<<<<< HEAD
=======

import niren
>>>>>>> 4adb892f93db09cea01c9682603ff9f9bbc35cb1

users = []
=======
import niren

<<<<<<< HEAD

>>>>>>> login-backend
=======


users = []

>>>>>>> 4adb892f93db09cea01c9682603ff9f9bbc35cb1


@post("/signup")
def _():
    # Missing Validation
    user_id = str(uuid.uuid4())
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_email = request.forms.get("user_email")
    user_name = request.forms.get("user_name")
    user_password = request.forms.get("user_password")
    user = {
        "id": user_id,
        "first_name": user_first_name,
        "last_name": user_last_name,
        "email": user_email,
        "username": user_name,
        "user_password": user_password
    }
<<<<<<< HEAD
<<<<<<< HEAD
    users.append(user)
=======
    niren.USERS.append(user)
>>>>>>> login-backend
=======

    niren.USERS.append(user)

    users.append(user)

>>>>>>> 4adb892f93db09cea01c9682603ff9f9bbc35cb1
    return redirect(f"/signup-get?id={user_id}&first_name={user_first_name}&last_name={user_last_name}&email={user_email}&username={user_name}&user_password={user_password}")