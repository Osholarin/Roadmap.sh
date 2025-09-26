import requests

username = input("Enter Username: ")

url = f"https://api.github.com/users/{username}/events"

response = requests.get(url)

response = response.json()
print(response)