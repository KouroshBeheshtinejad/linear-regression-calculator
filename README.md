# Linear Regression Calculator

A simple Python program to calculate **linear regression** and **correlation coefficient** from user-provided data points, with visualization.

## Features
- Accepts custom **x** and **y** values from user input.
- Calculates:
  - Regression line equation (`y = mx + b`)
  - Correlation coefficient (**r**)
- Plots the scatter points and regression line using **Matplotlib**.
- Handles invalid inputs gracefully.


## How It Works
1. User enters values for `x` and `y` until they type `-1` to stop.
2. The program:
   - Computes the slope (**m**) and intercept (**b**).
   - Calculates correlation coefficient (**r**).
   - Displays the scatter plot with the regression line.


## Example Output
enter -1 for end the while loop!
Determine the length of two arrays and array elements x: 1
Declare the values of the array elements y: 2
...
Regression line equation: y = 0.8571x + 1.1429
Correlation coefficient: 0.9648


## Visualization
- **Blue dots** → Input data points  
- **Red line** → Best-fit regression line


## Requirements
- Python 3.x
- NumPy
- Matplotlib

Install dependencies:
```bash
pip install numpy matplotlib

Run
python regression.py

License
This project is open-source and free to use.

Author: Kourosh Beheshtinejad