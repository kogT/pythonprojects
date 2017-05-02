anz = raw_input("Wieviele Spieler nehmen am Turnier teil? ")
Str = None
if anz == "1":
    Str = "nimmt"
else:
    Str = "nehmen"

#%s for Display and %r for Debugging
print "Es %s %s Spieler am Turnier teil. Ist das korrekt?(j/n)" %(Str, anz) 
jn = raw_input();
if jn !="j":
    print "Korrigieren Sie ihre Eingabe:"
    anz = raw_input();

if anz == "1":
    Str = "nimmt"
else:
    Str = "nehmen"
print "Es %s %s Spieler am Turnier teil." %(Str, anz)