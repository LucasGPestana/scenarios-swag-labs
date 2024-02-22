from quantity import QuantityScenario

if __name__ == "__main__":

  fifth_scenario = QuantityScenario("https://www.saucedemo.com/inventory.html")

  if fifth_scenario.compareQuantityWithExpectedResult():

    print("Os resultados foram iguais!")
  
  else:

    print("Os resultados foram diferentes!")