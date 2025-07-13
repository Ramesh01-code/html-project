# 🧮 Calculator App

A feature-rich calculator application built with Python and Streamlit framework.

## Features

### Basic Operations
- Addition (+)
- Subtraction (−)
- Multiplication (×)
- Division (÷)
- Decimal point support
- Clear (C) and backspace (⌫) functions
- Plus/minus toggle (±)

### Scientific Functions
- Square root (√)
- Trigonometric functions (sin, cos, tan) - input in degrees
- Logarithm (log base 10)
- Square (x²)
- Cube (x³)
- Reciprocal (1/x)
- Pi (π) constant

### User Interface
- Clean, modern design with responsive layout
- Large, easy-to-read display
- Intuitive button layout similar to physical calculators
- Error handling for invalid operations
- Hover effects on buttons

## Installation

1. Make sure you have Python 3.7+ installed on your system
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory
2. Run the Streamlit app:

```bash
streamlit run calculator_app.py
```

3. The app will open in your default web browser at `http://localhost:8501`

## How to Use

1. Click on number buttons to input numbers
2. Click on operation buttons (+, −, ×, ÷) to perform calculations
3. Press "=" to get the result
4. Use "C" to clear everything
5. Use "⌫" to delete the last digit
6. Use "±" to toggle between positive and negative numbers
7. Use scientific functions for advanced calculations

## Features in Detail

- **Memory Management**: The calculator maintains state between operations
- **Error Handling**: Division by zero and invalid operations show "Error"
- **Decimal Support**: Full decimal number support
- **Scientific Functions**: Trigonometric functions work with degrees
- **Responsive Design**: Works well on different screen sizes

## Technical Details

- Built with Streamlit for the web interface
- Uses Python's built-in `math` module for calculations
- Session state management for calculator memory
- Custom CSS styling for improved appearance
- Modular function design for easy maintenance

## Browser Support

The calculator app works in all modern web browsers including:
- Chrome
- Firefox
- Safari
- Edge

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests

## License

This project is open source and available under the MIT License.