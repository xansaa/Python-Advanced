n = int(input())
matrix = [[int(el) for el in input().split()] for el in range(n)]

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][- i - 1] for i in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))