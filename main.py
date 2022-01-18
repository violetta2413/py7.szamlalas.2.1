'''
2.1 Feladat
A program számolja össze, hogy hány darab 'A' vagy 'a' betűvel kezdődő szó van a szavak listában.
A képernyőre írja is ki a feltételnek megfelelő szavakat!
szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
'''


szavak = ['alma', 'barack', 'Attila', 'kávé', 'szekrény', 'asztal']
as_szavak = [szo for szo in szavak if szo[0] in {"a","A"}]
print(len(as_szavak))
print(as_szavak)
