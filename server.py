from flask import Flask, render_template, request

# Create a Flask app instance named "Mathematics Problem Solver"
app = Flask("Mathematics Problem Solver")

# Function to check if a value can be converted to float
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Decorator to handle non-numerical input for route functions
def handle_non_numerical_input(route_function):
    def wrapper():
        # Get the input values from request arguments
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        
        # Check if both values are numerical
        if not is_float(num1) or not is_float(num2):
            # If not, return an error response
            return "Invalid input. Please provide numerical values.", 400
        # If both values are numerical, call the original route function
        return route_function()
    return wrapper

# Route for addition operation
@app.route("/sum")
@handle_non_numerical_input
def sum_route():
    # Get numerical values from request arguments
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    
    # Perform addition operation
    result = num1 + num2
    # Return the result as a string
    return str(result)

# Route for subtraction operation
@app.route("/sub")
@handle_non_numerical_input
def sub_route():
    # Get numerical values from request arguments
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    
    # Perform subtraction operation
    result = num1 - num2
    # Return the result as a string
    return str(result)

# Route for multiplication operation
@app.route("/mul")
@handle_non_numerical_input
def mul_route():
    # Get numerical values from request arguments
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    
    # Perform multiplication operation
    result = num1 * num2
    # Return the result as a string
    return str(result)

# Default route to render the index page
@app.route("/")
def render_index_page():
    # Render the index.html template
    return render_template('index.html')

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)