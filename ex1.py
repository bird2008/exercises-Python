password = input("Podaj łańcuch zawierający 16 znaków: ")

if len(password) in {14,15}:
    password = password[::2] 
    password.replace(password[3], password[4])
    print(password[::-1])
else:
    print("Błedny łańcuch! Łańcuch musi zawierać 15 albo 16 znaków")
    