from bottle import default_app, get, run, static_file


import login_post
import signup_get
import home_get
import signup_post


#############################################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

#############################################
@get("/images/<image_name>")
def _(image_name):
    return static_file(image_name, root="./images")
#############################################
@get("/app.js")
def _():
    return static_file("app.js", root=".")

#############################################



try:
    import production
    application = default_app()
except:
    run(host='127.0.0.1', port=3333, debug=True, reloader=True, server="paste")