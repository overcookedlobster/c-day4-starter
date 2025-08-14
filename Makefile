# Makefile for Day 4 C Assignments

# Compiler and flags
CC = gcc
CFLAGS = -Wall -Wextra -std=c11 -lm

# All targets to be built
all: shape_calculator basic_calculator

# Rule to build the shape calculator
shape_calculator: shape_calculator.c
	$(CC) $(CFLAGS) -o shape_calculator shape_calculator.c

# Rule to build the basic calculator (homework)
basic_calculator: basic_calculator.c
	$(CC) $(CFLAGS) -o basic_calculator basic_calculator.c

# Rule to run the python autograding tests
test:
	python3 tests.py

# Rule to clean up compiled files
clean:
	rm -f shape_calculator basic_calculator

