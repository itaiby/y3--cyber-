def rotate(image, degrees):
    result = ""
    if degrees == 0:
        result = image
    elif degrees == 90:
        length = len(image.splitlines()[0])
        for i in range(length):
            for j in range(len(image.splitlines())-1,-1,-1):
                result += image[j*(length+1)+i]
            result += "\n"
    elif degrees == 180:
        result = image[::-1]
    elif degrees == 270:
        result = rotate(image[::-1],90)
    elif degrees == 360:
        for line in image.splitlines():
            result += line[::-1] + "\n"
    return result

def convert(image, convertion_table, conv_choice):
    result = ""
    for char in image:
        if char in [conv[0] for conv in convertion_table]:
            result += [conv[conv_choice] for conv in convertion_table if conv[0] == char][0]
        elif char == "\n":
            result += char
        else:
            result += "X"
    return result

def serialize(string, rotation, conv_choice, conversion_table, to_print=False):
    with open(string, "r") as file:
        rotated_and_converted = convert(rotate(file.read(), rotation), conversion_table, conv_choice)
        last = rotated_and_converted[0]
        i = 1
        result = ""
        for char in rotated_and_converted[1:]:
            if char == last:
                i += 1
            else:
                result += str(i) + last
                last = char
                i = 1
        if to_print:
            return result
        else:
            with open(string[0:string.find(".")]+"-output.txt", "w") as output:
                output.write(result)
                return output.name

def deserialize(string, rotation, conv_choice, conversion_table, to_print=False):
    with open(string, "r") as file:
        deserialized = ""
        num = ""
        for char in file.read():
            if char.isdigit():
                num += char
            else:
                deserialized += int(num) * char
                num = ""
        if rotation != 360 and rotation != 0:
            rotation = 360-rotation
        for i in range(len(conversion_table)):
            conversion_table[i] = conversion_table[i][::-1]
        result = convert(rotate(deserialized, rotation), conversion_table, conv_choice)
        if to_print:
            return result
        else:
            with open(string[0:string.find(".")]+"-output.txt", "w") as output:
                output.write(result)
                return output.name



#print(rotate("$$$$$***   ....\n&&&&&(,,/  ##))\n**   ****./,///", 180))
#print(convert("$$$$$***   ....\n&&&&&(,,/  ##))\n**   ****./,///",["(^$","$;!","*|#"],1))
#print(serialize("h.txt", 270, 2, ["h^$","f;!","w|#"],False))
#print(deserialize("h-output.txt", 270, 2, ["h^$","f;!","w|#"],True))