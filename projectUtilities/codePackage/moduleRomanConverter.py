# functions for roman to number converter
def convertPlaceValue(romanList, placeValuesList, placeValue):
	count = 0
	num = 0
	if placeValue == 1000:
		if len(romanList) > 0 and romanList[0] == placeValuesList[0]:
			for romanLiteral in romanList:
				if romanLiteral == placeValuesList[0]:
					count += 1
				else:
					break
			del romanList[0:count]
			num += (count * placeValue)
	else:
		if len(romanList) > 0 and romanList[0] == placeValuesList[1]:
			count = 1
			num = count * 5 * placeValue
			romanList.pop(0)

		if len(romanList) > 0 and romanList[0] == placeValuesList[0]:
			if len(romanList) > 1 and romanList[1] == placeValuesList[1]:
				count = 4
				del romanList[0:2]
			elif len(romanList) > 1 and romanList[1] == placeValuesList[2]:
				count = 9
				del romanList[0:2]
			else:
				count = 0
				for romanLiteral in romanList:
					if romanLiteral == placeValuesList[0]:
						count += 1
					else:
						break
				del romanList[0:count]

			num += (count * placeValue);
	return num

def convertToNumber(roman):
	romanList = []
	for romanLiteral in roman:
		romanList.append(romanLiteral)

	numberTemp = 0
	numberTemp += convertPlaceValue(romanList, placeValuesList = ['M'], placeValue = 1000)
	numberTemp += convertPlaceValue(romanList, placeValuesList = ['C', 'D', 'M'], placeValue = 100)
	numberTemp += convertPlaceValue(romanList, placeValuesList = ['X', 'L', 'C'], placeValue = 10)
	numberTemp += convertPlaceValue(romanList, placeValuesList = ['I', 'V', 'X'], placeValue = 1)
	number = numberTemp
	return number
