from bottle import default_app, get, run

@get("/")
def _():
    return "ok"




try:
    import production
    application = default_app()
except:
    run(host='127.0.0.1', port=3333, debug=True, reloader=True, server="paste")