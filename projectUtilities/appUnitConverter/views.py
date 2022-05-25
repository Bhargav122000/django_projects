from django.shortcuts import render
from codePackage import moduleAreaConverter, moduleDataConverter
from codePackage import moduleLengthConverter, moduleMassConverter
from codePackage import moduleTemperatureConverter, moduleVolumeConverter
from codePackage import moduleSearch

# function to adjust decimal
def adjustDecimalValue(n):
    if n - int(n) == 0:
        return int(n)
    else:
        return round(n, 10)

# function to convert input accordingly
def convert(measurement, fromUnit, toUnit, input):
	if measurement == 'Area':
		return moduleAreaConverter.convertArea(fromUnit, toUnit, input)
	elif measurement == 'Data':
		return moduleDataConverter.convertData(fromUnit, toUnit, input)
	elif measurement == 'Length':
		return moduleLengthConverter.convertLength(fromUnit, toUnit, input)
	elif measurement == 'Mass':
		return moduleMassConverter.convertMass(fromUnit, toUnit, input)
	elif measurement == 'Temperature':
		return moduleTemperatureConverter.convertTemperature(fromUnit, toUnit, input)
	else:
		return moduleVolumeConverter.convertVolume(fromUnit, toUnit, input)

# Create your views here.
def unitConverter(request):
    if request.GET.dict().get('search') == None:
        return render(request, 'appUnitConverter/unitConverter.html')
    else:
        return moduleSearch.searchAndNavigate(request, 'appUnitConverter:unitConverter')

def genericUnitConverter(request, measurement):
    unitsDict = { 'Area': {'Acre': 'ac', 'Hectare': 'ha', 'Square Centimetre': 'sq.cm', 'Square Foot': 'sq.ft', 'Square Inch': 'sq.in', 'Square Metre': 'sq.m'},
    'Data': {'Bit': 'b', 'Byte': 'B', 'Kilobyte': 'KB', 'Megabyte': 'MB', 'Gigabyte': 'GB', 'Terabyte': 'TB'},
    'Length': {'Millimetre': 'mm', 'Centimetre': 'cm', 'Metre': 'm', 'Kilometre': 'km', 'Inch': 'in', 'Foot': 'ft', 'Yard': 'yd', 'Mile': 'mi'},
    'Mass': {'Ton': 't', 'Pound': 'lb', 'Ounce': 'oz', 'Kilogram': 'kg', 'Gram': 'g'},
    'Temperature': {'Celsius': 'C', 'Fahrenheit': 'F', 'Kelvin': 'K'},
    'Volume': {'Gallon': 'gal', 'Litre': 'l', 'Millilitre': 'ml', 'Cubic Centimetre': 'cb.cm', 'Cubic Metre': 'cb.m', 'Cubic Inch': 'cb.in', 'Cubic Foot': 'cb.ft'}
    }
    valuesDict = { 'measurement': measurement, 'units': unitsDict[measurement], 'input': '', 'result': '', 'fromUnit': '', 'toUnit': '', 'response': False }
    if request.method == 'POST':
        formValuesDict = request.POST.dict()
        input = float(formValuesDict['input'])
        fromUnit = formValuesDict['fromUnit']
        toUnit = formValuesDict['toUnit']
        result = convert(measurement, fromUnit, toUnit, input)
        input = adjustDecimalValue(input)
        result = adjustDecimalValue(result)
        valuesDict['input'] = input
        valuesDict['result'] = result
        valuesDict['fromUnit'] = fromUnit
        valuesDict['toUnit'] = toUnit
        valuesDict['response'] = True
        return render(request, 'appUnitConverter/genericUnitConverter.html', context = valuesDict)
    elif request.method == 'GET':
        if request.GET.dict().get('search') == None:
            return render(request, 'appUnitConverter/genericUnitConverter.html', context = valuesDict)
        else:
            targetPages = { 'Area': 'appUnitConverter:areaUnitConverter',
            'Data': 'appUnitConverter:dataUnitConverter',
            'Length': 'appUnitConverter:lengthUnitConverter',
            'Mass': 'appUnitConverter:massUnitConverter',
            'Temperature': 'appUnitConverter:temperatureUnitConverter',
            'Volume': 'appUnitConverter:volumeUnitConverter'
            }
            return moduleSearch.searchAndNavigate(request, targetPages[measurement])

def areaUnitConverter(request):
	return genericUnitConverter(request, 'Area')

def dataUnitConverter(request):
    return genericUnitConverter(request, 'Data')

def lengthUnitConverter(request):
    return genericUnitConverter(request, 'Length')

def massUnitConverter(request):
    return genericUnitConverter(request, 'Mass')

def temperatureUnitConverter(request):
    return genericUnitConverter(request, 'Temperature')

def volumeUnitConverter(request):
    return genericUnitConverter(request, 'Volume')
