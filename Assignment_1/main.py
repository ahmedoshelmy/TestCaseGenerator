from TestCasesGenerator import TestCasesGenerator

# Options can be edited here :
options_array = ["BufferData", "TimeOut"]

test_case_generator = TestCasesGenerator(options_array)
test_case_generator.generate_test_cases()
test_case_generator.write_to_csv("new_test_cases.csv")
