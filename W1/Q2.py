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

result = hex_summary("ABRAKADABRA")
print(result)
print(decimal_to_base(8, result))
print(decimal_to_base(2, result))
