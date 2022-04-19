from bottle import get, view, request


@get("/signup-get")
@view("signup-get")
def _():
    user_id = request.params.get("id")
    user_first_name = request.params.get("first_name")
    user_last_name = request.params.get("last_name")
    user_email = request.params.get("email")
    user_name = request.params.get("username")
    user_password = request.params.get("user_password")
    return dict(user_id=user_id, user_first_name=user_first_name, user_last_name=user_last_name, user_email=user_email, user_name=user_name, user_password=user_password)