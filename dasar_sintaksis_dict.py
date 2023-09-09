users = {
    'id': 1,
    'name': 'Learn Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}


print(users)
print(users['id'])
print(users['name'])
print(users['username'])
print(users["address"])
# di bawah ini cara memanggil street yang berada dalam address / json dalam json / dictionary dalam dictionary
print(users['address']['street'])
print(users['address']['geo'])
print(users['address']['geo']['lat'])

print('\n berikut ini type data dictionary')
print(users)
print(type(users))

print('\n Ubah dictonary ke json')
import json
result = json.dumps(users)
print(result)
print(type(result))