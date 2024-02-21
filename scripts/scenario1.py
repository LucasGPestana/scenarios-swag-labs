from filters import FilterScenario

if __name__ == "__main__":

  first_cenario = FilterScenario("https://www.saucedemo.com/inventory.html")
  if first_cenario.compareNameWithExpectedResult():
    print("Os resultados foram iguais!")
  else:
    print("Os resultados foram diferentes!")