
from bottle import post, redirect, request

import niren



@post("/login")
def _():
    user_name = request.forms.get("username")
    user_password = request.forms.get("user_password")
    for user in niren.USERS:
        if user_name == user["username"] and user_password == user["user_password"]:
            return "something is wrong"
    return redirect ("/signup-get")