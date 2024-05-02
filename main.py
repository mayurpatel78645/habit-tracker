import requests
import datetime as dt

USERNAME = "enigma"
TOKEN = "djf;afj;aslfjk"
GRAPH_ID = "graph1"

user_params = {
    "username": USERNAME,
    "token": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
pixela_endpoint = "https://pixe.la/v1/users"
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
dt = dt.datetime
today = dt.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many commits did you write today? "),
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)