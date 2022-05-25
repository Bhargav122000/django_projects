from django.shortcuts import render
from codePackage import moduleSearch

# Create your views here.
def welcome(request):
    if request.GET.dict().get('search') == None:
        return render(request, 'appWelcome/welcome.html')
    else:
        return moduleSearch.searchAndNavigate(request, 'appWelcome:welcome')
