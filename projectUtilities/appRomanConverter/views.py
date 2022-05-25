from django.shortcuts import render
from codePackage import moduleRomanConverter, moduleSearch

# Create your views here.
def romanConverter(request):
	valuesDict = {'input': '', 'result': '', 'response': False}
	if request.method == 'POST':
		formValuesDict = request.POST.dict()
		inputRoman = formValuesDict['inputRoman']
		numberValue = moduleRomanConverter.convertToNumber(inputRoman)
		valuesDict['input'] = inputRoman
		valuesDict['result'] = str(numberValue)
		valuesDict['response'] = True
		return render(request, 'appRomanConverter/romanConverter.html', context=valuesDict)
	elif request.method == 'GET':
		if request.GET.dict().get('search') == None:
			return render(request, 'appRomanConverter/romanConverter.html', context=valuesDict)
		else :
			return moduleSearch.searchAndNavigate(request, 'appRomanConverter:romanConverter')
