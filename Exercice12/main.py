class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, year={self.year!r})"


class Library:
    def __init__(self):
        self.books = []           # livres disponibles (objets Book)
        self.borrowed_books = []  # livres empruntés (objets Book)

    # --- utilitaire interne ---
    @staticmethod
    def _find_by_title(books_list, book_title: str):
        """Retourne l'index du livre (ou -1) dans la liste selon le titre (insensible à la casse)."""
        target = book_title.strip().lower()
        for i, b in enumerate(books_list):
            if b.title.strip().lower() == target:
                return i
        return -1

    # --- méthodes demandées ---
    def add_book(self, book: Book) -> bool:
        """Ajoute un livre si un livre du même titre n'existe pas déjà (disponible ou emprunté)."""
        if (self._find_by_title(self.books, book.title) != -1 or
                self._find_by_title(self.borrowed_books, book.title) != -1):
            return False
        self.books.append(book)
        return True

    def remove_book(self, book_title: str) -> bool:
        """Supprime un livre (par son titre) uniquement s'il est disponible."""
        idx = self._find_by_title(self.books, book_title)
        if idx == -1:
            return False
        self.books.pop(idx)
        return True

    def borrow_book(self, book_title: str) -> bool:
        """Emprunte un livre (par son titre) s'il est disponible."""
        idx = self._find_by_title(self.books, book_title)
        if idx == -1:
            return False
        book = self.books.pop(idx)
        self.borrowed_books.append(book)
        return True

    def return_book(self, book_title: str) -> bool:
        """Retourne un livre (par son titre) s'il est actuellement emprunté."""
        idx = self._find_by_title(self.borrowed_books, book_title)
        if idx == -1:
            return False
        book = self.borrowed_books.pop(idx)
        self.books.append(book)
        return True

    def available_books(self):
        """Liste des titres disponibles."""
        return [b.title for b in self.books]

    # Renommée pour éviter le conflit nom attribut <-> méthode
    def list_borrowed_books(self):
        """Liste des titres empruntés."""
        return [b.title for b in self.borrowed_books]


# --- Test ---
if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("1984", "George Orwell", 1949))
    lib.add_book(Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943))
    lib.add_book(Book("Fondation", "Isaac Asimov", 1951))

    print("Disponibles:", lib.available_books())
    lib.borrow_book("1984")
    print("Disponibles après emprunt:", lib.available_books())
    print("Empruntés:", lib.list_borrowed_books())
    lib.return_book("1984")
    print("Disponibles après retour:", lib.available_books())