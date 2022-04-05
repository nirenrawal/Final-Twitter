from bottle import default_app, get, run, static_file



import signup_get
import home_get

#############################################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

#############################################




try:
    import production
    application = default_app()
except:
    run(host='127.0.0.1', port=3333, debug=True, reloader=True, server="paste")