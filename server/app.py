#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# default route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# route for printing parameter
@app.route('/print/<string:word>')
def print_string(word):
    print(word)
    return word

# route for counting range of the integer provided
@app.route('/count/<int:number>')
def count(number):
    numbers = '\n'.join(str(n) for n in range(number))
    return numbers + '\n'
    
# Route for performing operations
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error : Modulo by zero!"
    if result is not None:
        return str(result)  # Convert the result to string for consistency with test expectations
    else:
        return "Error: Invalid operation!"
            

if __name__ == '__main__':
    app.run(port=5555, debug=True)
