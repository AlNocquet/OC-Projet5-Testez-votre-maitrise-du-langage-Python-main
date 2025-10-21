
def square(x):
    """
    Renvoie le carré d'un nombre.


    Paramètres:
    x (int or float): Le nombre à mettre au carré.


    Retourne:
    int or float: Le carré de x, ou None si x n'est pas un nombre.
    """

    if not isinstance(x, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return x * x # Calcul et retour du carré


if __name__ == "__main__":
    tests = [5, -3, 2.5, "abc", None]
    for val in tests:
        result = square(val)
        print(f"square({val!r}) = {result}")