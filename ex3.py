y = input("y: ")
skok = input("skok: ")

nls = 0
c = 0

try:
    y = int(y)
    skok = int(skok)
except:
    print("Podaj liczbę o z przedziału 0 do 600!")
    quit()

if y <= 600 and y >= 0 and skok <= 10 and skok >= 0:
    while y > 0:
        nls += 1
        y -= skok
        c += 1
        if c == 10:
            if skok > 0:
                print("Liczba skoków: -1")
                quit()
            else: 
                skok -= 1
                c = 0 
else:
    print("Podaj szerokość łaki(0 - 600) oraz długość skoku(0 - 10)")
    quit()

print("Liczba skoków: {}".format(nls))
