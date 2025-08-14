// Day 4 C: Shape Area Calculator
#include <stdio.h>
#include <string.h> // Required for strcmp()

// Define a constant for PI
#define PI 3.14159

int main() {
    char shape[20];
    printf("Enter the shape (circle, rectangle, triangle): ");
    scanf("%s", shape);

    // Use strcmp() to compare strings in C. It returns 0 if they are equal.
    if (strcmp(shape, "circle") == 0) {
        float radius, area;
        // TODO: Prompt the user to enter the radius.
        // TODO: Read the radius from user input using scanf().
        // TODO: Calculate the area of the circle (PI * radius * radius).
        // TODO: Print the result in the format "Area: <value>\n".
        printf("Area: 0.0\n"); // Placeholder

    } else if (strcmp(shape, "rectangle") == 0) {
        float length, width, area;
        // TODO: Prompt for and read the length and width.
        // TODO: Calculate the area.
        // TODO: Print the result.
        printf("Area: 0.0\n"); // Placeholder

    } else if (strcmp(shape, "triangle") == 0) {
        float base, height, area;
        // TODO: Prompt for and read the base and height.
        // TODO: Calculate the area (0.5 * base * height).
        // TODO: Print the result.
        printf("Area: 0.0\n"); // Placeholder
        
    } else {
        printf("Invalid shape!\n");
    }

    return 0; // Indicates successful execution
}

