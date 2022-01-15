def fibonacci(long):
    # variabel awal bilangan fibonacci
    f1, f2 = 0, 1
    count = 0

    # cek apakah inputan bilangan bulat positif
    if long <= 0:
       print("Bukan angka positif")
       
    # generate fibonacci sequence
    else:
       print("Urutan bilangan fibonacci : ")
       while count < long:
           print(f1, "", end="")
           temp = f1 + f2
           # update value
           f1,f2 = f2, temp
           count += 1
           if(count == long):
               print("")
        
while(True):
    val = input("Berapa banyak ? ") #menerima inputan
    try:
        long = int(val) #check apakah inputan adalah angkan atau bukan
    except ValueError:
        print("inputan bukan angka")
        continue
    fibonacci(long)
    berhenti = input("Apakah anda ingin melanjutkan ? (Y/N) : ")
    if(berhenti == 'n' or berhenti == 'N'):
        exit(0)
