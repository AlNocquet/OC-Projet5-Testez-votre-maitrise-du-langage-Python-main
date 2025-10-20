students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}


name = input("Entrez le nom de l’étudiant : ")

if name in students:
    notes = students[name]
    print(f"Notes de {name} :")
    for matiere, note in notes.items():
        print(f"{matiere} : {note}")
    moyenne = sum(notes.values()) / len(notes)
    print(f"Moyenne de {name} : {moyenne}")
else:
    print(f"L'étudiant {name} n'existe pas dans la liste.")