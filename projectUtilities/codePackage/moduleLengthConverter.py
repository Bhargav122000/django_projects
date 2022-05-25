# functions for Length Converter
def convertFromMillimetre(toUnit, input):
    valDict = { 'Millimetre': 1,
                'Centimetre': 0.1,
                'Metre': 0.001,
                'Kilometre': 0.000001,
                'Inch': 0.0393700787,
                'Foot': 0.0032808399,
                'Yard': 0.0010936133,
                'Mile': 0.0000006214 }
    result = input * valDict[toUnit]
    return result

def convertFromCentimetre(toUnit, input):
    valDict = { 'Millimetre': 10,
                'Centimetre': 1,
                'Metre': 0.01,
                'Kilometre': 0.00001,
                'Inch': 0.3937007874,
                'Foot': 0.032808399,
                'Yard': 0.010936133,
                'Mile': 0.0000062137 }
    result = input * valDict[toUnit]
    return result

def convertFromMetre(toUnit, input):
    valDict = { 'Millimetre': 1000,
                'Centimetre': 100,
                'Metre': 1,
                'Kilometre': 0.001,
                'Inch': 39.3700787402,
                'Foot': 3.280839895,
                'Yard': 1.0936132983,
                'Mile': 0.0006213712 }
    result = input * valDict[toUnit]
    return result

def convertFromKilometre(toUnit, input):
    valDict = { 'Millimetre': 1000000,
                'Centimetre': 100000,
                'Metre': 1000,
                'Kilometre': 1,
                'Inch': 39370.078740157,
                'Foot': 3280.8398950131,
                'Yard': 1093.6132983377,
                'Mile': 0.6213711922 }
    result = input * valDict[toUnit]
    return result

def convertFromInch(toUnit, input):
    valDict = { 'Millimetre': 25.4,
                'Centimetre': 2.54,
                'Metre': 0.0254,
                'Kilometre': 0.0000254,
                'Inch': 1,
                'Foot': 0.0833333333,
                'Yard': 0.0277777778,
                'Mile': 0.0000157828 }
    result = input * valDict[toUnit]
    return result

def convertFromFoot(toUnit, input):
    valDict = { 'Millimetre': 304.8,
                'Centimetre': 30.48,
                'Metre': 0.3048,
                'Kilometre': 0.0003048,
                'Inch': 12,
                'Foot': 1,
                'Yard': 0.3333333333,
                'Mile': 0.0001893939 }
    result = input * valDict[toUnit]
    return result

def convertFromYard(toUnit, input):
    valDict = { 'Millimetre': 914.4,
                'Centimetre': 91.44,
                'Metre': 0.9144,
                'Kilometre': 0.0009144,
                'Inch': 36,
                'Foot': 3,
                'Yard': 1,
                'Mile': 0.0005681818 }
    result = input * valDict[toUnit]
    return result

def convertFromMile(toUnit, input):
    valDict = { 'Millimetre': 1609344,
                'Centimetre': 160934.4,
                'Metre': 1609.344,
                'Kilometre': 1.609344,
                'Inch': 63360,
                'Foot': 5280,
                'Yard': 1760,
                'Mile': 1 }
    result = input * valDict[toUnit]
    return result

def convertLength(fromUnit, toUnit, input):
    funDict = { 'Millimetre': convertFromMillimetre,
                'Centimetre': convertFromCentimetre,
                'Metre': convertFromMetre,
                'Kilometre': convertFromKilometre,
                'Inch': convertFromInch,
                'Foot': convertFromFoot,
                'Yard': convertFromYard,
                'Mile': convertFromMile }
    return funDict[fromUnit](toUnit, input)
