from convert import *
length_test_values = [
    {"value": 50, "unit": "millimeter", "new_unit": "meter"},
    {"value": 50, "unit": "centimeter", "new_unit": "meter"},
    {"value": 50, "unit": "meter", "new_unit": "kilometer"},
    {"value": 50, "unit": "kilometer", "new_unit": "meter"},
    {"value": 50, "unit": "inch", "new_unit": "meter"},
    {"value": 50, "unit": "feet", "new_unit": "meter"},
    {"value": 50, "unit": "yard", "new_unit": "meter"},
    {"value": 50, "unit": "mile", "new_unit": "meter"},
]

expected_length_result = ['0.0500m', '0.5000m', '0.0500km', '50000m', '1.2700m', '15.2400m', '45.7200m', '80467.0000m']
def test_convert_length():
    for i in range(len(length_test_values)):
        assert convert_length(**length_test_values[i]) == expected_length_result[i]


weight_test_values = [
    {"value": 50, "unit": "milligram", "new_unit": "kilogram"},
    {"value": 50, "unit": "gram", "new_unit": "kilogram"},
    {"value": 50, "unit": "kilogram", "new_unit": "gram"},
    {"value": 50, "unit": "ounce", "new_unit": "kilogram"},
    {"value": 50, "unit": "pound", "new_unit": "kilogram"},
]
expected_weight_result = ['0.0001kg','0.0500kg','50000g','1.4175kg','22.6796kg']
def test_convert_weight():
    for i in range(len(weight_test_values)):
        assert convert_weight(**weight_test_values[i]) == expected_weight_result[i]


temperature_test_values = [
    {"value": 50, "unit": "celsius", "new_unit": "kelvin"},
    {"value": 50, "unit": "fahrenheit", "new_unit": "celsius"},
    {"value": 50, "unit": "kelvin", "new_unit": "celsius"},
]
expected_temperature_result = ['323.1500k','10.0000℃','-223.1500℃']
def test_convert_temperature():
    for i in range(len(temperature_test_values)):
        assert convert_temperature(**temperature_test_values[i]) == expected_temperature_result[i]
