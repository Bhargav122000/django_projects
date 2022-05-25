from django.shortcuts import render
from codePackage import moduleCalculator, moduleSearch

# Create your views here.
def calculator(request):
    valuesDict = { 'input': '', 'result': '', 'response': False}
    if request.method == 'POST':
        formValuesDict = request.POST.dict()
        input = formValuesDict['input']
        result = moduleCalculator.calculate(input)
        valuesDict['input'] = input
        valuesDict['result'] = result
        valuesDict['response'] = True
        return render(request, 'appCalculator/calculator.html', context = valuesDict)
    elif request.method == 'GET':
        if request.GET.dict().get('search') == None:
            return render(request, 'appCalculator/calculator.html', context = valuesDict)
        else:
            return moduleSearch.searchAndNavigate(request, 'appCalculator:calculator')
