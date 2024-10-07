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

print(count_symbols("morse1.txt"))