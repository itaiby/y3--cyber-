import statistics

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


print(get_input_average(), "\n")
# challenge
print(get_input_median(), "\n")
# ultra challenge
print(statistics.median(get_input_list()))