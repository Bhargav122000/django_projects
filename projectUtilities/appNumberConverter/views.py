from django.shortcuts import render
from codePackage import moduleNumberConverter, moduleSearch

# Create your views here.
def numberConverter(request):
	valuesDict = {'input':'', 'result':'', 'response':False}
	if request.method == 'POST':
		formValuesDict = request.POST.dict()
		inputNumber = int(formValuesDict['inputNumber'])
		romanValue = moduleNumberConverter.convertToRoman(inputNumber)
		valuesDict['input'] = str(inputNumber)
		valuesDict['result'] = romanValue
		valuesDict['response'] = True
		return render(request, 'appNumberConverter/numberConverter.html', context = valuesDict)
	elif request.method == 'GET':
		if request.GET.dict().get('search') == None:
			return render(request, 'appNumberConverter/numberConverter.html', context = valuesDict)
		else :
			return moduleSearch.searchAndNavigate(request, 'appNumberConverter:numberConverter')
