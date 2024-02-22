from base import BaseScenario
from selenium.webdriver.common.by import By
import sys


class FilterScenario(BaseScenario):

    # value True in reverse attribute indicates Z to A order (or high to low price)
    def __init__(self, base_url: str, reverse: bool = False):

        self.reverse = reverse
        super().__init__(base_url)

    # Get a list of WebElement instances resulted by "Name A to Z" (or "Name Z to A", in cases of reverse equals True) filter
    def getItemsNameAuto(self):

        if self.base_url != self.driver.current_url:

            sys.exit("A URL atual é diferente da URL base!")

        else:

            # Step 1: User clicks on filter button under cart button
            filter_elem = self.driver.find_element(
                by=By.CLASS_NAME, value="product_sort_container")
            filter_elem.click()

            # Step 2: User selects "Name (A to Z)" (or "Name (Z to A)") option between filter options
            option_filter_elems = filter_elem.find_elements(
                by=By.TAG_NAME, value="option")

            selected_option_elem = list(filter(lambda x: x.get_attribute("value") == "az", option_filter_elems))[
                0] if not self.reverse else list(filter(lambda x: x.get_attribute("value") == "za", option_filter_elems))[0]
            selected_option_elem.click()

            # Step 3: System loads page with product cards sorted by alphabetical order
            # Get all items, now sorted
            item_elems = self.driver.find_elements(
                by=By.CLASS_NAME, value="inventory_item")

            return item_elems

    # Function used on sorted built-in function
    @staticmethod
    def sortItemsByName(item_elem):

        name_elem = item_elem.find_element(
            by=By.CLASS_NAME, value="inventory_item_name")

        return name_elem.text

    # Shows getted (User simulation) and expected name items and compares their lists that contains WebElement instances, returning a boolean that indicates their similarity
    def compareNameWithExpectedResult(self):

        getted_item_elems = self.getItemsNameAuto()

        item_elems = self.driver.find_elements(
            by=By.CLASS_NAME, value="inventory_item")

        excepted_item_elems = sorted(
            item_elems, key=FilterScenario.sortItemsByName, reverse=self.reverse)

        print("\033[1;34mGETTED \033[m|\033[1;32m EXPECTED\033[m")
        for i in range(len(getted_item_elems)):

            getted_name_item_elem = getted_item_elems[i].find_element(
                by=By.CLASS_NAME, value="inventory_item_name")
            expected_name_item_elem = excepted_item_elems[i].find_element(
                by=By.CLASS_NAME, value="inventory_item_name")

            print(f"\033[1;34m{getted_name_item_elem.text} \033[m|\033[1;32m {
                  expected_name_item_elem.text}\033[m")

        return getted_item_elems == excepted_item_elems
    
    def getItemsPriceAuto(self):

        if self.base_url != self.driver.current_url:

            sys.exit("A URL atual é diferente da URL base!")
        
        else:

            filter_elem = self.driver.find_element(by=By.CLASS_NAME, value="product_sort_container")
            filter_elem.click()

            option_filter_elems = filter_elem.find_elements(by=By.TAG_NAME, value="option")

            selected_option_elem = list(filter(lambda x: x.get_attribute("value") == "lohi", option_filter_elems))[0] if not self.reverse else list(filter(lambda x: x.get_attribute("value") == "hilo", option_filter_elems))[0]
            selected_option_elem.click()

            item_elems = self.driver.find_elements(by=By.CLASS_NAME, value="inventory_item")

            return item_elems