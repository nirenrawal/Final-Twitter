from bottle import get, response
import g
import json

@get("/tweets")
@get("/<language>/tweets")
def _(language ="en"):
    try:
        if f"{language}_server_error" not in g._errors : language = "en"
    except Exception as ex:
        print(ex)
        return g._send(500, g._errors[f"{language}_server_error"])

    try:
        db = g._db_connect("database.sqlite")
        tweets = db.execute("SELECT * FROM tweets").fetchall()
        if not tweets: return g._send(204, "")
        response.content_type = "application/json"
        return json.dumps(tweets)
    except Exception as ex:
        print(ex)
        return g._send(500, g._errors[f"{language}_server_error"])
    finally:
        db.close()
