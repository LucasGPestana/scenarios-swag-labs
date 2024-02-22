from filters import FilterScenario

if __name__ == "__main__":

  third_scenario = FilterScenario("https://www.saucedemo.com/inventory.html")

  if third_scenario.comparePriceWithExpectedResult():

    print("Os resultados foram iguais!")
  
  else:

    print("Os resultados foram diferentes!")