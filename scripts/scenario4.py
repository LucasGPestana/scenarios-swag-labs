from filters import FilterScenario

if __name__ == "__main__":

  fourth_scenario = FilterScenario("https://www.saucedemo.com/inventory.html", True)

  try:

    fourth_scenario.comparePriceWithExpectedResult()
  
  except AssertionError:

    print("As listas são diferentes!")