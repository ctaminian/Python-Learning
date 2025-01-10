###############################################################################################################################

# 1. Parse JSON Response
# Write a function parse_instance_ids(response) that takes an AWS API response.
# The input can either be a dictionary or a JSON string, and the function should handle both cases.
# The function extracts all InstanceIds and returns them as a list.
# Example:
# Input:
# response = '{"Instances": [{"InstanceId": "i-1234567890abcdef0"}, {"InstanceId": "i-0abcdef1234567890"}]}'
# Output:
# ["i-1234567890abcdef0", "i-0abcdef1234567890"]

import json

response = '{"Instances": [{"InstanceId": "i-1234567890abcdef0"}, {"InstanceId": "i-0abcdef1234567890"}]}'

def parse_instance_ids(response):
    if isinstance(response, str):
        response = json.loads(response)
    return [instance["InstanceId"] for instance in response["Instances"]]

print(parse_instance_ids(response))

###############################################################################################################################

# 2. Check if a Key Exists in Configuration
# Write a function check_key(config, key) that checks if a specific key exists in a dictionary representing a configuration file.
# Example:
# Input:
# config = {"Region": "us-west-1", "InstanceType": "t2.micro"}  
# key = "Region"
# Output: True

config = {"Region": "us-west-1", "InstanceType": "t2.micro"}  
key = "Region"

def check_key(config, key):
    return key in config

print(check_key(config, key))

###############################################################################################################################

# 3. Validate S3 Bucket Name
# Write a function is_valid_bucket_name(name) that checks whether a given string is a valid S3 bucket name based on AWS naming rules
# (e.g., no uppercase letters, between 3 and 63 characters, etc.).
# Example:
# Input: "my-test-bucket"
# Output: True
# Input: "MyTestBucket"
# Output: False

import re

def is_valid_bucket_name(name):
    if not isinstance(name, str):
        return False
    if len(name) < 3 or len(name) > 63:
        return False
    if not re.match(r"^[a-z0-9-]+$", name):
        return False
    if not name[0].isalnum() or not name[-1].isalnum():
        return False
    if re.match(r"^\d+.\d+.\d+.\d+", name):
        return False
    return True

print(is_valid_bucket_name("my-test-bucket"))

###############################################################################################################################

# 4. Calculate Total Cost for EC2 Instances
# Write a function calculate_cost(prices, usage_hours) that takes a dictionary of instance types and their hourly prices, and a dictionary of instance usage in hours, and calculates the total cost.
# Example:
# Input:
# prices = {"t2.micro": 0.0116, "t2.large": 0.0928}  
# usage_hours = {"t2.micro": 100, "t2.large": 50}
# Output: 5.96

prices = {"t2.micro": 0.0116, "t2.large": 0.0928}  
usage_hours = {"t2.micro": 100, "t2.large": 50}

def calculate_cost(prices, usage_hours):
    total_cost = 0
    for instance, hours in usage_hours.items():
        if instance in prices:
            total_cost += prices[instance] * hours
    return total_cost

print(calculate_cost(prices, usage_hours))

###############################################################################################################################

# 5. Filter Logs by IP Address
# Write a function filter_logs(logs, ip) that filters a list of logs and returns only those that match a specific IP address.
# Example:
# Input:
# logs = [
#     "192.168.1.1 - GET /index.html",
#     "10.0.0.1 - POST /upload",
#     "192.168.1.1 - DELETE /file.txt"
# ]  
# ip = "192.168.1.1"
# Output:
# ["192.168.1.1 - GET /index.html", "192.168.1.1 - DELETE /file.txt"]

###############################################################################################################################

# 6. Simulate AWS CloudWatch Metrics
# Write a function simulate_metrics(cpu_usage, memory_usage) that takes a list of CPU usage percentages and memory usage values and formats them into a dictionary resembling CloudWatch metrics.
# Example:
# Input:
# cpu_usage = [45, 56, 78]  
# memory_usage = [2.1, 3.5, 4.0]
# Output:
# {"CPU": [45, 56, 78], "Memory": [2.1, 3.5, 4.0]}

###############################################################################################################################

# 7. Generate IAM Policy
# Write a function generate_iam_policy(resource, actions) that generates an IAM policy for the specified resource and actions.
# Example:
# Input:
# resource = "arn:aws:s3:::my-bucket/*"  
# actions = ["s3:GetObject", "s3:PutObject"]
# Output:
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": ["s3:GetObject", "s3:PutObject"],
#             "Resource": "arn:aws:s3:::my-bucket/*"
#         }
#     ]
# }

###############################################################################################################################

# 8. Check for Missing Tags
# Write a function check_missing_tags(resources, required_tags) that checks if any required tags are missing from a list of resources.
# Example:
# Input:
# resources = [
#     {"ResourceId": "i-123456", "Tags": {"Name": "AppServer"}},
#     {"ResourceId": "i-789012", "Tags": {"Environment": "Production"}}
# ]  
# required_tags = ["Name", "Environment"]
# Output:
# {"i-123456": ["Environment"], "i-789012": ["Name"]}

###############################################################################################################################