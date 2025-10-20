words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]


vowels = set("aeiouyAEIOUY")

result = [(word, sum(1 for c in word if c in vowels)) for word in words]

print(result)