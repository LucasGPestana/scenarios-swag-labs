from filters import FilterScenario

if __name__ == "__main__":

  third_scenario = FilterScenario("https://www.saucedemo.com/inventory.html")

  try:
  
    third_scenario.comparePriceWithExpectedResult()
  
  except AssertionError:

    print("As listas são diferentes!")