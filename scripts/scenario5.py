from quantity import QuantityScenario

if __name__ == "__main__":

  fifth_scenario = QuantityScenario("https://www.saucedemo.com/inventory.html")

  try:
  
    fifth_scenario.compareQuantityWithExpectedResult()
  
  except AssertionError:

    print("As quantidades são diferentes!")