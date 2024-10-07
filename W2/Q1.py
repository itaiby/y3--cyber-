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