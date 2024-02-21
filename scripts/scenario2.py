from filters import FilterScenario

if __name__ == "__main__":

  second_cenario = FilterScenario("https://www.saucedemo.com/inventory.html", True)
  if second_cenario.compareNameWithExpectedResult():
    print("Os resultados foram iguais!")
  else:
    print("Os resultados foram diferentes!")