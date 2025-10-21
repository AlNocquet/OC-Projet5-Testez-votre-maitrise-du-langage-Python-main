
def calculate_average(numbers):
    """
    Calcule la moyenne d'une liste de nombres.

    Paramètres:
    numbers (list of int or float): Liste de nombres dont on veut calculer la moyenne.

    Retourne:
    float: La moyenne des nombres. Renvoie 0 si la liste est vide.
    """

    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # Exemple d'utilisation de la fonction
    
    numbers = [10, 20, 30, 40, 50]
    average = calculate_average(numbers)
    print("La moyenne est :", average)