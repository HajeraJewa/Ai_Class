x = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10, 7, 9, 8, 1, 5, 7, 8, 9, 10, 4]
y = int(input("Masukkan nilai x yang ingin dicari: ")) 

if y in x and y % 2 == 0:
    indeks = [i for i, nilai in enumerate(x) if nilai == y]
    print("Indeks ke :", indeks)
else:
    print("Bukan Bilangan Genap")