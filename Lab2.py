import statistics


def display_main_menu () :
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input () :
    print("get user input")
    x = input()
    y = x.split(", ")
    mylist = y
    #print(mylist)
    float_mylist = []
    for item in mylist :
        float_mylist.append(float(item))
    #print(float_mylist)
    return float_mylist
def calc_average () :
    average = sum(list) / len(list)
    print("The Average is ")
    print(average)
def find_min_max () :
    minimum = min(list)
    maximum = max(list)
    print("The minimum value is ")
    print(minimum)
    print("The maximum value is ")
    print(maximum)

def sort_temperature () :
    temp_sort = sorted(list)
    print(temp_sort)
    return temp_sort

def calc_median_temperature () :
    Tmedian = statistics.median(sort)
    print("Median is ")
    print(Tmedian)

display_main_menu()
list = get_user_input()
calc_average()
find_min_max()
sort = sort_temperature()
calc_median_temperature()