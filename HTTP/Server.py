from flask import Flask, request

app = Flask(__name__)

def main():
    app.run(host="127.0.0.1", port=8000)

@app.route('/sum')
def sum_command():
    try:
        c = 0
        for value in list(request.args.values()):
            c += int(value)

        html_response = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Sum Result</title>
        </head>
        <body>
            <h1>The result of {" + ".join(list(request.args.values()))} is: {c}</h1>
        </body>
        </html>
        """
        return html_response
    except ValueError:
        return "Invalid input. Please provide integers as 'a' and 'b'.", 400

@app.route('/average')
def average_command():
    try:
        c = 0
        i = 0
        for value in list(request.args.values()):
            c += int(value)
            i += 1
        c /= i

        html_response = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Sum Result</title>
        </head>
        <body>
            <h1>The result of {" and ".join(list(request.args.values()))}'s average is: {c}</h1>
        </body>
        </html>
        """
        return html_response
    except ValueError:
        return "Invalid input. Please provide integers as 'a' and 'b'.", 400

if __name__ == "__main__":
    main()
