def main():

    instances = [
        {"instance_id": "i-1", "region": "us-west-2"},
        {"instance_id": "i-2", "region": "us-east-1"},
        {"instance_id": "i-3", "region": "us-west-2"}
    ]

    print(filter_instances_by_region(instances, "us-west-2"))

def filter_instances_by_region(server_list, region):
    return [item["instance_id"] for item in server_list if item["region"] == region]

    # Using filter and map to achieve the same thing
    # filtered_list =  list(filter(lambda item: item["region"] == region, server_list))
    # return list(map(lambda lst: lst["instance_id"], filtered_list))

if __name__ == "__main__":
    main()