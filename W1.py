def hex_to_int(str):
    # dict for translating hex to int
    hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    # removing the first 0x if found
    str = (str[:2] * (not str.startswith("0x"))) + str[2:]
    sum = 0
    i = 1
    for ch in str[::-1]:
        try:
            sum += hex[ch] * i
            i *= 16
        except KeyError:
            return "invalid hex number"
    return sum

def hex_summary(str):
    # dict for translating hex to int
    hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    # handling uppercase chars too
    str = str.lower()
    # creating another str from who to strip as we go along the chars we passed
    striped_str = str
    sum = 0
    i = 1
    for ch in str[::-1]:
        try:
            striped_str = striped_str.rstrip(ch)
            sum += hex[ch] * i
            i *= 16
        except KeyError:
            return sum + hex_summary(striped_str)
    return sum

def decimal_to_base(base, num):
    left_over = num
    result = ""
    while left_over != 0:
        result = str(left_over % base) + result
        left_over = int(left_over / base)
    return result

def get_input_list():
    try:
        return [int(input()),] + get_input_list()
    except ValueError:
        return []

def get_input_median():
    list = []
    num = input()
    while num.isdigit():
        list.append(int(num))
        num = input()
    list.sort()
    n = len(list)
    if n % 2 == 0:
        return (list[int((n/2)-1)] + list[int(n/2)]) / 2
    else:
        return list[int(n/2)]

def get_input_average(sum=0, size=0):
    num = input()
    if not num.isdigit():
        return sum/size
    return get_input_average(sum+int(num), size+1)
