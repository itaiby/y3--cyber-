def morse_file(file_path):
    with open(file_path, 'r') as file:
        try:
            return translate_morse(file.read().strip("\n"))
        except KeyError:
            return "Error in Morse Code"

def translate_morse(text):
    morse = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
        '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9',
        '/': ' '}
    try:
        return morse[text[0:text.index(" ")]] + translate_morse(text[text.index(" ")+1:])
    except ValueError:
        return morse[text]

def count_symbols(file_path):
    symbols = {}
    with open(file_path, 'r') as file:
        for chr in file.read():
            if chr != " ":
                if chr in symbols:
                    symbols[chr] += 1
                else:
                    symbols[chr] = 1
    return dict(sorted(symbols.items(), key=lambda item: item[1], reverse=True))

def print_count(symbols):
    last_count = list(symbols.values())[0]
    for symbol in symbols.items():
        if last_count != symbol[1]:
            print(f" - {last_count}")
        print(symbol[0].upper(), end='')
        last_count = symbol[1]
    print(f" - {last_count}")