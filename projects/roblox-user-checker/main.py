import requests

username = input("Enter a Roblox username: ")

flagged_groups = [1056909393, 905077734] # Group IDs

def get_user_info(username):
    user_data = {
    "usernames": [username],
    "excludeBannedUsers": False
    }
    
    req = requests.post('https://users.roblox.com/v1/usernames/users', json=user_data)
    response = req.json()

    if response["data"]:
        user_id = response["data"][0]["id"]
        name = response["data"][0]["name"]
        display_name = response["data"][0]["displayName"]
        return user_id, name, display_name
    else:
        return None


user_info = get_user_info(username)

if user_info:
    user_id, name, display_name = user_info
    print("Roblox Username: ", name)
    print("Display Name: ", display_name)
    print(f"Profile Link: https://roblox.com/users/{user_id}/profile")

# Get group information
    req = requests.get(f'https://groups.roblox.com/v1/users/{user_id}/groups/roles')
    response = req.json()
    # print(req.status_code)
    # print(response)

# Get inventory visibility status
    inv_req = requests.get(f'https://inventory.roblox.com/v1/users/{user_id}/can-view-inventory')
    inv_response = inv_req.json()
    # print(inv_req.status_code)
    # print(inv_response)

    if inv_response["canView"]:
        print("Inventory public?", "|", "Yes")
    else:
        print("Inventory public?", "|", "No")

# Loop thru user groups & print info about each group + find flagged groups based on list and print
    for group_info in response["data"]:
        group_name = group_info["group"]["name"]
        group_role = group_info["role"]["name"]
        group_rank = group_info["role"]["rank"]
        group_id = group_info["group"]["id"]

        if group_id in flagged_groups:
            print(f"Group: {group_name} | Role: {group_role} | Rank: {group_rank} | Flagged! ⚠️")
        else:
            print(f"Group: {group_name} | Role: {group_role} | Rank: {group_rank}")
else:
    print("Invalid username!")