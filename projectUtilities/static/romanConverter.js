let keyValues = ['I', 'V', 'X', 'L', 'C', 'D', 'M', ''];
let keyIds = [];
for (let i = 0; i < keyValues.length; i++) {
  keyIds[i] = 'key' + "_" + keyValues[i];
}

function clearFields() {
  let numberValue = document.getElementById('resultNumber').value;
  if (numberValue.length > 0) {
    document.getElementById('resultNumber').value = '';
    document.getElementById('inputRoman').value = '';
  }
}

function updateInputField(inputValue, keyValue) {
  if (keyValue === '') {
    inputValue = '';
  } else {
    if (inputValue.length === 0) {
      inputValue = keyValue;
    } else {
      inputValue += keyValue;
    }
  }
  return inputValue;
}

for (let i = 0; i < keyIds.length; i++) {
  document.getElementById(keyIds[i]).addEventListener('click', function() {
    //clear input & output fields if output is present in output field
    clearFields();

    //update the input field
    let inputValue = document.getElementById('inputRoman').value;
    inputValue = updateInputField(inputValue, keyValues[i]);
    document.getElementById('inputRoman').value = inputValue;
  });
}

document.getElementById('submit').addEventListener('click', function (event) {
  let inputValue = document.getElementById('inputRoman').value;
  if (inputValue.length === 0) {
    event.preventDefault();
    alert('Hii User!! Please provide a Roman to convert into Number Equivalent...');
  } else {
    let isLimitExceeded = (inputValue.length > 3) && (inputValue.slice(0,3) === 'MMM');

    let isMultipleV = inputValue.lastIndexOf('V') !== inputValue.indexOf('V');
    let isMultipleL = inputValue.lastIndexOf('L') !== inputValue.indexOf('L');
    let isMultipleD = inputValue.lastIndexOf('D') !== inputValue.indexOf('D');

    let patternExcess = /I{4,}|X{4,}|C{4,}/;
    let isExcessRepeatition = inputValue.search(patternExcess) !== -1;

    let isInvalidPositioning = false;

    let patternInvalidPositionI = /I{2,}(V|X)|I(L|C|D|M)|I(V|X)I/;
    let isInvalidPositionI = inputValue.search(patternInvalidPositionI) !== -1;
    isInvalidPositioning = isInvalidPositioning || isInvalidPositionI;

    let patternInvalidPositionX = /X{2,}(L|C)|X(D|M)|X(L|C)X/;
    let isInvalidPositionX = inputValue.search(patternInvalidPositionX) !== -1;
    isInvalidPositioning = isInvalidPositioning || isInvalidPositionX;

    let patternInvalidPositionC = /C{2,}(D|M)|C(D|M)C/;
    let isInvalidPositionC = inputValue.search(patternInvalidPositionC) !== -1;
    isInvalidPositioning = isInvalidPositioning || isInvalidPositionC;

    let patternInvalidPositionV = /V(X|L|C|D|M)/;
	  let isInvalidPositionV = inputValue.search(patternInvalidPositionV) !== -1;
    isInvalidPositioning = isInvalidPositioning || isInvalidPositionV;

	  let patternInvalidPositionL = /L(C|D|M)/;
	  let isInvalidPositionL = inputValue.search(patternInvalidPositionL) !== -1;
    isInvalidPositioning = isInvalidPositioning || isInvalidPositionL;

	  let patternInvalidPositionD = /DM/;
	  let isInvalidPositionD = inputValue.search(patternInvalidPositionD) !== -1;
    isInvalidPositioning = isInvalidPositioning || isInvalidPositionD;

    if (isLimitExceeded) {
      event.preventDefault();
      alert('Hii User!! Max limit of MMM is exceeded...');
    } else if (isMultipleV || isMultipleL || isMultipleD) {
      event.preventDefault();
      alert('Hii User!! Roman literals - [D, L, V] should occur only once in roman form...');
    } else if (isExcessRepeatition) {
      event.preventDefault();
      alert('Hii User!! Roman literals - [C, X, I] repeated exceedingly...');
    } else if (isInvalidPositioning) {
      event.preventDefault();
      alert('Hii User!! Invalid positioning of roman literals...');
    }
  }
});
