# Day 4 C: Basics & Shape Calculator

Welcome to Day 4! Today we switch gears from Python to C, a powerful and widely-used programming language. C is a **compiled language**, which introduces a few new steps to our workflow.

## From Python to C: What's New?

-   **Compilation**: Unlike Python, which is interpreted, C code must be compiled into an executable file before it can be run. We will use a compiler called `gcc`.
-   **`Makefile`**: To make compiling easy, we will use a `Makefile`. You won't need to write this file, but you will use it. To compile all your programs, you'll just run the command `make` in your terminal.
-   **Boilerplate**: Every C program needs a `main` function (`int main() { ... }`), and you must `#include <stdio.h>` to handle input/output.
-   **Static Types**: You must declare the type of every variable (e.g., `int`, `float`, `char`).
-   **Syntax**: Pay attention to the details! Lines in C end with a semicolon `;`, and code blocks are enclosed in curly braces `{}`.

## Sub-Task 1: C Shape Area Calculator
-   **File to edit:** `shape_calculator.c`
-   **Goal:** Write a C program that calculates the area of a circle, rectangle, or triangle based on user input. This will teach you C variables, `printf` (for output), `scanf` (for input), and `if/else if/else` for logic.
-   **To Compile & Run**:
    1.  `make shape_calculator`
    2.  `./shape_calculator`

## Homework: Basic Arithmetic Calculator
-   **File to edit:** `basic_calculator.c`
-   **Goal:** Reinforce your C skills by creating a calculator that performs addition, subtraction, multiplication, and division. This is a great exercise for practicing with the `switch` statement.
-   **To Compile & Run**:
    1.  `make basic_calculator`
    2.  `./basic_calculator`

## Instructions
1.  Review the new C concepts.
2.  Edit the `.c` files to complete the `// TODO:` sections.
3.  Use the `make` command to compile your code. Test it yourself before pushing.
4.  Push your code to GitHub to run the autograding tests. All tests must pass.
