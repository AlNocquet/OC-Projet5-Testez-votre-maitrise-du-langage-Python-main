
def log_decorator(func):
    """
    Décorateur qui affiche un message avant et après l'exécution d'une fonction sans arguments.
    """
    def wrapper():
        print(f"Appel de la fonction {func.__name__}")
        result = func()
        print(f"Fin de l'appel de la fonction {func.__name__}")
        return result
    return wrapper


@log_decorator
def function_test():
    """Fonction de test sans arguments."""
    print("Cette fonction ne prend pas d'arguments.")


if __name__ == "__main__":
    function_test()