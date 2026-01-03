temperature_base_map = {
    "celsius": lambda c: c + 273.15,
    "fahrenheit": lambda c: ((c - 32) * 5/9) + 273.15,
    "kelvin": lambda c: c * 1
}

kelvin_map = {
    "fahrenheit": lambda c:((c - 273.15) * 9/5 + 32),
    "celsius": lambda c: c - 273.15,
    "kelvin": lambda c: c * 1
}
def convert_temperature(value, unit, new_unit):
    if new_unit in kelvin_map:
        base = temperature_base_map[unit](value)
        return round(kelvin_map[new_unit](base), 5)
    
weight_base_map = {
    "milligram": 0.001,
    "gram": 1,
    "kilogram": 1000,
    "ounce": 28.3495,
    "pound": 453.592
}

gram_map = {
    "milligram": 1000,
    "gram": 1,
    "kilogram": 0.001,
    "ounce": 0.03527,
    "pound": 0.002204
}

def convert_weight(value, unit, new_unit):
    if unit in weight_base_map:
        base = weight_base_map[unit] * value
        return round(base * gram_map[new_unit], 5)

length_base_map = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "feet": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34,
}

meter_map = {
    "millimeter": 1000,
    "centimeter": 100,
    "meter": 1,
    "kilometer": 0.001,
    "inch": 39.3071,
    "feet": 3.28084,
    "yard": 1.09361,
    "mile": 0.000621371,
}

def convert_length(value, unit, new_unit):
    if unit in length_base_map:
        base = length_base_map[unit] * value
        return round(base * meter_map[new_unit], 5)