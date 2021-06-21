import requests
import json

from requests.api import head 
BASE = "https://dev-40888608.okta.com"
HEADERS = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "SSWS00zfzbXULR-8n3ESRvgoyJVduTX5QIsFGwElNO9-k0"
}
user_id = "00u11sghrogCnZR195d7"

def list_users():
    response = requests.get(BASE + "/api/v1/users", headers=HEADERS)
    json_response = response.json();
    for user_profile in json_response:
        print(user_profile, "\n")

def create_user():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    email = input("Enter the email: ")
    login = input("Enter the login: ")
    user = {
        "profile": 
        {
            "firstName": first_name, 
            "lastName": last_name, 
            "email": email, 
            "login": login
        }
    }
    
    user_data = json.dumps(user);
    response = requests.post(BASE + "/api/v1/users?activate=true", data=user_data, headers=HEADERS)
    print(response.status_code);
    print(response.json());

def update_user():
    updated_data = {
        "profile": {
            "lastName": "Nadigoti",
        }
    }
    updated_data_json = json.dumps(updated_data)
    response = requests.post(BASE + "/api/v1/users/" + user_id, headers=HEADERS, data= updated_data_json);
    print(response.json())
    print(response.status_code);

def reactivate_user():
    
    reactivation_url = BASE + "/api/v1/users/" + user_id + "/lifecycle/reactivate?sendEmail=false"
    response = requests.post(reactivation_url, headers=HEADERS)
    print(response.status_code)
    print(response.json());

def fetch_user():
    user_id = input("Enter the user id: ")
    fetch_url = BASE + "/api/v1/users/" + user_id;
    response = requests.get(fetch_url, headers=HEADERS)
    json_response = response.json()
    print(json_response['profile'])

def get_app_links():
    user_id = input("Enter the user id: ")
    app_link_url = BASE + "/api/v1/users/" + user_id + "/appLinks"
    response = requests.get(app_link_url, headers=HEADERS)
    print(response.json())

def get_users_groups():
    user_id = "me"
    user_groups_url = BASE + "/api/v1/users/" + user_id + "/groups"
    response = requests.get(user_groups_url, headers=HEADERS)
    print(response.json())

def activate_user():
    user_id = input("Enter the user id: ")
    activation_url = BASE + "/api/v1/users/" + user_id + "/lifecycle/activate?sendEmail=false"
    response = requests.post(activation_url, headers=HEADERS)
    print(response.json())

def suspend_user():
    user_id = input("Enter the user id: ")
    suspend_url = BASE + "/api/v1/users/" + user_id + "/lifecycle/suspend"
    response = requests.post(suspend_url, headers=HEADERS)
    print(response.json())

def exit_menu():
    exit()

while True:
    print("1.Create user \n2.List users \n3.Update user \n4.Reactivate user\n5.Fetch user details\n6.Get app links \n7.activate user \n8.Suspend user ")
    [create_user, list_users, update_user, reactivate_user, fetch_user, get_app_links, activate_user, suspend_user, exit_menu][int(input("Enter your choice: ")) - 1]()
# get_users_groups()
activate_user()
