from convert import *
test_values = [
    {"value": 50, "unit": "meter", "new_unit": "kilometer"},
    {"value": 100, "unit": "kilometer", "new_unit": "meter"}
    # {"value": 50, "unit": "meter", "new_unit": "kilometer"}
    # {"value": 50, "unit": "meter", "new_unit": "kilometer"}
]

expected_result = [0.05, 100000]
def test_convert_length():
    for i in range(len(test_values)):
        assert convert_length(**test_values[i]) == expected_result[i]
