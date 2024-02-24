from filters import FilterScenario

if __name__ == "__main__":

  second_scenario = FilterScenario("https://www.saucedemo.com/inventory.html", True)

  try:

    second_scenario.compareNameWithExpectedResult()
  
  except AssertionError:

    print("As listas são diferentes!")