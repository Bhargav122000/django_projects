#functions for Temperature Converter
def convertFromCelsius(toUnit, input):
    result = -1
    if toUnit == 'Celsius':
        result = input
    elif toUnit == 'Fahrenheit':
        result = (input * 1.8) + 32
    elif toUnit == 'Kelvin':
        result = input + 273.15
    return result

def convertFromFahrenheit(toUnit, input):
    result = -1
    if toUnit == 'Celsius':
        result = (input - 32) * (5 / 9)
    elif toUnit == 'Fahrenheit':
        result = input
    elif toUnit == 'Kelvin':
        result = convertFromFahrenheit('Celsius', input)
        result = convertFromCelsius('Kelvin', result)
    return result

def convertFromKelvin(toUnit, input):
    result = -1
    if toUnit == 'Celsius':
        result = input - 273.15
    elif toUnit == 'Fahrenheit':
        result = convertFromKelvin('Celsius', input)
        result = convertFromCelsius('Fahrenheit', result)
    elif toUnit == 'Kelvin':
        result = input
    return result

def convertTemperature(fromUnit, toUnit, input):
    funDict = { 'Celsius': convertFromCelsius,
                'Fahrenheit': convertFromFahrenheit,
                'Kelvin': convertFromKelvin }
    return funDict[fromUnit](toUnit, input)
