import json, requests

response = requests.get("https://api.github.com/repositories/132619461").text
objeto = json.loads(response)
assert objeto['owner']["login"] == "seatcode", "login key doesn´t correspond seatcode"
if objeto['owner']["login"] == "seatcode":
    print ("word seatcode is present in the field owner->login")
print ("login: " + objeto['owner']["login"])
