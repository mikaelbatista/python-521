
import requests

URL = 'https://gen-net.herokuapp.com/api/users/{}'

user_id = input('Digite seu id: ')

response = requests.get(URL.format(user_id))

if response.status_code == 200:
	print(response.json().get('name'),response.json().get('email'))
else:
	print(response.text)

