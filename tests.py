import unittest
import subprocess
import os

class TestDay4C(unittest.TestCase):

    def run_c_executable(self, executable_name, inputs, expected_substring):
        """Compiles and runs a C executable, provides input, and checks output."""
        # Ensure the executable exists
        self.assertTrue(os.path.exists(executable_name), f"Executable '{executable_name}' not found. Did it compile?")

        # Run the executable as a subprocess
        process = subprocess.run(
            [f'./{executable_name}'],
            input='\n'.join(map(str, inputs)),
            capture_output=True,
            text=True,
            timeout=5
        )

        # Check for runtime errors
        self.assertIsNone(process.stderr or None, f"Runtime error: {process.stderr}")

        # Check for expected output
        output = process.stdout.strip()
        self.assertIn(expected_substring, output, f"Expected '{expected_substring}', got '{output}'")

    # In-Class: Shape Calculator Tests
    def test_shape_circle(self):
        self.run_c_executable("shape_calculator", ["circle", "10"], "Area: 314.159")

    def test_shape_rectangle(self):
        self.run_c_executable("shape_calculator", ["rectangle", "5", "4"], "Area: 20.0")

    def test_shape_triangle(self):
        self.run_c_executable("shape_calculator", ["triangle", "10", "5"], "Area: 25.0")

    def test_shape_invalid(self):
        self.run_c_executable("shape_calculator", ["square"], "Invalid shape!")

    # Homework: Basic Calculator Tests
    def test_calculator_add(self):
        self.run_c_executable("basic_calculator", ["10 + 5"], "Result: 15.0")

    def test_calculator_subtract(self):
        self.run_c_executable("basic_calculator", ["10 - 5"], "Result: 5.0")

    def test_calculator_multiply(self):
        self.run_c_executable("basic_calculator", ["10 * 5"], "Result: 50.0")

    def test_calculator_divide(self):
        self.run_c_executable("basic_calculator", ["10 / 4"], "Result: 2.5")

    def test_calculator_div_by_zero(self):
        self.run_c_executable("basic_calculator", ["10 / 0"], "Error: Division by zero")

    def test_calculator_invalid_op(self):
        self.run_c_executable("basic_calculator", ["10 % 5"], "Error: Invalid operator")

if __name__ == '__main__':
    # We can't run tests if the code hasn't been compiled.
    # The YAML file will handle the compilation step first.
    if os.path.exists('shape_calculator') and os.path.exists('basic_calculator'):
        unittest.main()
    else:
        print("Executables not found. Please run 'make' first.")

