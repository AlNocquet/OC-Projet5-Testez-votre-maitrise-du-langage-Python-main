class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = float(balance)

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Le montant du dépôt doit être positif.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
        if amount > self.balance:
            raise ValueError("Fonds insuffisants pour effectuer ce retrait.")
        self.balance -= amount
        return self.balance

    def display_balance(self) -> None:
        print(f"Titulaire: {self.account_holder} | Solde: {self.balance:.2f} €")


# --- Test ---
if __name__ == "__main__":
    compte = BankAccount("Alice", 100.0)
    compte.display_balance()       # Titulaire: Alice | Solde: 100.00 €
    compte.deposit(50)             # Nouveau solde: 150.00 €
    compte.withdraw(20)            # Nouveau solde: 130.00 €
    compte.display_balance()       # Titulaire: Alice | Solde: 130.00 €