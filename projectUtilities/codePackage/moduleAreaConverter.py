# functions for Area Converter
def convertFromAcre(toUnit, input):
    valDict = { 'Acre':1,
                'Hectare':0.4046856422,
                'Square Centimetre':40468564.224,
                'Square Foot':43560,
                'Square Inch':6272640,
                'Square Metre':4046.8564224 }
    result = input * valDict[toUnit]
    return result

def convertFromHectare(toUnit, input):
    valDict = { 'Acre':2.4710538147,
                'Hectare':1,
                'Square Centimetre':10**8,
                'Square Foot':107639.10416709,
                'Square Inch':15500031.000062,
                'Square Metre':10**4 }
    result = input * valDict[toUnit]
    return result

def convertFromSquareCentimetre(toUnit, input):
    valDict = { 'Acre':2.47105381e-8,
                'Hectare':10**-8,
                'Square Centimetre':1,
                'Square Foot':0.001076391,
                'Square Inch':0.15500031,
                'Square Metre':10**-4 }
    result = input * valDict[toUnit]
    return result

def convertFromSquareFoot(toUnit, input):
    valDict = { 'Acre':0.0000229568,
                'Hectare':0.0000092903,
                'Square Centimetre':929.0304,
                'Square Foot':1,
                'Square Inch':144,
                'Square Metre':0.09290304 }
    result = input * valDict[toUnit]
    return result

def convertFromSquareInch(toUnit, input):
    valDict = { 'Acre':1.59422508e-7,
                'Hectare':0.0000000645,
                'Square Centimetre':6.4516,
                'Square Foot':0.0069444444,
                'Square Inch':1,
                'Square Metre':0.00064516 }
    result = input * valDict[toUnit]
    return result

def convertFromSquareMetre(toUnit, input):
    valDict = { 'Acre':0.0002471054,
                'Hectare':10**-4,
                'Square Centimetre':10**4,
                'Square Foot':10.7639104167,
                'Square Inch':1550.0031000062,
                'Square Metre':1 }
    result = input * valDict[toUnit]
    return result

def convertArea(fromUnit, toUnit, input):
    funDict = { 'Acre':convertFromAcre,
                'Hectare':convertFromHectare,
                'Square Centimetre':convertFromSquareCentimetre,
                'Square Foot':convertFromSquareFoot,
                'Square Inch':convertFromSquareInch,
                'Square Metre':convertFromSquareMetre }
    return funDict[fromUnit](toUnit, input)
