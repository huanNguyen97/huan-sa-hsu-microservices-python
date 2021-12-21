from firebase import firebase

firebase = firebase.FirebaseApplication('https://huan-sa-hsu-microservices-default-rtdb.asia-southeast1.firebasedatabase.app/', None)

data = {
    'name': 'Huan',
    'age': 26
}

result = firebase.post('/User', data, params="user1")
result2 = firebase.get('/User', None)

# count = 0

# for key, value in result2.items():
#     if value["age"] == 26:
#         count += 1

# for key, value in result2.items():
#     print(key, value)

# print(count)

# print(count)
# print(result2)