from base import BaseScenario
from selenium.webdriver.common.by import By


class QuantityScenario(BaseScenario):

  def getSelectedItemsAuto(self):

    # Get only first three elements
    item_elems = self.driver.find_elements(by=By.CLASS_NAME, value="inventory_item")
    item_elems = item_elems[:3]

    for item_elem in item_elems:

      button_add_cart = item_elem.find_element(by=By.TAG_NAME, value="button")
      button_add_cart.click()

    return item_elems