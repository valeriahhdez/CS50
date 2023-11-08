import re

def validate(s):
    values = s.split('/')
    return len(values) == 2 and all(i.isdigit() for i in values)

while True:
    
    try: 
        input_fraction = input("FRaction: ")
        numbers = re.findall(r'\d+',input_fraction)
        num_1, num_2 = [int(n) for n in numbers]

        if validate(input_fraction) and (num_1 <= num_2):
            percentage = round(num_1/num_2 * 100)
            if 99 <= percentage:
                gauge_output ="F"
            elif percentage <= 1:
                gauge_output ="E"
            elif 1 < percentage < 99:
                gauge_output =f"{percentage}%"
            break

    except ValueError:
        print("Fraction does not have integers")
    except num_1 > num_2:
        print("Invalid fraction")
    except ZeroDivisionError:
        print("The denominator can't be 0")

print(gauge_output)

