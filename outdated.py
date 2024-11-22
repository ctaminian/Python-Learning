months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ")

    if "/" in date:
        split_date = date.split("/")
        if len(split_date) == 3:
            month = int(split_date[0])
            day = int(split_date[1])
            year = split_date[2]
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
    else:
        split_date = date.replace(",", "").split(" ")
        if len(split_date) == 3:
            month_name = split_date[0].title()
            if month_name in months:
                month = months.index(month_name) + 1
                day = int(split_date[1])
                year = split_date[2]
                if 1 <= day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break