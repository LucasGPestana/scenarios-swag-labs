from filters import FilterScenario

if __name__ == "__main__":

  first_scenario = FilterScenario("https://www.saucedemo.com/inventory.html")

  try:

    first_scenario.compareNameWithExpectedResult()
  
  except AssertionError:

    print("As listas são diferentes!")