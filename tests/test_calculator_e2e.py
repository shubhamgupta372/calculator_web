import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver(request):
    """Setup Chrome driver for testing"""
    show_browser = request.config.getoption("--show-browser")
    
    try:
        # Try to get chromedriver from webdriver-manager
        chrome_driver_path = ChromeDriverManager().install()
        
        # Make sure it's executable
        os.chmod(chrome_driver_path, 0o755)
        
        chrome_options = webdriver.ChromeOptions()
        
        # Only add headless if --show-browser flag not set
        if not show_browser:
            chrome_options.add_argument("--headless")  # Run in background
        
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print(f"Warning: webdriver-manager failed, trying system chromedriver: {e}")
        chrome_options = webdriver.ChromeOptions()
        
        if not show_browser:
            chrome_options.add_argument("--headless")
        
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        
        driver = webdriver.Chrome(options=chrome_options)
    
    yield driver
    driver.quit()


@pytest.fixture
def calculator(driver):
    """Open calculator app"""
    # Adjust URL based on your server setup
    driver.get("http://localhost:8000")
    time.sleep(1)  # Wait for page load
    return driver


class TestCalculatorBasicOperations:
    """Test suite for basic calculator operations"""
    
    def test_addition(self, calculator):
        """Test: 5 + 3 = 8"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='5']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-op='+']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='3']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-fn='equals']").click()
        
        assert display.get_attribute("value") == "8"
    
    def test_subtraction(self, calculator):
        """Test: 10 - 4 = 6"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='1']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='0']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-op='-']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='4']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-fn='equals']").click()
        
        assert display.get_attribute("value") == "6"
    
    def test_multiplication(self, calculator):
        """Test: 6 * 7 = 42"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='6']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-op='*']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='7']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-fn='equals']").click()
        
        assert display.get_attribute("value") == "42"
    
    def test_division(self, calculator):
        """Test: 20 / 4 = 5"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='2']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='0']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-op='/']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='4']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-fn='equals']").click()
        
        assert display.get_attribute("value") == "5"
    
    def test_decimal_numbers(self, calculator):
        """Test: 3.5 + 2.5 = 6"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='3']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='.']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='5']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-op='+']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='2']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='.']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='5']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-fn='equals']").click()
        
        assert display.get_attribute("value") == "6"


class TestCalculatorFunctions:
    """Test suite for calculator functions"""
    
    def test_clear_function(self, calculator):
        """Test: Clear button resets to 0"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='9']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='8']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='7']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-fn='clear']").click()
        
        assert display.get_attribute("value") == "0"
    
    def test_delete_function(self, calculator):
        """Test: Delete button removes last digit"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='1']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='2']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='3']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-fn='delete']").click()
        
        assert display.get_attribute("value") == "12"
    
    def test_chained_operations(self, calculator):
        """Test: 5 + 3 + 2 = 10"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='5']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-op='+']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='3']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-op='+']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='2']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-fn='equals']").click()
        
        assert display.get_attribute("value") == "10"


class TestCalculatorKeyboard:
    """Test suite for keyboard input"""
    
    def test_keyboard_numbers(self, calculator):
        """Test: Typing numbers with keyboard"""
        from selenium.webdriver.common.keys import Keys
        display = calculator.find_element(By.ID, "display")
        
        display.send_keys("42")
        assert display.get_attribute("value") == "42"
    
    def test_keyboard_operations(self, calculator):
        """Test: Keyboard operations and equals"""
        from selenium.webdriver.common.keys import Keys
        display = calculator.find_element(By.ID, "display")
        
        display.send_keys("8")
        display.send_keys("+")
        display.send_keys("2")
        display.send_keys("=")
        
        assert display.get_attribute("value") == "10"
    
    def test_keyboard_backspace(self, calculator):
        """Test: Backspace key for delete"""
        from selenium.webdriver.common.keys import Keys
        display = calculator.find_element(By.ID, "display")
        
        display.send_keys("456")
        display.send_keys(Keys.BACKSPACE)
        
        assert display.get_attribute("value") == "45"


class TestCalculatorEdgeCases:
    """Test suite for edge cases"""
    
    def test_leading_zero(self, calculator):
        """Test: Leading zeros are handled"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='0']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='5']").click()
        
        assert display.get_attribute("value") == "5"
    
    def test_multiple_decimal_points_prevented(self, calculator):
        """Test: Only one decimal point allowed per number"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='3']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='.']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='1']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='.']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='4']").click()
        
        # Second decimal point should be ignored
        assert display.get_attribute("value") == "3.14"
    
    def test_negative_result(self, calculator):
        """Test: Negative results work correctly"""
        display = calculator.find_element(By.ID, "display")
        
        calculator.find_element(By.CSS_SELECTOR, "[data-num='3']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-op='-']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-num='8']").click()
        calculator.find_element(By.CSS_SELECTOR, "[data-fn='equals']").click()
        
        assert display.get_attribute("value") == "-5"
