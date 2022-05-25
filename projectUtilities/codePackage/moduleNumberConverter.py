# functions for number to roman converter
def convertPlaceValue(number, placeValuesList, placeValue):
	str = ""
	count = 0
	if placeValue == 1000:
		if number >= placeValue:
			count = number // placeValue
			for i in range(count):
				str += placeValuesList[0]
	else:
		if number >= placeValue:
			count = number // placeValue
			if count <= 3:
				for i in range(count):
					str += placeValuesList[0]
			elif count == 4:
				str += placeValuesList[0] + placeValuesList[1]
			elif count >= 5 and count <= 8:
				str += placeValuesList[1]
				for i in range(count - 5):
					str += placeValuesList[0]
			elif count == 9:
				str += placeValuesList[0] + placeValuesList[2]
	return str

def convertToRoman(number):
	roman = ""
	roman += convertPlaceValue(number, placeValuesList = ['M'], placeValue = 1000)
	number %= 1000
	roman += convertPlaceValue(number, placeValuesList = ['C', 'D', 'M'], placeValue = 100)
	number %= 100
	roman += convertPlaceValue(number, placeValuesList = ['X', 'L', 'C'], placeValue = 10)
	number %= 10
	roman += convertPlaceValue(number, placeValuesList = ['I', 'V', 'X'], placeValue = 1)
	number %= 1
	return roman
