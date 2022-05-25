# functions for Data Converter
def convertFromBit(toUnit, input):
    valDict = { 'Bit': 1,
                'Byte': 0.125,
                'Kilobyte': 0.0001220703,
                'Megabyte': 1.19209290e-7,
                'Gigabyte': 1.16415322e-10,
                'Terabyte': 1.13686838e-13 }
    result = input * valDict[toUnit]
    return result

def convertFromByte(toUnit, input):
    valDict = { 'Bit': 8,
                'Byte': 1,
                'Kilobyte': 0.0009765625,
                'Megabyte': 0.0000009537,
                'Gigabyte': 0.0000000009,
                'Terabyte': 9.09494702e-13 }
    result = input * valDict[toUnit]
    return result

def convertFromKilobyte(toUnit, input):
    valDict = { 'Bit': 8192,
                'Byte': 1024,
                'Kilobyte': 1,
                'Megabyte': 0.0009765625,
                'Gigabyte': 0.0000009537,
                'Terabyte': 0.0000000009 }
    result = input * valDict[toUnit]
    return result

def convertFromMegabyte(toUnit, input):
    valDict = { 'Bit': 8388608,
                'Byte': 1048576,
                'Kilobyte': 1024,
                'Megabyte': 1,
                'Gigabyte': 0.0009765625,
                'Terabyte': 0.0000009537 }
    result = input * valDict[toUnit]
    return result

def convertFromGigabyte(toUnit, input):
    valDict = { 'Bit': 8589934592,
                'Byte': 1073741824,
                'Kilobyte': 1048576,
                'Megabyte': 1024,
                'Gigabyte': 1,
                'Terabyte': 0.0009765625 }
    result = input * valDict[toUnit]
    return result

def convertFromTerabyte(toUnit, input):
    valDict = { 'Bit': 8796093022208,
                'Byte': 1099511627776,
                'Kilobyte': 1073741824,
                'Megabyte': 1048576,
                'Gigabyte': 1024,
                'Terabyte': 1 }
    result = input * valDict[toUnit]
    return result

def convertData(fromUnit, toUnit, input):
    funDict = { 'Bit':convertFromBit,
                'Byte':convertFromByte,
                'Kilobyte':convertFromKilobyte,
                'Megabyte':convertFromMegabyte,
                'Gigabyte':convertFromGigabyte,
                'Terabyte':convertFromTerabyte }
    return funDict[fromUnit](toUnit, input)
