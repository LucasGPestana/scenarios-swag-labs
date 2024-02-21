from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import random
import sys

class BaseScenario:

  page_url = "https://www.saucedemo.com/"

  # Initial Setup
  def __init__(self, base_url: str):

    if not BaseScenario.page_url in base_url:

      sys.exit("A URL base do cenário deve conter a URL da página!")
    
    else:

      self.base_url = base_url

    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-extension")
    options.add_argument("--window-size=1920,1080")

    # Instance of WebDriver class that represents a session between driver and a chrome instance configured by server with options defined previously.
    self.driver = webdriver.Chrome(service=service, options=options)

    self.driver.get(BaseScenario.page_url)

    self.login()
    
  # Prerequisite: User should be logged on Swag Labs
  def login(self):

    # While the browser don't recieve the response of HTTP request, the script won't continue
    while self.driver.current_url != BaseScenario.page_url:

      continue

    accepted_usernames_elem = self.driver.find_element(by=By.ID, value="login_credentials")
    accepted_passwords_elem = self.driver.find_element(by=By.CLASS_NAME, value="login_password")

    # Includes titles (First element of lists)
    accepted_usernames = accepted_usernames_elem.text.split("\n")
    accepted_passwords = accepted_passwords_elem.text.split("\n")

    # Removes these titles with a slice
    accepted_usernames = accepted_usernames[1:]
    accepted_passwords = accepted_passwords[1:]

    # First line credentials selects a random username to use, but each username on Swag Labs has a different behavior.
    # credentials = (random.choice(accepted_usernames), random.choice(accepted_passwords))
    credentials = (accepted_usernames[0], random.choice(accepted_passwords))

    form_elem = self.driver.find_element(by=By.TAG_NAME, value="form")

    input_elems = form_elem.find_elements(by=By.TAG_NAME, value="input")

    # Filters all WebElements in WebElement tagged form it hasn't value 'submit' in attribute 'type'
    text_input_elems = list(filter(lambda x: x.get_attribute("type") != "submit", input_elems))

    for i in range(len(text_input_elems)):

      text_input_elems[i].send_keys(credentials[i])
    
    # Click on submit input button (Last element in input_elems)
    input_elems[-1].click()

