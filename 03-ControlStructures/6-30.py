n = 5
matrix = []

for i in range(n):
    row = [0] * n
    row[i] = 1        # na przekątnej (indeks wiersza == indeks kolumny) wstawiamy 1
    row[n- 1 - i] = 1
    matrix.append(row)

# Wypisanie ładnie wiersz po wierszu:
for row in matrix:
    print(*row)