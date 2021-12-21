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