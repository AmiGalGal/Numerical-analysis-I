import numpy as np
import matplotlib.pyplot as plt

def createfunc(value):
    return (1/(1+(value*value)))

def product(i, value, x):
    product = 1;
    for j in range(i):
        product = product * (value - x[j]);
    return product;


# Function for calculating
# divided difference table
def dividedDiffTable(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                       (x[j] - x[i + j]));
    return y;


# Function for applying Newton's
# divided difference formula
def CreateFormula(value, x, y, n):
    sum = y[0][0];

    for i in range(1, n):
        sum = sum + (product(i, value, x) * y[0][i]);

    return sum;


# Function for displaying divided
# difference table
def printDiffTable(y, n):
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t",
                  end=" ");

        print("");

for k in range (4):
    n = 5*(k+1)
    y = [[0 for i in range(n)] for j in range(n)]
    x = [0 for i in range (n)]
    if (n == 5):
        x = [-5.0, -2.5, 0.0, 2.5, 5.0]
        y[0][0] = 1/26
        y[1][0] = 4/29
        y[2][0] = 1
        y[3][0] = 4/29
        y[4][0] = 1/26
    if (n == 10):
        x = [-5, -35/9, -25/9, -5/3, -5/9, 5/9, 5/3, 25/9,35/9, 5]
        y[0][0] = 1 / 26
        y[1][0] = 81 / 1306
        y[2][0] = 81 / 706
        y[3][0] = 9 / 34
        y[4][0] = 81 / 106
        y[5][0] = 81 / 106
        y[6][0] = 9 / 34
        y[7][0] = 81 / 706
        y[8][0] = 81 / 1306
        y[9][0] = 1 / 26
    if (n == 15):
        x = [-5, -30/7, -25/7, -20/7, -15/7, -10/7, -5/7, 0, 5/7, 10/7, 15/7, 20/7, 25/7, 30/7, 5]
        y[0][0] = 1/26
        y[1][0] = 49/949
        y[2][0] = 49/674
        y[3][0] = 49/449
        y[4][0] = 49/274
        y[5][0] = 49/149
        y[6][0] = 49/74
        y[7][0] = 1
        y[8][0] = 49/74
        y[9][0] = 49/149
        y[10][0] = 49/274
        y[11][0] = 49/449
        y[12][0] = 49/674
        y[13][0] = 49/949
        y[14][0] = 1/26
    if (n == 20):
        x = [-5, -85/19, -75/19, -65/19, -55/19, -45/19, -35/19, -25/19, -15/19, -5/19, 5/19, 15/19, 25/19, 35/19, 45/19, 55/19, 65/19, 75/19, 85/19, 5 ]
        y[0][0] = 1 / 26
        y[1][0] = 361 / 7586
        y[2][0] = 361 / 5986
        y[3][0] = 361 / 4586
        y[4][0] = 361 / 3386
        y[5][0] = 361 / 2386
        y[6][0] = 361 / 1586
        y[7][0] = 361 / 986
        y[8][0] = 361 / 586
        y[9][0] = 361 / 386
        y[10][0] = 361 / 386
        y[11][0] = 361 / 586
        y[12][0] = 361 / 986
        y[13][0] = 361 / 1586
        y[14][0] = 361 / 2386
        y[15][0] = 361 / 3386
        y[16][0] = 361 / 4586
        y[17][0] = 361 / 5986
        y[18][0] = 361 / 7586
        y[19][0] = 1 / 26

    print("For n = ", n, "\n")
    y = dividedDiffTable(x, y, n);
    printDiffTable(y, n);
    if (n == 5):
        x_interpolated5 = np.linspace(min(x), max(x), 100)
        y_interpolated5 = [CreateFormula(val, x, y, n) for val in x_interpolated5]
    if (n == 10):
        x_interpolated10 = np.linspace(min(x), max(x), 100)
        y_interpolated10 = [CreateFormula(val, x, y, n) for val in x_interpolated10]
    if (n == 15):
        x_interpolated15 = np.linspace(min(x), max(x), 100)
        y_interpolated15 = [CreateFormula(val, x, y, n) for val in x_interpolated15]
    if (n == 20):
        x_interpolated20 = np.linspace(min(x), max(x), 100)
        y_interpolated20 = [CreateFormula(val, x, y, n) for val in x_interpolated20]

b = [createfunc(val) for val in x_interpolated20]


plt.plot(x_interpolated5, y_interpolated5, 'r',
         x_interpolated10, y_interpolated10, 'g',
         x_interpolated15, y_interpolated15, 'b',
         x_interpolated20, y_interpolated20, 'y',
         x_interpolated20, b, 'k')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton Divided Difference Formula')
plt.grid(True)
plt.show()
