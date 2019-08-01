
import requests

URL = 'https://gen-net.herokuapp.com/api/users'

response = requests.get(URL)

users = response.json()

email = input('Digite seu email: ')

for user in users:
	if user.get('email') == email:
		print(user)

