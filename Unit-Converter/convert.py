# Functions for temperature conversion
def convert_from_kelvin(value, new_unit):
    if new_unit == "celsius":
        result = value - 273.15
        return f"{value}K = {result:.2f}℃"
    
    if new_unit == "fahrenheit":
        result = ((value - 273.15) * 9/5 + 32)
        return f"{value}K = {result:.2f}℉"

def convert_from_celsius(value, new_unit):
    if new_unit == "kelvin":
        result = value + 273.15
        return f"{value}℃ = {result:.2f}K"
    
    if new_unit == "fahrenheit":
        result = (value * 9/5) + 32  # FIXED: was 5/9, should be 9/5
        return f"{value}℃ = {result:.2f}℉"

def convert_from_fahrenheit(value, new_unit):
    if new_unit == "celsius":
        result = (value - 32) * 5/9
        return f"{value}℉ = {result:.2f}℃"
    if new_unit == "kelvin":
        result = ((value - 32) * 5/9) + 273.15
        return f"{value}℉ = {result}K"
    
def convert_temperature(value, unit, new_unit):
    if unit == "kelvin":
        return convert_from_kelvin(value, new_unit)

    if unit == "celsius":
        return convert_from_celsius(value, new_unit)
    
    if unit == "fahrenheit":
        return convert_from_fahrenheit(value, new_unit)
    
# Functions for weight
def convert_from_milligram(value, new_unit):
    if new_unit == "gram":
        result = value / 1000
        return f"{value}mg = {result:.2f}g"
    if new_unit == "kilogram":
        result = value / 1000000
        return f"{value}mg = {result:.2f}kg"
    if new_unit == "ounce":
        result = value / 28349.52
        return f"{value}mg = {result:.2f}oz"
    if new_unit == "pound":
        result = value / 453592.37
        return f"{value}mg = {result:.2f}lb"

def convert_from_gram(value, new_unit):
    if new_unit == "milligram":
        result = value * 1000
        return f"{value}g = {result:.2f}mg"
    if new_unit == "kilogram":
        result = value / 1000
        return f"{value}g = {result:.2f}kg"
    if new_unit == "ounce":
        result = value / 28.3495
        return f"{value}g = {result:.2f}oz"
    if new_unit == "pound":
        result = value / 453.592
        return f"{value}g = {result:.2f}lb"


def convert_from_kilogram(value, new_unit):
    if new_unit == "milligram":
        result = value * 1000000
        return f"{value}kg = {result:.2f}mg"
    if new_unit == "gram":
        result = value * 1000
        return f"{value}kg = {result:.2f}g"
    if new_unit == "ounce":
        result = value * 35.274
        return f"{value}kg = {result:.2f}oz"
    if new_unit == "pound":
        result = value * 2.20462
        return f"{value}kg = {result:.2f}lb"

def convert_from_ounce(value, new_unit):
    if new_unit == "milligram":
        result = value * 28349.52
        return f"{value}oz = {result:.2f}mg"
    if new_unit == "gram":
        result = value * 28.3495
        return f"{value}oz = {result:.2f}g"
    if new_unit == "kilogram":
        result = value / 35.274
        return f"{value}oz = {result:.2f}kg"
    if new_unit == "pound":
        result = value / 16
        return f"{value}oz = {result:.2f}lb"

def convert_from_pound(value, new_unit):
    if new_unit == "milligram":
        result = value * 453592.37
        return f"{value}lb = {result:.2f}mg"
    if new_unit == "gram":
        result = value * 453.592
        return f"{value}lb = {result:.2f}g"
    if new_unit == "kilogram":
        result = value / 2.20462
        return f"{value}lb = {result:.2f}kg"
    if new_unit == "ounce":
        result = value * 16
        return f"{value}lb = {result:.2f}oz"

def convert_weight(value, unit, new_unit):
    if unit == "milligram":
        return convert_from_milligram(value, new_unit)
    if unit == "gram":
        return convert_from_gram(value, new_unit)
    if unit == "kilogram":
        return convert_from_kilogram(value, new_unit)
    if unit == "ounce":
        return convert_from_ounce(value, new_unit)
    if unit == "pound":
        return convert_from_pound(value, new_unit)


# Conversion function for length
def convert_from_millimeter(value, new_unit):
    if new_unit == "centimeter":
        result = value / 10
        return f"{value}mm = {result:.2f}cm"
    if new_unit == "meter":
        result = value / 1000
        return f"{value}mm = {result:.2f}m"
    if new_unit == "kilometer":
        result = value / 1000000
        return f"{value}mm = {result:.2f}km"
    if new_unit == "inch":
        result = value / 25.4
        return f"{value}mm = {result:.2f}in"
    if new_unit == "feet":
        result = value / 304.8
        return f"{value}mm = {result:.2f}ft"
    if new_unit == "yard":
        result = value / 914.4
        return f"{value}mm = {result:.2f}yd"
    if new_unit == "mile":
        result = value / 1609344
        return f"{value}mm = {result:.2f}mi"

def convert_from_centimeter(value, new_unit):
    if new_unit == "millimeter":
        result = value * 10
        return f"{value}cm = {result:.2f}mm"
    if new_unit == "meter":
        result = value / 100
        return f"{value}cm = {result:.2f}m"
    if new_unit == "kilometer":
        result = value / 100000
        return f"{value}cm = {result:.2f}km"
    if new_unit == "inch":
        result = value / 2.54
        return f"{value}cm = {result:.2f}in"
    if new_unit == "feet":
        result = value / 30.48
        return f"{value}cm = {result:.2f}ft"
    if new_unit == "yard":
        result = value / 91.44
        return f"{value}cm = {result:.2f}yd"
    if new_unit == "mile":
        result = value / 160934.4
        return f"{value}cm = {result:.2f}mi"

