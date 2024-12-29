instance_metadata = {
    "instance_id": "i-0123456789abcdef0",
    "region": "us-west-2",
    "tags": {
        "Name": "WebServer",
        "Environment": "Production",
        "Owner": "CloudTeam"
    },
    "instance_type": "t2.micro"
}

environment = instance_metadata["tags"]["Environment"]
print(environment)

if "Owner" not in instance_metadata["tags"]:
    instance_metadata["tags"]["Owner"] = "DefaultOwner"
else:
    print("Owner already exists")

for tag in instance_metadata["tags"].items():
    print(f"{tag[0]}: {tag[1]}")