from bottle import delete
import g

##############################
@delete("/users/<user_id>")
@delete("/<language>/users/<user_id>")
def _(language = "en", user_id = ""):
  try:
    # Maybe the user enters a language that is not supported, then default to english
    if f"{language}_server_error" not in g._errors : language = "en"
    
    user_id, error = g._is_uuid4(user_id, language)
    if error : return g._send(400, error)
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])

  try:
    db = g._db_connect("database.sqlite")
    counter = db.execute("DELETE FROM users WHERE user_id = ?", (user_id,)).rowcount
    db.commit()
    if not counter : return g._send(204, "")
    return {"info":"User successfully deleted"}
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])
  finally:
    db.close()






