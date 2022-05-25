let keyValues = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '00', '.', '( )', '+', '-', '*', '/', '^', '+/-', '' ];
let keyIds = [];
for (let i = 0; i < keyValues.length; i++) {
  keyIds[i] = 'key' + '_' + keyValues[i];
}

let operators = [ '+', '-', '*', '/', '^' ];
function isOperator(term) {
  let result = false;
  for (operator of operators) {
    if (operator === term) {
      result = true;
      break;
    }
  }
  return result;
}

function processOperatorButtons(inputValue, operator) {
  if (inputValue.length > 0) {
    if (inputValue.slice(-1) === ')' || inputValue.slice(-1) !== ' ') {
      inputValue = inputValue + ' ' + operator + ' ';
    }
  }
  return inputValue;
}

function processParenthesesButton(inputValue) {
  let terms = inputValue.split(' ');
  let currentTerm = terms[terms.length - 1];
  let pCount = 0;
  for (let c of inputValue) {
    if (c === '(') {
      pCount += 1;
    } else if (c === ')') {
      pCount -= 1;
    }
  }

  if (currentTerm.length === 0) {
    inputValue = inputValue + '( ';
    pCount = pCount + 1;
  } else if (currentTerm.length > 0 ) {
    if (currentTerm === ')') {
      if (pCount > 0) {
        inputValue = inputValue + ' )';
        pCount -= 1;
      } else {
        inputValue = inputValue + ' * ( ';
        pCount += 1;
      }
    } else {
      if (pCount > 0) {
        inputValue = inputValue + ' )';
        pCount -= 1;
      } else {
        inputValue = inputValue + ' * ( ';
        pCount += 1;
      }
    }
  }
  return inputValue;
}

function processDecimalButton(inputValue) {
  if (inputValue.length === 0) {
    inputValue = '0.';
  } else {
    let terms = inputValue.split(' ');
    let currentTerm = terms[terms.length - 1];
    if (!currentTerm.includes('.')) {
      if (currentTerm.length === 0) {
        inputValue = inputValue + '0.';
      } else {
        inputValue = inputValue + '.';
      }
    }
  }
  return inputValue;
}

function processSignButton(inputValue) {
  let terms = inputValue.split(' ');
  let currentTerm = terms[terms.length - 1];

  if (inputValue === '') {
    inputValue = '( -';
  } else {
    if (inputValue.slice(-3) === '( -') {
      terms.pop();
      terms.pop();
    } else if (currentTerm === '') {
      if (terms.length > 1) {
        if (terms[terms.length - 2] === '(') {
      	   currentTerm = '( -';
        } else if (isOperator(terms[terms.length - 2])) {
           currentTerm = '( -';
        }
        terms[terms.length - 1] = currentTerm;
      }
    } else if (currentTerm === ')') {
      currentTerm = currentTerm + ' * ( -';
      terms[terms.length - 1] = currentTerm;
    } else {
      if (currentTerm.includes('-')) {
        terms.pop();
        terms.pop();
        terms.push(currentTerm.slice(1));
      } else {
        currentTerm = '( -' + currentTerm;
        terms[terms.length - 1] = currentTerm;
      }
    }

    let inputValueNew = '';
    let term;
    for (term of terms) {
      inputValueNew = inputValueNew + term + ' ';
    }

    if (!(isOperator(term) && term === ')' && term === '(')) {
      inputValueNew = inputValueNew.trim();
    }

    inputValue = inputValueNew;
  }
  return inputValue;
}

function processDigitButtons(inputValue, digit) {
  if (inputValue.length === 0) {
    if (digit !== '0' && digit !== '00') {
      inputValue = digit;
    }
  } else {
    inputValue += digit;
  }
  return inputValue;
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
  } else if (isOperator(keyValue)) {
    inputValue = processOperatorButtons(inputValue, keyValue);
  } else if (keyValue === '( )') {
    inputValue = processParenthesesButton(inputValue);
  } else if (keyValue === '.') {
    inputValue = processDecimalButton(inputValue);
  } else if (keyValue === '+/-') {
    inputValue = processSignButton(inputValue);
  } else {
    inputValue = processDigitButtons(inputValue, keyValue);
  }
  return inputValue;
}

for (let i = 0; i < keyIds.length; i++) {
  document.getElementById(keyIds[i]).addEventListener('click', function() {
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
  let isEmpty = inputValue.length === 0;
  let isInvalid = false;
  if (inputValue.slice(-1) === '.' || inputValue.slice(-1) === ' ' || inputValue.slice(-2) === '( ' || inputValue.slice(-3) === '( -') {
    isInvalid = true;
  }
  if (isEmpty || isInvalid) {
    event.preventDefault();
    if (isEmpty) {
      alert('Hii User!! Please provide an Input for computation...');
    } else {
      alert('Hii User!! Please provide a Valid Input for computation...');
    }
  }
});
