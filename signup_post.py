from bottle import post, request, redirect
import uuid
import niren




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
    niren.USERS.append(user)
    return redirect(f"/signup-get?id={user_id}&first_name={user_first_name}&last_name={user_last_name}&email={user_email}&username={user_name}&user_password={user_password}")