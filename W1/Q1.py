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

print(hex_to_int("11"))