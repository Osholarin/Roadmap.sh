symbol_map = {
    "millimeter": "mm",
    "centimeter": "cm",
    "meter": "m",
    "kilometer": "km",
    "inch": "in",
    "feet": "ft",
    "yard": "yd",
    "mile": "mi",
    "milligram": "mg",
    "gram": "g",
    "kilogram": "kg",
    "ounce": "ou",
    "pound": "pd",
    "celsius": "℃",
    "fahrenheit": "℉",
    "kelvin": "k"
}
def pretty_print(new_unit, result):
    if isinstance(result, float):
        return f"{result:.4f}{symbol_map[new_unit]}"
    else:
        return f"{result}{symbol_map[new_unit]}"

def convert_length(value, unit, new_unit):
    """
    Convert length measurements between metric and imperial units.
    """

    # Conversion values to base unit
    to_meters = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1,
        "kilometer": 1000,
        "inch": 0.0254,
        "feet": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }

    # Conversion values from base to target units
    from_meters = {
        "millimeter": 1000,
        "centimeter": 100,
        "meter": 1,
        "kilometer": 0.001,
        "inch": 39.3701,
        "feet": 3.28084,
        "yard": 1.09361,
        "mile": 0.000621371
    }

    # validate units
    if unit not in to_meters:
        raise ValueError(f"Unkown length unit: {unit}")
    if new_unit not in from_meters:
        raise ValueError(f"Unkown length unit: {new_unit}")
    
    # conversion
    result_in_meter = to_meters[unit] * value
    return pretty_print(new_unit, result_in_meter * from_meters[new_unit])

def convert_weight(value, unit, new_unit):
    """
    Converts between units of weight
    """

    # Conversion values to base unit
    to_grams = {
        "milligram": 0.001,
        "gram": 1,
        "kilogram": 1000,
        "ounce": 28.3495,
        "pound": 453.592
    }

    # Conversion values from base to target unit
    from_grams = {
        "milligram": 1000,
        "gram": 1,
        "kilogram": 0.001,
        "ounce": 0.03527,
        "pound": 0.002204
    }

    # Validating input units
    if unit not in to_grams:
        raise ValueError(f"Unknown weight unit: {unit}")
    if new_unit not in from_grams:
        raise ValueError(f"Unknown weight unit: {new_unit}")
    
    # Convert to grams, then to target unit
    grams = to_grams[unit] * value
    return pretty_print(new_unit, grams * from_grams[new_unit])

def convert_temperature(value, unit, new_unit):
    """
    Convert temperature between celsius, fahrenheit, and kelvin.
    """
    # Conversion functions to Kelvin (base unit)
    to_kelvin = {
        "celsius": lambda c: c + 273.15,
        "fahrenheit": lambda f: ((f - 32) * 5/9) + 273.15,
        "kelvin": lambda k: k
    }
    
    # Conversion functions from Kelvin to target unit
    from_kelvin = {
        "celsius": lambda k: k - 273.15,
        "fahrenheit": lambda k: ((k - 273.15) * 9/5) + 32,
        "kelvin": lambda k: k
    }
    
    # Validate units
    if unit not in to_kelvin:
        raise ValueError(f"Unknown temperature unit: {unit}")
    if new_unit not in from_kelvin:
        raise ValueError(f"Unknown temperature unit: {new_unit}")
    
    # Converts to Kelvin, then to target unit
    kelvin_value = to_kelvin[unit](value)
    return pretty_print(new_unit, from_kelvin[new_unit](kelvin_value))
