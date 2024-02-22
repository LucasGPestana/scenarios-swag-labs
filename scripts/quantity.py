from base import BaseScenario
from selenium.webdriver.common.by import By


class QuantityScenario(BaseScenario):

  def getSelectedItemsAuto(self):
    
    # Get only first three elements
    item_elems = self.driver.find_elements(by=By.CLASS_NAME, value="inventory_item")
    item_elems = item_elems[:3]

    # Step 1: User clicks on "Add to cart" button that corresponds three selected products 
    for item_elem in item_elems:

      button_add_cart = item_elem.find_element(by=By.TAG_NAME, value="button")
      button_add_cart.click()

    # Step 2: System adds products on cart
    # Step 3: System adds quantity icon next to cart icon
    return item_elems
  
  def compareQuantityWithExpectedResult(self):

    getted_item_elems = self.getSelectedItemsAuto()

    # WebElement that represents quantity icon
    expected_quantity_item = self.driver.find_element(by=By.CLASS_NAME, value="shopping_cart_badge")

    print("\033[1;34mGETTED \033[m|\033[1;32m EXPECTED\033[m")
    print(f"\033[1;34m{len(getted_item_elems)} \033[m|\033[1;32m {expected_quantity_item.text}\033[m")

    return len(getted_item_elems) == int(expected_quantity_item.text)