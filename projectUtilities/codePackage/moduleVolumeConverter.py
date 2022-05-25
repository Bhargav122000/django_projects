# functions for Volume Converter
def convertFromGallon(toUnit, input):
    valDict = { 'Gallon': 1,
                'Litre': 4.54609,
                'Millilitre': 4546.09,
                'Cubic Centimetre': 4546.09,
                'Cubic Metre': 0.00454609,
                'Cubic Inch': 277.4194327916,
                'Cubic Foot': 0.1605436532 }
    result = input * valDict[toUnit]
    return result

def convertFromLitre(toUnit, input):
    valDict = { 'Gallon': 0.2199692483,
                'Litre': 1,
                'Millilitre': 1000,
                'Cubic Centimetre': 1000,
                'Cubic Metre': 0.001,
                'Cubic Inch': 61.0237440947,
                'Cubic Foot': 0.0353146667 }
    result = input * valDict[toUnit]
    return result

def convertFromMillilitre(toUnit, input):
    valDict = { 'Gallon': 0.0002199692,
                'Litre': 0.001,
                'Millilitre': 1,
                'Cubic Centimetre': 1,
                'Cubic Metre': 0.000001,
                'Cubic Inch': 0.0610237441,
                'Cubic Foot': 0.0000353147 }
    result = input * valDict[toUnit]
    return result

def convertFromCubicCentimetre(toUnit, input):
    valDict = { 'Gallon': 0.0002199692,
                'Litre': 0.001,
                'Millilitre': 1,
                'Cubic Centimetre': 1,
                'Cubic Metre': 0.000001,
                'Cubic Inch': 0.0610237441,
                'Cubic Foot': 0.0000353147 }
    result = input * valDict[toUnit]
    return result

def convertFromCubicMetre(toUnit, input):
    valDict = { 'Gallon': 219.9692482991,
                'Litre': 1000,
                'Millilitre': 1000000,
                'Cubic Centimetre': 1000000,
                'Cubic Metre': 1,
                'Cubic Inch': 61023.744094732,
                'Cubic Foot': 35.3146667215 }
    result = input * valDict[toUnit]
    return result

def convertFromCubicInch(toUnit, input):
    valDict = { 'Gallon': 0.0036046501,
                'Litre': 0.016387064,
                'Millilitre': 16.387064,
                'Cubic Centimetre': 16.387064,
                'Cubic Metre': 0.0000163871,
                'Cubic Inch': 1,
                'Cubic Foot': 0.0005787037 }
    result = input * valDict[toUnit]
    return result

def convertFromCubicFoot(toUnit, input):
    valDict = { 'Gallon': 6.228835459,
                'Litre': 28.316846592,
                'Millilitre': 28316.846592,
                'Cubic Centimetre': 28316.846592,
                'Cubic Metre': 0.0283168466,
                'Cubic Inch': 1728,
                'Cubic Foot': 1 }
    result = input * valDict[toUnit]
    return result

def convertVolume(fromUnit, toUnit, input):
    funDict = { 'Gallon': convertFromGallon,
                'Litre': convertFromLitre,
                'Millilitre': convertFromMillilitre,
                'Cubic Centimetre': convertFromCubicCentimetre,
                'Cubic Metre': convertFromCubicMetre,
                'Cubic Inch': convertFromCubicInch,
                'Cubic Foot': convertFromCubicFoot }
    return funDict[fromUnit](toUnit, input)
