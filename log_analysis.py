def main():

    logs = [
        {"status_code": 200, "response_time": 120, "endpoint": "/login"},
        {"status_code": 500, "response_time": 350, "endpoint": "/create-user"},
        {"status_code": 200, "response_time": 90, "endpoint": "/get-data"},
        {"status_code": 503, "response_time": 420, "endpoint": "/login"},
        {"status_code": 404, "response_time": 50, "endpoint": "/update-user"},
        {"status_code": 200, "response_time": 600, "endpoint": "/create-user"},
        {"status_code": 503, "response_time": 700, "endpoint": "/login"}
    ]

    print(get_failed_requests(logs))
    print(get_slow_requests(logs))
    print(get_most_failed_requests(logs))

def get_failed_requests(logs):
    return [log for log in logs if log["status_code"] >= 500]

def get_slow_requests(logs):
    filtered_list = list(filter(lambda log: log["response_time"] > 400, logs))
    final_list = {}
    for item in filtered_list:
        if item["endpoint"] not in final_list:
            final_list[item["endpoint"]] = [item["response_time"]]
        else:
            final_list[item["endpoint"]].append(item["response_time"])
    return final_list

def get_most_failed_requests(logs):
    failed_requests = list(filter(lambda log: log["status_code"] >= 500, logs))
    new_list = {}
    for item in failed_requests:
        if item["endpoint"] not in new_list:
            new_list[item["endpoint"]] = 1
        else:
            new_list[item["endpoint"]] += 1
    sorted_dict = dict(sorted(new_list.items(), key=lambda item: item[1], reverse=True))
    return [next(iter(sorted_dict))]

if __name__ == "__main__":
    main()