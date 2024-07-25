import requests
import json

url = 'http://localhost:8080/auth/login'
data = {'email': 'admin1@test.com', 'password': 'pass_1234'}
headers = {'Content-type': 'application/json'}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)

jsonResponse = json.loads(response.content)
accessToken = jsonResponse['accessToken']

######### Add Author
url = 'http://localhost:8080/api/authors'
data = {
'firstName': 'test 2',
'lastName': 'test 2',
'gender': 'MALE',
'birthday': ''
}
headers = {
'Content-type': 'application/json',
'Authorization': f'Bearer {accessToken}'
}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)

######### Get Authors
url = 'http://localhost:8080/api/authors'
headers = {
'Content-type': 'application/json',
'Authorization': f'Bearer {accessToken}'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)

jsonResponse = json.loads(response.content)

#########

print(jsonResponse['_embedded']['authors'])

authors = jsonResponse['_embedded']['authors']

for author in authors:
    #firstName, lastName, gender, birthday = author
    #print(firstName, lastName, gender. birthday)
    print(author)

if total := len(jsonResponse['_embedded']['authors']):
    print(f'we have {total} authors')