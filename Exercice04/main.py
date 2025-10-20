class MyClass:
    """Représente une personne avec un nom complet."""

    def __init__(self, full_name):
        self.full_name = full_name

    def display_name(self):
        """Affiche le nom complet."""
        print("Le nom complet est :", self.full_name)


class OtherClass:
    """Représente une personne avec prénom et nom de famille séparés."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display_name(self):
        """Affiche le prénom et le nom de famille."""
        print(f"Nom complet : {self.first_name} {self.last_name}")
