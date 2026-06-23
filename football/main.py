goalkeepers = {"Matej Kovar": "Czech Republic",
               "Raul Rangel": "Mexico",
               "Gianluigi Donnarumma": "Italy",
               "Ronwen Williams": "South Africa",
               "Kim Seung-gyu": "South Korea",
               "Nikola Vasilj": "Bosnia",
               "Owen Goodman": "Canada",
               "Mahmud Abunada": "Qatar",
               "Alisson": "Brazil",
               "Yassine Bounou": "Morocco",
               "Matthew Ryan": "Australia",
               "Manuel Neuer": "Germany",
               "Zion Suzuki": "Japan",
               "Bart Verbruggen": "Netherlands",
               "Thibaut Courtois": "Belgium",
               "Max Crocombe": "New Zealand",
               "Vozinha": "Cape Verde",
               "David Raya": "Spain",
               "Robin Risser": "France",
               "Emiliano Martinez": "Argentina",
               "Diogo Costa": "Portugal",
               "Dean Henderson": "England"}

defenders = {"Israel Reyes": "Mexico",
             "Derek Cornelius": "Canada",
             "Eray Comert": "Switzerland",
             "Achraf Hakimi": "Morocco",
             "Aaron Hickey": "Scotland",
             "Mark McKenzie": "USA",
             "Antonio Rudiger": "Germany",
             "Virgil van Dijk": "Netherlands",
             "Tarek Alaa": "Egypt",
             "Cristian Romero": "Argentina",
             "Gideon Mensah": "Ghana",
             "Alphonso Davies": "Canada"}

midfielders = {"Luka Modric": "Croatia",
               "Sphephelo Sithole": "South Africa",
               "Granit Xhaka": "Switzerland",
               "Scott McTominay": "Scotland",
               "Diego Gomez": "Paraguay",
               "Alan Minda": "Ecuador",
               "Jamal Musiala": "Germany",
               "Daichi Kamada": "Japan",
               "Frenkie de Jong": "Netherlands",
               "Kevin de Bruyne": "Belgium",
               "Elijah Just": "New Zealand",
               "Rodri": "Spain",
               "Martin Odegaard": "Norway",
               "Rodrigo De Paul": "Argentina",
               "James Rodriguez": "Colombia",
               "Bruno Fernandes": "Portugal",
               "Jude Bellingham": "England"}

forwards = {"Julian Quinones": "Mexico",
            "Son Heung-min": "South Korea",
            "Neymar": "Brazil",
            "Vinicius Junior": "Brazil",
            "Che Addams": "Scotland",
            "Christian Pulisic": "USA",
            "Kai Havertz": "Germany",
            "Ayase Ueda": "Japan",
            "Memphis Depay": "Netherlands",
            "Alexander Isak": "Sweden",
            "Viktor Gyokeres": "Sweden",
            "Romelu Lukaku": "Belgium",
            "Chris Wood": "New Zealand",
            "Mohammed Salah": "Egypt",
            "Mehdi Taremi": "Iran",
            "Lamine Yamal": "Spain",
            "Darwin Nunez": "Uruguay",
            "Lionel Messi": "Argentina",
            "Cristiano Ronaldo": "Portugal",
            "Sadio Mane": "Senegal",
            "Harry Kane": "England",
            "Erling Haaland": "Norway",
            "Kylian Mbappe": "France",
            "Robert Lewandowski": "Poland"}

my_team = {}

print("Football team builder!")
goalie = ""
defend1 = ""
defend2 = ""
defend3 = ""
defend4 = ""
mid1 = ""
mid2 = ""
mid3 = ""
attacker1 = ""
attacker2 = ""
attacker3 = ""
MAX_CAPACITY = 11
current_capacity = len(my_team)
while current_capacity != MAX_CAPACITY:
    goalie = input("Which goalkeeper would you like on your team? ").title()
    if goalie not in goalkeepers:
        print("{} is unavailable!".format(goalie))
    else:
        my_team[goalie] = goalkeepers.get(goalie)
    defend1 = input("Choose a defender: ").title()
    if defend1 not in defenders:
        print("{} is unavailable!".format(defend1))
    else:
        my_team[defend1] = defenders.get(defend1)
    defend2 = input("Choose a defender: ").title()
    if defend2 not in defenders:
        print("{} is unavailable!".format(defend2))
    else:
        my_team[defend2] = defenders.get(defend2)
    defend3 = input("Choose a defender: ").title()
    if defend3 not in defenders:
        print("{} is unavailable!".format(defend3))
    else:
        my_team[defend3] = defenders.get(defend3)
    defend4 = input("Choose a defender: ").title()
    if defend4 not in defenders:
        print("{} is unavailable!".format(defend4))
    else:
        my_team[defend4] = defenders.get(defend4)
    mid1 = input("Choose a midfielder: ").title()
    if mid1 not in midfielders:
        print("{} is unavailable!".format(mid1))
    else:
        my_team[mid1] = midfielders.get(mid1)
    mid2 = input("Choose a midfielder: ").title()
    if mid2 not in midfielders:
        print("{} is unavailable!".format(mid2))
    else:
        my_team[mid2] = midfielders.get(mid2)
    mid3 = input("Choose a midfielder: ").title()
    if mid3 not in midfielders:
        print("{} is unavailable!".format(mid3))
    else:
        my_team[mid3] = midfielders.get(mid3)
    attacker1 = input("Choose a forward: ").title()
    if attacker1 not in forwards:
        print("{} is unavailable!".format(attacker1))
    else:
        my_team[attacker1] = forwards.get(attacker1)
    attacker2 = input("Choose a forward: ").title()
    if attacker2 not in forwards:
        print("{} is unavailable!".format(attacker2))
    else:
        my_team[attacker2] = forwards.get(attacker2)
    attacker3 = input("Choose a forward: ").title()
    if attacker3 not in forwards:
        print("{} is unavailable!".format(attacker3))
    else:
        my_team[attacker3] = forwards.get(attacker3)

for name, country in my_team.items():
    print("Player name: {}. National team: {}".format(name, country))
