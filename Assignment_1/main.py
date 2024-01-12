import csv
import re


class TestCasesGenerator:
    def __init__(self, options):
        """
        Initialize the TestCasesGenerator object.

        Parameters:
        - options: List of options for test cases.
        """
        if not options or not options[0]:
            raise ValueError("Options list cannot be empty.")
        if any(re.search(r"[!@#$%^&*(),.?\":{}|<>]", option) for option in options):
            raise ValueError("Options should not contain special characters.")

        self.options = options
        self.test_cases = []
        self.combinations = []
        self.columns = []
        self.values = ["NA", "TRUE", "FALSE"]
        self.options_types = ["MASTER", "CLIENT"]

    def generate_combinations(self, current_test_case, n, i=0):
        """
        Generate all combinations based on values and options using recursion.

        Parameters:
        - current_test_case: Current state of the test case being generated.
        - n: Length of the test case.
        - i: Current index in the test case being processed.

        This function uses recursion to generate all possible combinations of values for the test case.
        The complexity  of the code is O(3^n). 3 due to the number of possible values.
        """
        if i == n:
            self.test_cases.append(current_test_case.copy())
            return
        for value in self.values:
            current_test_case[i] = value
            self.generate_combinations(current_test_case, n, i + 1)

    def generate_expected_output(self):
        """
        Generate the expected output based on generated test cases.

        For each generated test case, determine the expected output and update the test case accordingly.
        """
        for idx, test_case in enumerate(self.test_cases):
            current_test_case = test_case
            expected_options = ["TRUE" for _ in range(len(self.options))]
            valid = True
            # generating the expected options based on Master options
            for i in range(len(self.options)):
                if current_test_case[i] == "FALSE":
                    expected_options[i] = "FALSE"
            j = 0
            # Checking the validity of Client options
            for i in range(len(self.options), 2 * len(self.options)):
                if current_test_case[i] != "NA" and current_test_case[i] != expected_options[j]:
                    valid = False
                    break
                j += 1

            current_test_case.insert(0, idx + 1)
            if not valid:
                current_test_case.append("NO")
                current_test_case.extend(["NA" for _ in range(len(expected_options))])
            else:
                current_test_case.append("YES")
                current_test_case.extend(expected_options)

    def generate_headers(self):
        """
        Generate column headers for the CSV file based on options and option types.
        """
        self.columns.append("TestCase ID")
        for option_type in self.options_types:
            for option in self.options:
                self.columns.append(f"{option_type} Option For {option}")
        self.columns.append("Valid TC")

        for option in self.options:
            self.columns.append(f"Expected {option}")

    def generate_test_cases(self):
        """
        Generate test cases, expected output, and headers.
        """
        self.generate_headers()
        n = len(self.options_types) * len(self.options)
        initial_test_case = ["NA" for _ in range(n)]
        self.generate_combinations(initial_test_case, n)
        self.generate_expected_output()

    def display_test_cases(self):
        """
        Display the generated test cases.
        """
        if not self.test_cases:
            print("Test cases not generated. Call generate_test_cases() first.")
        else:
            for idx, test_case in enumerate(self.test_cases, 1):
                print(f"Test Case {idx}: {test_case}")

    def write_to_csv(self, csv_file_path):
        """
        Write generated test cases to a CSV file.

        Parameters:
        - csv_file_path: Path to the CSV file.
        """
        with open(csv_file_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)

            # Inserting the column headers
            csv_writer.writerow(self.columns)

            # Write the data
            for test_case in self.test_cases:
                csv_writer.writerow(test_case)


# Options can be edited here :
options_array = ["BufferData", "TimeOut"]

test_case_generator = TestCasesGenerator(options_array)
test_case_generator.generate_test_cases()
test_case_generator.write_to_csv("new_test_cases.csv")
