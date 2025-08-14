// Day 4 C HW: Basic Calculator
#include <stdio.h>

int main() {
    char operator;
    float num1, num2, result;

    printf("Enter an expression (e.g., 5 + 3): ");
    // scanf can read multiple values at once.
    // The space before %c is important to consume any leftover whitespace.
    scanf("%f %c %f", &num1, &operator, &num2); 

    switch (operator) {
        case '+':
            // TODO: Calculate the sum.
            break;
        case '-':
            // TODO: Calculate the difference.
            break;
        case '*':
            // TODO: Calculate the product.
            break;
        case '/':
            // TODO: Check if num2 is 0. If it is, print "Error: Division by zero\n" and exit.
            // Otherwise, calculate the quotient.
            break;
        default:
            printf("Error: Invalid operator\n");
            return 1; // Indicate an error
    }

    // TODO: Print the result in the format "Result: <value>\n".
    // Make sure this line doesn't execute if there was an error.

    return 0;
}

