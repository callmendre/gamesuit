from random import choice

print("\n>>>>>>>>> Game Suit Lawan Bot <<<<<<<<<")
a = 0
b = 0
for jawaban in range(5):
    DafList = ["gunting","kertas","batu"]
    hasil = choice(DafList)

    tebak = input("\ngunting, batu, kertas ? : ")

    if tebak == "kertas":
        if hasil == "kertas":
            print("Imbang, Sama Sama ",tebak)
        elif hasil == "gunting":
            print("Kamu kalah")
            b+=1    
        elif hasil == "batu":
            print("Kamu Menang")
            a+=1

    elif tebak == "batu":
        if hasil == "batu":
            print("Imbang, Sama Sama ",tebak)
        elif hasil == "gunting":
            print("Kamu Menang")   
            a+=1 
        elif hasil == "kertas":
            print("Kamu Kalah")
            b+=1
    
    elif tebak == "gunting":
        if hasil == "gunting":
            print("Imbang, Sama Sama",tebak)
        elif hasil == "kertas":
            print("Kamu menang")    
            a+=1
        elif hasil == "batu":
            print("Kamu kalah")
            b+=1

    else:
        print("\nSepertinya jawaban kamu salah, Coba Masukkan pilihan dengan benar!!!")
else:
    print("\nJatah Nebaknya Udah Abis :( ")
    print("\nKamu Menang sebanyak = ",a); print("Botnya menang sebanyak = ",b)
    if a > b:
        print("Kamu menang dengan score = ",a,":",b)
    elif a < b:
        print("Kamu kalah dengan score = ",a,":",b)
    else:
        print("Kamu Imbang dengan score = ",a,":",b)