def convert_from_kelvin(value: int, new_unit: str):
    if new_unit == "celsius":
        result = value - 273.15
        return f"{value}K = {result}℃"
    
    if new_unit == "fahrenheit":
        result = ((value - 273.15) * 9/5 + 32)
        return f"{value}K = {result}℉"

def convert_from_celsius(value, new_unit):
    if new_unit == "kelvin":
        result = value + 273.15
        return f"{value}℃ = {result}K"
    
    if new_unit == "fahrenheit":
        result = (value* 5/9) + 32
        return f"{value}℃ = {result}℉"

def convert_from_fahrenheit(value, new_unit):
    if new_unit == "celsius":
        result = (value - 32) * 5/9
        return f"{value}℉ = {result}℃"
    if new_unit == "kelvin":
        result = ((value - 32) * 5/9) + 273.15
        return f"{value}℉ = {result}K"
    
def convert_temperature(value: int, unit: str, new_unit:str):
    if unit == "kelvin":
        return convert_from_kelvin(value, new_unit)

    if unit == "celsius":
        return convert_from_celsius(value, new_unit)
    
    if unit == "fahrenheit":
        return convert_from_fahrenheit(value, new_unit)
    

def convert_weight(value, unit, new_unit):
    ...

def convert_length(value, unit, new_unit):
    ...