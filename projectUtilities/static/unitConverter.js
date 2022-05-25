let keyValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '00', '.', ''];
let keyIds = [];
for (let i = 0; i < keyValues.length; i++) {
  keyIds[i] = 'key' + "_" + keyValues[i];
}

function clearFields() {
  let resultValue = document.getElementById('result').value;
  if (resultValue.length > 0) {
    document.getElementById('result').value = '';
    document.getElementById('input').value = '';
  }
}

function updateInputField(inputValue, keyValue) {
  if (keyValue === '') {
    inputValue = '';
  } else if (keyValue === '.'){
    let isPresent = inputValue.includes('.');
    if (!isPresent) {
      if (inputValue.length === 0){
        inputValue = '0'
      }
      inputValue = inputValue + keyValue;
    }
  } else if (keyValue === '0' || keyValue === '00') {
    if (inputValue.length != 0) {
      inputValue = inputValue + keyValue;
    }
  } else {
    inputValue = inputValue + keyValue;
  }
  return inputValue;
}

for (let i = 0; i < keyIds.length; i++) {
  document.getElementById(keyIds[i]).addEventListener('click', function(){
    //clear input & output fields if output is present in output field
    clearFields();

    //update the input field
    let inputValue = document.getElementById('input').value;
    inputValue = updateInputField(inputValue, keyValues[i]);
    document.getElementById('input').value = inputValue;
  });
}

document.getElementById('submit').addEventListener('click', function (event) {
  let inputValue = document.getElementById('input').value;
  let fromUnit = document.getElementById('fromUnit').value;
  let toUnit = document.getElementById('toUnit').value;

  let isEmpty = inputValue.length === 0;
  let isFromUnitNotSelected = fromUnit === 'select from unit';
  let isToUnitNotSelected = toUnit === 'select to unit';
  if (isFromUnitNotSelected || isToUnitNotSelected || isEmpty) {
    event.preventDefault();
    if (isFromUnitNotSelected) {
      alert('Hii User!! Please select a "from unit" to proceed for conversion...');
    } else if (isToUnitNotSelected) {
      alert('Hii User!! Please select a "to unit" to proceed for conversion...');
    } else {
      alert('Hii User!! Please provide a Value to convert from ' + fromUnit + ' to ' + toUnit + '...');
    }
  }
});
