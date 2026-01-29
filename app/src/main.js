(function() {
  const display = document.getElementById('display');
  let currentValue = '0';
  let previousValue = '';
  let operation = null;
  let shouldResetDisplay = false;

  function updateDisplay() {
    display.value = currentValue;
  }

  function handleNumber(num) {
    if (shouldResetDisplay) {
      currentValue = num;
      shouldResetDisplay = false;
    } else {
      if (currentValue === '0' && num !== '.') {
        currentValue = num;
      } else if (num === '.' && currentValue.includes('.')) {
        return;
      } else {
        currentValue += num;
      }
    }
    updateDisplay();
  }

  function handleOperation(op) {
    if (operation !== null && !shouldResetDisplay) {
      calculate();
    }
    previousValue = currentValue;
    operation = op;
    shouldResetDisplay = true;
  }

  function calculate() {
    if (operation === null || shouldResetDisplay) return;
    
    let result;
    const prev = parseFloat(previousValue);
    const curr = parseFloat(currentValue);
    
    switch (operation) {
      case '+':
        result = prev + curr;
        break;
      case '-':
        result = prev - curr;
        break;
      case '*':
        result = prev * curr;
        break;
      case '/':
        result = prev / curr;
        break;
      default:
        return;
    }
    
    currentValue = result.toString();
    operation = null;
    shouldResetDisplay = true;
    updateDisplay();
  }

  function clear() {
    currentValue = '0';
    previousValue = '';
    operation = null;
    shouldResetDisplay = false;
    updateDisplay();
  }

  function deleteLastChar() {
    if (currentValue.length > 1) {
      currentValue = currentValue.slice(0, -1);
    } else {
      currentValue = '0';
    }
    updateDisplay();
  }

  // Event listeners
  document.querySelectorAll('.num-btn').forEach(btn => {
    btn.addEventListener('click', () => handleNumber(btn.dataset.num));
  });

  document.querySelectorAll('.op-btn').forEach(btn => {
    btn.addEventListener('click', () => handleOperation(btn.dataset.op));
  });

  document.querySelector('[data-fn="clear"]').addEventListener('click', clear);
  document.querySelector('[data-fn="delete"]').addEventListener('click', deleteLastChar);
  document.querySelector('[data-fn="equals"]').addEventListener('click', calculate);

  // Keyboard support
  document.addEventListener('keydown', (e) => {
    if (/[0-9.]/.test(e.key)) handleNumber(e.key);
    if (e.key === '+' || e.key === '-' || e.key === '*' || e.key === '/') handleOperation(e.key);
    if (e.key === 'Enter' || e.key === '=') calculate();
    if (e.key === 'Backspace') deleteLastChar();
    if (e.key === 'Escape' || e.key === 'c' || e.key === 'C') clear();
  });

  updateDisplay();
})();
