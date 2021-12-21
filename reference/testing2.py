import pyrebase

config = {
    "apiKey": "AIzaSyCh_LLod4y9rPKI1EeE1PhfpZjJUCOABbk",
    "authDomain": "huan-sa-hsu-microservices.firebaseapp.com",
    "databaseURL": "https://huan-sa-hsu-microservices-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "huan-sa-hsu-microservices",
    "storageBucket": "huan-sa-hsu-microservices.appspot.com",
    "messagingSenderId": "985686998684",
    "appId": "1:985686998684:web:fa07feb0352f2bc56cf759",
    "measurementId": "G-20PTFD86KW"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# # Save database
# data = {"name": "Mortimer 'Morty' Smith"}
# db.child("User").push(data)

# # Save database from key
# data = {
#     "name": "Mortimer",
#     "age": 24
# }
# db.child("User").child("user1").set(data)
rs = db.child("User").get()

count = 0

# if rs.each() == None:
#     print(1)
# else:
#     print(2)

str1 = "haha"
str2 = "hihi"
num1 = 1

# rs = str + str(num1)
# print(rs)

rs = str1 + str(num1)
print(rs)

# for user in rs.each():
#     # print(user.key(), user.val())
#     count += 1

# print(count)
# print(rs)