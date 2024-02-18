import re

def main():
    print(convert(input("Hours: ")))


def convert(time_range):
    pattern = r"[\s|to]+"  # Split on "+" or "-"
    split_list = re.split(pattern,time_range)
    start_time = split_list[0:2] # returns a list containing the start time and period (len = 2)
    end_time = split_list[2:] # returns a list containing the end time and period (len = 2)
    start_dict, end_dict = parse_time(start_time), parse_time(end_time)


    
    

def parse_time(time_str):
    time_dict = {}
    try:
        hour, minutes = time_str[0].split(':')
        period = time_str[-1]
        time_dict = {"hour": int(hour), "minutes": int(minutes), "period": period}
        # print(len(time_dict))
        # return time_dict
    except:
        hour, period = time_str[0], time_str[1]
        time_dict = {"hour": int(hour), "minutes": 0, "period": period}
        # print(len(time_dict))

    # hour_new_format = 0
    if 1 <= time_dict["period"] <= 12 and (time_dict["minutes"] < 60): 
        if time_dict["period"] == 'AM':
            if time_dict["hour"] == 12:
                time_dict["hour"] = 0
        elif time_dict["period"] == 'PM':
            if 1 <= time_dict["hour"] <= 11: 
                time_dict["hour"] = time_dict["hour"] + 12
    else:
        raise ValueError
    
    return time_dict


if __name__ == "__main__":
    main()

