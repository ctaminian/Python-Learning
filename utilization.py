def main():
    
    instances = [
    {
        "instance_id": "i-1",
        "region": "us-west-2",
        "resources": {
            "cpu": {"average_cpu_utilization": 15},
            "memory": {"average_memory_utilization": 45}
        }
    },
    {
        "instance_id": "i-2",
        "region": "us-east-1",
        "resources": {
            "cpu": {"average_cpu_utilization": 35},
            "memory": {"average_memory_utilization": 50}
        }
    },
    {
        "instance_id": "i-3",
        "region": "us-west-2",
        "resources": {
            "cpu": {"average_cpu_utilization": 10},
            "memory": {"average_memory_utilization": 25}
        }
    }
]

    print(get_underutilized_instances(instances))

def get_underutilized_instances(data):
    return {instance["instance_id"]: instance["resources"]["cpu"]["average_cpu_utilization"] for instance in data if instance["resources"]["cpu"]["average_cpu_utilization"] <= 20}

if __name__ == "__main__":
    main()