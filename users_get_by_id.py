from bottle import get
import g

##############################
@get("/users/<user_id>")
@get("/<language>/users/<user_id>")
def _(language = "en", user_id = ""):
  try:
    # Use any key to see if the language is in the errors dictionary
    if f"{language}_server_error" not in g._errors : language = "en"
    user_id, error = g._is_uuid4(user_id, language)
    if error : return g._send(400, error)
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])

  try:
    db = g._db_connect("database.sqlite")
    user = db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    if not user: return g._send(204, "")
    return user
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])
  finally:
    db.close()






