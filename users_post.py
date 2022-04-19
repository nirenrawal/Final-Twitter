from bottle import post, request
import g
import uuid
import time
from datetime import datetime

##############################
@post("/users")
@post("/<language>/users")
def _(language = "en"):
  try:
   #just to make user that the user does not type anyother language
    if f"{language}_server_error" not in g._errors : language = "en"

### not sure if to put backend validation or not for first name and last name

    # user_first_name, error = g._is_user_first_name(request.forms.get("user_first_name"), language)
    # if error : return g._send(400, error)
    # user_last_name, error = g._is_user_last_name(request.forms.get("user_last_name"), language)
    # if error : return g._send(400, error)  
    
    user_id = str(uuid.uuid4())
    user_first_name = request.forms.get("user_first_name")
    user_last_name = request.forms.get("user_last_name")
    user_name, error = g._is_user_name(request.forms.get("user_name"), language)
    if error : return g._send(400, error) 
    user_email, error = g._is_user_email(request.forms.get("user_email"), language)
    if error : return g._send(400, error) 
    user_password, error = g._is_user_password(request.forms.get("user_password"), language)
    if error : return g._send(400, error) 
    
    user = {
      "user_id":user_id,
      "user_first_name":user_first_name,
      "user_last_name":user_last_name,
      "user_name":user_name,
      "user_email":user_email,
      "user_password": user_password
    }
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])

  try:    
    db = g._db_connect("database.sqlite")
    db.execute("""INSERT INTO users 
                VALUES(:user_id, :user_first_name, :user_last_name, :user_name, :user_email, 
                :user_password)""", user)
    db.commit()
    return user
  except Exception as ex:
    print(ex)
    return g._send(500, g._errors[f"{language}_server_error"])
  finally:
    db.close()