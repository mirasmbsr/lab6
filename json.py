import json

# Load the JSON data from the file
with open("sample-data.json") as file:
    data = json.load(file)

# Extract the interface status information
interface_status = data["imdata"]

# Print the header
print("Interface Status")
print("=" * 80)
print("{:<50}{:<20}{:<10}{:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Iterate over the interface status data and print the information
for item in interface_status:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print("{:<50}{:<20}{:<10}{:<6}".format(dn, description, speed, mtu))