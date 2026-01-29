# Simple Calculator Web App

A modern, responsive calculator web application built with vanilla JavaScript, HTML, and CSS. No frameworks or external dependencies required.

## 📁 Project Structure

```
calculator_web/
├── app/                    # Application code
│   ├── index.html         # Main HTML file with calculator UI
│   ├── src/
│   │   └── main.js        # Calculator logic and event handlers
│   └── styles/
│       └── style.css      # Styling and responsive design
├── tests/                 # Test files
│   └── test_main.js       # Test placeholder
└── README.md             # This file
```

## ✨ Features

- ✅ **Full Calculator Operations**: Addition, subtraction, multiplication, division
- ✅ **Clear Function**: Reset calculator to initial state
- ✅ **Delete Function**: Remove last digit entered
- ✅ **Decimal Support**: Handle floating-point numbers
- ✅ **Keyboard Support**: Type numbers and operations directly from keyboard
- ✅ **Responsive Design**: Works on desktop, tablet, and mobile devices
- ✅ **Modern UI**: Gradient background, smooth animations, intuitive button layout
- ✅ **No Dependencies**: Pure vanilla JavaScript, HTML, CSS

## 🚀 Getting Started

### Prerequisites
- A web browser (Chrome, Firefox, Safari, Edge, etc.)
- Python 3 or Node.js (for local server)

### Installation & Running Locally

#### Option 1: Python (Recommended - No Installation Required)

```bash
cd /Users/shubham/Desktop/calculator_web/app
python3 -m http.server 8000
```

Then open Chrome and visit: **http://localhost:8000**

#### Option 2: Node.js

```bash
cd /Users/shubham/Desktop/calculator_web/app
npx http-server
```

Visit the URL displayed in terminal (usually **http://localhost:8080**)

#### Option 3: VS Code Live Server Extension

1. Install the "Live Server" extension in VS Code
2. Right-click on `app/index.html`
3. Select "Open with Live Server"
4. Chrome will automatically open

---

## 📖 How to Use

### Mouse/Touch
- Click number buttons (0-9) to enter numbers
- Click operation buttons (+, −, ×, ÷) to select operation
- Click **=** to calculate result
- Click **C** to clear and reset
- Click **DEL** to delete last digit

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Enter numbers |
| `.` | Enter decimal point |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `Enter` or `=` | Calculate result |
| `Backspace` | Delete last digit (DEL) |
| `Escape` or `C` | Clear calculator |

---

## 🎨 Customization

### Change Colors
Edit `/app/styles/style.css`:
- `#667eea` - Operation buttons (primary blue)
- `#764ba2` - Gradient background (purple)
- `#ff6b6b` - Function buttons (red)
- `#51cf66` - Equals button (green)

### Change Button Layout
Edit `/app/index.html` to add/remove buttons in the grid.

### Modify Font Size
In `/app/styles/style.css`, adjust:
- `#display` font-size (currently `2.5rem`)
- `.btn` font-size (currently `1.3rem`)

---

## 🧪 Testing

Test file located at: `tests/test_main.js`

To add tests:
1. Install a test framework (Jest, Mocha, or Node assert)
2. Write tests in `test_main.js`
3. Run tests via `npm test` or similar command

Example test:
```javascript
const assert = require('assert');
// Test code here
assert.strictEqual(2 + 2, 4);
```

---

## 🛠️ Development

### File Descriptions

- **index.html**: Contains calculator UI structure with semantic HTML buttons
- **main.js**: Contains all calculator logic:
  - `handleNumber()` - Processes number input
  - `handleOperation()` - Sets active operation
  - `calculate()` - Performs arithmetic
  - `clear()` - Resets calculator
  - `deleteLastChar()` - Removes last digit
  - Event listeners for buttons and keyboard
- **style.css**: Modern responsive styling with:
  - CSS Grid for button layout
  - Flexbox for alignment
  - Media queries for mobile responsiveness
  - Smooth transitions and hover effects

### Browser Compatibility

- Chrome ✅
- Firefox ✅
- Safari ✅
- Edge ✅
- Mobile browsers ✅

---

## 📝 License

Free to use and modify for personal or educational purposes.

---

## 💡 Tips

- The calculator supports chained operations (e.g., `5 + 3 + 2 = 10`)
- Division by zero is handled gracefully
- Maximum precision matches JavaScript's floating-point limits
- Long expressions are displayed in the input field

Enjoy your calculator! 🎉
