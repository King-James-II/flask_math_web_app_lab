from flask import Flask, render_template, request
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def handle_non_numerical_input(route_function):
    def wrapper():
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        if not is_float(num1) or not is_float(num2):
            return "Invalid input. Please provide numerical values.", 400
        return route_function()
    return wrapper
    

@app.route("/sum")
@handle_non_numerical_input
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))

    result = summation(num1, num2)
    return str(result)

@app.route("/sub")
@handle_non_numerical_input
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = subtraction(num1, num2)
    return str(result)

@app.route("/mul")
@handle_non_numerical_input
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    result = multiplication(num1, num2)
    return str(result)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
