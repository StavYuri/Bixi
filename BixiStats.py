import csv
import math
from datetime import datetime


def calculate_total_extra_charges(exceeded_minutes, free_minutes_limit):
    total = 0
    for minutes in exceeded_minutes:
        if minutes <= free_minutes_limit:
            total += 1.8
        else:
            exceed_quarters = math.ceil((minutes - free_minutes_limit) / 15)
            total += (3 * exceed_quarters)
    return total


with open('/Users/yuristavchanskyy/PycharmProjects/Bixi/files/OD_2018-06.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    exceed_minutes_members = []
    exceed_minutes_non_members = []

    next(csv_reader)

    try:
        for row in csv_reader:
            start_date = datetime.strptime(row[0],"%Y-%m-%d %H:%M")
            end_date = datetime.strptime(row[2], "%Y-%m-%d %H:%M")
            is_member = row[5]
            difference_in_minutes = (end_date - start_date).total_seconds() / 60

            if is_member == '1' and difference_in_minutes > 45:
                exceed_minutes_members.append(difference_in_minutes)
            elif is_member == '0' and difference_in_minutes > 30:
                exceed_minutes_non_members.append(difference_in_minutes)

            line_count += 1

        print(len(exceed_minutes_members))
        print(len(exceed_minutes_non_members))

        print(calculate_total_extra_charges(exceed_minutes_members, 60))
        print(calculate_total_extra_charges(exceed_minutes_non_members, 45))

    except:
        print("Error")
    print(f'Processed {line_count} lines.')
