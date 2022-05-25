#functions for Mass Converter
def convertFromTon(toUnit, input):
    valDict = { 'Ton': 1,
                'Pound': 2204.6226218488,
                'Ounce': 35273.96194958,
                'Kilogram': 1000,
                'Gram': 1000000 }
    result = input * valDict[toUnit]
    return result

def convertFromPound(toUnit, input):
    valDict = { 'Ton': 0.0004535924,
                'Pound': 1,
                'Ounce': 16,
                'Kilogram': 0.45359237,
                'Gram': 453.59237 }
    result = input * valDict[toUnit]
    return result

def convertFromOunce(toUnit, input):
    valDict = { 'Ton': 0.0000283495,
                'Pound': 0.0625,
                'Ounce': 1,
                'Kilogram': 0.0283495231,
                'Gram': 28.349523125 }
    result = input * valDict[toUnit]
    return result

def convertFromKilogram(toUnit, input):
    valDict = { 'Ton': 0.001,
                'Pound': 2.2046226218,
                'Ounce': 35.2739619496,
                'Kilogram': 1,
                'Gram': 1000 }
    result = input * valDict[toUnit]
    return result

def convertFromGram(toUnit, input):
    valDict = { 'Ton': 0.000001, 
                'Pound': 0.0022046226,
                'Ounce': 0.0352739619,
                'Kilogram': 0.001,
                'Gram': 1 }
    result = input * valDict[toUnit]
    return result

def convertMass(fromUnit, toUnit, input):
    funDict = { 'Ton': convertFromTon,
                'Pound': convertFromPound,
                'Ounce': convertFromOunce,
                'Kilogram': convertFromKilogram,
                'Gram': convertFromGram }
    return funDict[fromUnit](toUnit, input)
