a = input("a: ")
b = input("b: ")
nwd = 0
it1 = 0
it2 = 0
c = 0
d = 0

try:
    val = int(a)
except ValueError:
    print("Podaj liczby obie ujemne lub obie dodatnie, całkowite, różne od 0!")
    quit()

if int(a) > 0 and int(b) < 0: 
    print("Podaj liczby obie ujemne lub obie dodatnie, całkowite, różne od 0!")
    quit()

if int(b) > 0 and int(a) < 0: 
    print("Podaj liczby obie ujemne lub obie dodatnie, całkowite, różne od 0!")
    quit()

if int(a) < 0 and int(b) < 0:
    a = int(a)
    a = abs(a)
    b = int(b)
    b = abs(b)

if int(a) == 0  or int(b) == 0:
    print("Podaj liczby obie ujemne lub obie dodatnie, całkowite, różne od 0!")
    quit()
    
c = int(c) + int(a)
d = int(d) + int(b)
while c != d:
    it2 += 1
    if c > d:
        c = c - d
    else:
        d = d - c     
while int(b) > 0:
    it1 += 1
    r = int(a) % int(b)
    a = b
    b = r

nwd = a
    
print("NWD = ", int(nwd))
print("L_iteracji (I metoda) = {}".format(it1))
print("L_iteracji (II metoda) = {}".format(it2))
quit()