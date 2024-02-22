from filters import FilterScenario

if __name__ == "__main__":

  fourth_scenario = FilterScenario("https://www.saucedemo.com/inventory.html", True)

  if fourth_scenario.comparePriceWithExpectedResult():

    print("Os resultados foram iguais!")
  
  else:

    print("Os resultados foram diferentes!")