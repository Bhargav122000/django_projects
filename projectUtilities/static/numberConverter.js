let keyValues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ''];
let keyIds = [];
for (let i = 0; i < keyValues.length; i++) {
  keyIds[i] = 'key' + "_" + keyValues[i];
}

function clearFields() {
  let romanValue = document.getElementById('resultRoman').value;
  if (romanValue.length > 0) {
    document.getElementById('resultRoman').value = '';
    document.getElementById('inputNumber').value = '';
  }
}

function updateInputField(inputValue, keyValue) {
  if (keyValue === '') {
    inputValue = '';
  } else if(keyValue === '0') {
    if (inputValue.length > 0) {
      inputValue += keyValue;
    }
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
    let inputValue = document.getElementById('inputNumber').value;
    inputValue = updateInputField(inputValue, keyValues[i]);
    document.getElementById('inputNumber').value = inputValue;
  });
}

document.getElementById('submit').addEventListener('click', function (event) {
  let inputValue = document.getElementById('inputNumber').value;
  let isEmpty = inputValue.length === 0;
  let isExceeded = parseInt(inputValue) > 3000;
  if (isEmpty || isExceeded) {
    event.preventDefault();
    if (isEmpty) {
      alert('Hii User!! Please provide a Number to convert into Roman Equivalent...');
    } else {
      alert('Hii User!! Please provide a Number <= 3000 for conversion...');
    }
  }
});