def convert_from_meter(value, new_unit):
    if new_unit == "millimeter":
        result = value * 1000
        return f"{value}m = {result:.2f}mm"
    if new_unit == "centimeter":
        result = value * 100
        return f"{value}m = {result:.2f}cm"
    if new_unit == "kilometer":
        result = value / 1000
        return f"{value}m = {result:.2f}km"
    if new_unit == "inch":
        result = value * 39.3701
        return f"{value}m = {result:.2f}in"
    if new_unit == "feet":
        result = value * 3.28084
        return f"{value}m = {result:.sf}ft"
    if new_unit == "yard":
        result = value * 1.09361
        return f"{value}m = {result:.2f}yd"
    if new_unit == "mile":
        result = value / 1609.344
        return f"{value}m = {result:.2f}mi"
       
def convert_from_kilometer(value, new_unit):
    if new_unit == "millimeter":
        result = value * 1000000
        return f"{value}km = {result:.2f}mm"
    if new_unit == "centimeter":
        result = value * 100000
        return f"{value}km = {result:.2f}cm"
    if new_unit == "meter":
        result = value * 1000
        return f"{value}km = {result:.2f}m"
    if new_unit == "inch":
        result = value * 39370.1
        return f"{value}km = {result:.2f}in"
    if new_unit == "feet":
        result = value * 3280.84
        return f"{value}km = {result:.2f}ft"
    if new_unit == "yard":
        result = value * 1093.61
        return f"{value}km = {result:.2f}yd"
    if new_unit == "mile":
        result = value / 1.60934
        return f"{value}km = {result:.2f}mi"

def convert_from_inch(value, new_unit):
    if new_unit == "millimeter":
        result = value * 25.4
        return f"{value}in = {result:.2f}mm"
    if new_unit == "centimeter":
        result = value * 2.54
        return f"{value}in = {result:.2f}cm"
    if new_unit == "meter":
        result = value / 39.3701
        return f"{value}in = {result:.2f}m"
    if new_unit == "kilometer":
        result = value / 39370.1
        return f"{value}in = {result:.2f}km"
    if new_unit == "feet":
        result = value / 12
        return f"{value}in = {result:.2f}ft"
    if new_unit == "yard":
        result = value / 36
        return f"{value}in = {result:.2f}yd"
    if new_unit == "mile":
        result = value / 63360
        return f"{value}in = {result:.2f}mi"
    
def convert_from_feet(value, new_unit):
    if new_unit == "millimeter":
        result = value * 304.8
        return f"{value}ft = {result:.2f}mm"
    if new_unit == "centimeter":
        result = value * 30.48
        return f"{value}ft = {result:.2f}cm"
    if new_unit == "meter":
        result = value / 3.28084
        return f"{value}ft = {result:.2f}m"
    if new_unit == "kilometer":
        result = value / 3280.84
        return f"{value}ft = {result:.2f}km"
    if new_unit == "inch":
        result = value * 12
        return f"{value}ft = {result:.2f}in"
    if new_unit == "yard":
        result = value / 3
        return f"{value}ft = {result:.2f}yd"
    if new_unit == "mile":
        result = value / 5280
        return f"{value}ft = {result:.2f}mi"
    
def convert_from_yard(value, new_unit):
    if new_unit == "millimeter":
        result = value * 914.4
        return f"{value}yd = {result:.2f}mm"
    if new_unit == "centimeter":
        result = value * 91.44
        return f"{value}yd = {result:.2f}cm"
    if new_unit == "meter":
        result = value / 1.09361
        return f"{value}yd = {result:.2f}m"
    if new_unit == "kilometer":
        result = value / 1093.61
        return f"{value}yd = {result:.2f}km"
    if new_unit == "inch":
        result = value * 36
        return f"{value}yd = {result:.2f}in"
    if new_unit == "feet":
        result = value * 3
        return f"{value}yd = {result:.2f}ft"
    if new_unit == "mile":
        result = value / 1760
        return f"{value}yd = {result:.2f}mi"

def convert_from_mile(value, new_unit):
    if new_unit == "millimeter":
        result = value * 1609344
        return f"{value}mi = {result:.2f}mm"
    if new_unit == "centimeter":
        result = value * 160934.4
        return f"{value}mi = {result:.2f}cm"
    if new_unit == "meter":
        result = value * 1609.344
        return f"{value}mi = {result:.2f}m"
    if new_unit == "kilometer":
        result = value * 1.60934
        return f"{value}mi = {result:.2f}km"
    if new_unit == "inch":
        result = value * 63360
        return f"{value}mi = {result:.2f}in"
    if new_unit == "feet":
        result = value * 5280
        return f"{value}mi = {result:.2f}ft"
    if new_unit == "yard":
        result = value * 1760
        return f"{value}mi = {result:.2f}yd"


# convert from length
def convert_length(value, unit, new_unit):
    if unit == "millimeter":
        return convert_from_millimeter(value, new_unit)

    if unit == "centimeter":
        return convert_from_centimeter(value, new_unit)

    if unit == "meter":
        return convert_from_meter(value, new_unit)

    if unit == "kilometer":
        return convert_from_kilometer(value, new_unit)

    if unit == "inch":
        return convert_from_inch(value, new_unit)

    if unit == "feet":
        return convert_from_feet(value, new_unit)

    if unit == "yard":
        return convert_from_yard(value, new_unit)

    if unit == "mile":
        return convert_from_mile(value, new_unit)