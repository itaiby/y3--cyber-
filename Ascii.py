def rotate(image, degrees):
    result = []
    if degrees == 360:
        for line in image.splitlines():
            mirror_line = ""
            for char in line[::-1]:
                if char == "(":
                    mirror_line += ")"
                elif char == ")":
                    mirror_line += "("
                else:
                    mirror_line += char
            result.append(mirror_line)
        return '\n'.join(result)

    elif degrees == 0:
        return image

    for row in zip(*(image.splitlines()[::-1])):
        result.append(''.join(row))
    return rotate('\n'.join(result), degrees - 90)

def convert(image, conversion_table, conv_choice):
    result = ""
    if conv_choice == 0:
        return image
    for char in image:
        if char == "\n":
            result += char
        in_table = False
        for conv in conversion_table:
            if conv[0] == char:
                result += conv[conv_choice]
                in_table = True
                break
        if not in_table:
            result += "X"
    return result

def serialize(string, rotation, conv_choice, conversion_table, to_print=False):
    string = convert(rotate(string,rotation),conversion_table, conv_choice)
    last = string[0]
    count = 1
    result = ""
    for char in string[1:]:
        if char == "\n":
            result += char
        elif char == last:
            count += 1
        else:
            result += f"{count}{last}"
            last = char
            count = 1
    result += f"{count}{last}"

    if to_print:
        return result
    else:
        with open("output.txt", "w") as output:
            output.write(result)
            return output.name

def deserialize(string, rotation, conv_choice, conversion_table, to_print=False):
    num = ""
    result = ""
    for char in string:
        if char.isdigit():
            num += char
        else:
            result += int(num) * char
            num = ""

    if rotation in [90,270]:
        rotation = 360-rotation

    reversed_conversion_table = [conv[::-1] for conv in conversion_table]
    result = convert(rotate(result, rotation), reversed_conversion_table, conv_choice)

    if to_print:
        return result
    else:
        with open("output.txt", "w") as output:
            output.write(result)
            return output.name