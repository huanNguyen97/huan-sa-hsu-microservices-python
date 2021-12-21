# Import from python
from fastapi import FastAPI, Form
from typing import Optional

from fastapi.middleware.cors import CORSMiddleware

# Import from owner
from db_config import db


# Main app
# ------------------------------------------------
# ------------------------------------------------
app = FastAPI()

# Allow origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/register")
async def register(
    username: str = Form(...), 
    password: str = Form(...),
    confirm_password: str = Form(...)
):
    if password != confirm_password:
        return {"Error": "Password and config password is not correct!!!"}
    else:
        data = {"id": 1, "username": username, "password": password}
        
        result = db.child("User").get()
        if result.each() == None:
            db.child("User").child("user1").set(data)
        else:
            count = 0
            for user in result.each():
                if user.val()["username"] == username:
                    return {"Error": "Username have existed, try another username."}
                count += 1
            count_result = count + 1
            data["id"] = count_result
            db.child("User").child("user" + str(count_result)).set(data)

        return {
            "username": username,
            "password": password
        }


@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == None or password == None:
        return {"Error": "Please fill all the information"}
    else:
        result = db.child("User").get()
        for user in result.each():
            if username != user.val()["username"] or password != user.val()["password"]:
                pass
            else:
                return {
                    "status": 200,
                    "username": username
                }
        return {"Error": "Your username or password isn't correct"}

# ------------------------------------------------
# ------------------------------------------------
# End app