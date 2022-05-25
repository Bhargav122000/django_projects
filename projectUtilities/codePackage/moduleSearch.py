from django.shortcuts import redirect
import re

def searchAndNavigate(request, defaultTarget):
    searchValue = request.GET.dict().get('search').strip().lower()

    welcomePatterns = [ '^((home|welcome)(| *page)|utility(| *tool))$' ]

    calculatorPatterns = [ '^(calculat(e|or|ion)|arithmetic(s?)(| *calculat(e|or|ion)))$',
                           '^basic(| *arithmetic(s?)(| *calculat(e|or|ion)))$',
                           '^(\+|sum|add(|ition))$',
                           '^(-|difference|sub(|tract(|ion)))$',
                           '^(\*|product|multipl(y|ication))$',
                           '^(/|div(|ide|ision))$',
                           '^(\^|pow(|er)|exp(|onent))$' ]

    romanConverterPatterns = [ '^(roman(| *conver(t(|er|ion)|sion)))$',
                               '^(roman( *(|to|-) *number))$' ]

    numberConverterPatterns = [ '^(number(| *conver(t(|er|ion)|sion)))$',
                                '^(number( *(|to|-) *roman))$' ]

    unitConverterPatterns = [ '^(unit(| *conver(t(|er|ion)|sion)))$' ]

    joinPattern = '( *(|to|-) *)'

    areaUnitsPattern = '((acre|ac)|(hectare|ha)|((square|sq)(|\.| *)(centimetre|cm|f(|oo)t|in(|ch)|m(|etre))))'
    areaConverterPattern = '^' + areaUnitsPattern + '(|' + joinPattern + areaUnitsPattern + ')$'
    areaConverterPatterns = [ '^(area(| *unit))$',
                              '^(area((| *unit) *conver(t(|er|ion)|sion)))$',
                              areaConverterPattern ]

    dataUnitsPattern = '(bit|((|k(|ilo)|m(|ega)|g(|iga)|t(|era))(|\.| *)b(|yte)))'
    dataConverterPattern = '^' + dataUnitsPattern + '(|' + joinPattern + dataUnitsPattern + ')$'
    dataConverterPatterns = [ '^(data(| *unit))$',
                              '^(data((| *unit) *conver(t(|er|ion)|sion)))$',
                              dataConverterPattern ]

    lengthUnitsPattern = '(in(|ch)|f(|oo)t|y(|ar)d|mi(|le)|((|m(|illi)|c(|enti)|k(|ilo))(|\.| *)m(|etre)))'
    lengthConverterPattern = '^' + lengthUnitsPattern + '(|' + joinPattern + lengthUnitsPattern + ')$'
    lengthConverterPatterns = [ '^(length(| *unit))$',
                                '^(length((| *unit) *conver(t(|er|ion)|sion)))$',
                                lengthConverterPattern ]

    massUnitsPattern = '(t(|on)|(pound|lb)|o(unce|z)|((|k(|ilo))(|\.| *)g(|ram)))'
    massConverterPattern = '^' + massUnitsPattern + '(|' + joinPattern + massUnitsPattern + ')$'
    massConverterPatterns = [ '^(mass(| *unit))$',
                              '^(mass((| *unit) *conver(t(|er|ion)|sion)))$',
                              massConverterPattern ]

    temperatureUnitsPattern = '(c(|elsius|entigrade)|f(|ahrenheit)|k(|elvin))'
    temperatureConverterPattern = '^' + temperatureUnitsPattern + '(|' + joinPattern + temperatureUnitsPattern + ')$'
    temperatureConverterPatterns = [ '^(temperature(| *unit))$',
                                     '^(temperature((| *unit) *conver(t(|er|ion)|sion)))$',
                                     temperatureConverterPattern ]

    volumeUnitsPattern = '(gal(|lon)|(|m(|illi))(|\.| *)l(|itre)|((cubic|cb)(|\.| *)(in(|ch)|f(|oo)t|(|c(|enti))(|\.| *)m(|etre))))'
    volumeConverterPattern = '^' + volumeUnitsPattern + '(|' + joinPattern + volumeUnitsPattern + ')$'
    volumeConverterPatterns = [ '^(volume(| *unit))$',
                                '^(volume((| *unit) *conver(t(|er|ion)|sion)))$',
                                volumeConverterPattern ]

    patternsDict = {}
    for pattern in welcomePatterns:
        patternsDict[pattern] = 'appWelcome:welcome'
    for pattern in calculatorPatterns:
        patternsDict[pattern] = 'appCalculator:calculator'
    for pattern in numberConverterPatterns:
        patternsDict[pattern] = 'appNumberConverter:numberConverter'
    for pattern in romanConverterPatterns:
        patternsDict[pattern] = 'appRomanConverter:romanConverter'
    for pattern in unitConverterPatterns:
        patternsDict[pattern] = 'appUnitConverter:unitConverter'
    for pattern in areaConverterPatterns:
        patternsDict[pattern] = 'appUnitConverter:areaUnitConverter'
    for pattern in dataConverterPatterns:
        patternsDict[pattern] = 'appUnitConverter:dataUnitConverter'
    for pattern in lengthConverterPatterns:
        patternsDict[pattern] = 'appUnitConverter:lengthUnitConverter'
    for pattern in massConverterPatterns:
        patternsDict[pattern] = 'appUnitConverter:massUnitConverter'
    for pattern in temperatureConverterPatterns:
        patternsDict[pattern] = 'appUnitConverter:temperatureUnitConverter'
    for pattern in volumeConverterPatterns:
        patternsDict[pattern] = 'appUnitConverter:volumeUnitConverter'

    patternsList = list(patternsDict.keys())
    for pattern in patternsList:
        if re.search(pattern, searchValue):
            return redirect(patternsDict[pattern])
    return redirect(defaultTarget)
