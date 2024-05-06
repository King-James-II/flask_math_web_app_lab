# Mathematics Problem Solver

This is a simple Flask web application that provides endpoints for basic mathematical operations such as addition, subtraction, and multiplication.

## Endpoints

- `/sum`: Accepts two numerical values as query parameters (`num1` and `num2`) and returns their sum.
- `/sub`: Accepts two numerical values as query parameters (`num1` and `num2`) and returns their difference.
- `/mul`: Accepts two numerical values as query parameters (`num1` and `num2`) and returns their product.

## Error Handling

The application handles non-numerical input gracefully and returns a 400 Bad Request error with a descriptive message.