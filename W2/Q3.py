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