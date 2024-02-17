# 1 - Print -
# 2 - Variables - (Degisken, guherbar)
# 3 - Comments -  (Yorum satilari)
errors = open(file="logs/errors.txt", mode="w")
print("Ekrrana bir seyler yaziyor", end=".")

# 1. Form
print("1. Kullanici Sayfaya geldi.", file=errors)

# 2. Input - E-mail
print("2. Email adresini yazdi.", file=errors)

# 3. Input - Password
print("3. Passwod yazdi.", file=errors)

# 4. Button - Submit
print("4. Submit buttona basti.", file=errors)

errors.close()

