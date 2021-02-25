import requests


BASE = 'http://127.0.0.1:5000/'

data = [
    {'user_id': '1234', 'title': 'sample title', 'description': 'sample description'},
    {'user_id': '567', 'title': 'another title', 'description': 'another description'}
]

for i in range(len(data)):
    response = requests.put(BASE + 'item/' + str(i), data[i])
    print(response.json())


input("press Enter to continue: \n")
response = requests.get(BASE + 'item/1')
print(response.json())

input("press Enter to continue: \n")
response = requests.patch(BASE + 'item/1', {"user_id": "Tamar"})
print(response.json())

input("press Enter to continue: \n")
response = requests.put(BASE + 'user/Tamar', {'user_id': 'Tamar', 'pref_name': 'Tanner'})
print(response.json())

input("press Enter to continue: \n")
response = requests.get(BASE + 'user/Tamar')
print(response.json())

input("press Enter to continue: \n")
response = requests.patch(BASE + 'user/Tamar', {'pref_name': 'Grammar'})
print(response.json())

input("press Enter to continue: \n")
response = requests.delete(BASE + 'item/1')
print(response.json())

input("press Enter to continue: \n")
response = requests.put(BASE + 'user/Tziporah', {'user_id': 'Tziporah', 'pref_name': 'Tzip'})
print(response.json())

input("press Enter to continue: \n")
response = requests.patch(BASE + 'user/Tziporah', {'pref_name': 'Trish'})
print(response.json())

