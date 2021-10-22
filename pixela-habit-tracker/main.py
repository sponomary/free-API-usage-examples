"""Pixela API documentation: https://docs.pixe.la/"""

import requests
from datetime import datetime

USERNAME = "{your_username}"  # to reach created account: https://pixe.la/@{your_username}
TOKEN = "{your_secret_password}"
GRAPH_ID_1 = "walking"  # must follow rule: [a-z][a-z0-9-]{1,16}
GRAPH_ID_2 = "reading"

# -------------------------------------------------------------------------
# CREATING A PIXELA USER (post request)
# -------------------------------------------------------------------------
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(pixela_endpoint, json=user_params)
print(f'Pixela\'s new user: {response.text}')

# -------------------------------------------------------------------------0
# CREATING A GRAPH (post request)
# -------------------------------------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config_1 = {
    "id": GRAPH_ID_1,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",  # shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) or kuro (black)
}

graph_config_2 = {
    "id": GRAPH_ID_2,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response_1 = requests.post(url=graph_endpoint, json=graph_config_1, headers=headers)
response_2 = requests.post(url=graph_endpoint, json=graph_config_2, headers=headers)
print(f'Pixela\'s new graph for {GRAPH_ID_1}: {response_1.text}')
print(f'Pixela\'s new graph for {GRAPH_ID_2}: {response_2.text}')

# -------------------------------------------------------------------------
# CREATING A PIXEL (post request)
# -------------------------------------------------------------------------
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID_1}"

today = datetime.now()
# other date: date = datetime(year=2021, month=6, day=17)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you walk today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(f'New data added: {response.text}')

# -------------------------------------------------------------------------
# UPDATING A PIXEL (put request)
# -------------------------------------------------------------------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID_1}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.7",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(f'Data updated: {response.text}')

# -------------------------------------------------------------------------
# DELETING A PIXEL (delete request)
# -------------------------------------------------------------------------
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID_1}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(f'Data deleted: {response.text}')
