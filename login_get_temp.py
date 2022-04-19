from bottle import get, view

@get("/login")
@view("login_temp")
def _():
    return