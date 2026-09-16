import requests

username = input("Enter a Roblox username: ")

user_data = {
    "usernames": [username],
    "excludeBannedUsers": False
}

flagged_groups = [1056909393, 905077734]


req = requests.post('https://users.roblox.com/v1/usernames/users', json=user_data)
response = req.json()

if response["data"]:
    user_id = response["data"][0]["id"]
    name = response["data"][0]["name"]
    display_name = response["data"][0]["displayName"]

    print("Roblox Username: ", name)
    print("Display Name: ", display_name)
    print(f"Profile Link: https://roblox.com/users/{user_id}/profile")

    req = requests.get(f'https://groups.roblox.com/v1/users/{user_id}/groups/roles')
    response = req.json()
    print(req.status_code)
    # print(response)

    for group_info in response["data"]:
        print("Group:", group_info["group"]["name"], "|", "Rank:", group_info["role"]["name"])

    for group in flagged_groups:
        for group_info in response["data"]:
            if group == group_info["group"]["id"]:
                print(group , "IS FLAGGED!")

else:
    print("Invalid username!")