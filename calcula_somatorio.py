# Sua solução aqui

n = int(input())

soma = 0.0
for i in range(2, n + 1):
    soma += i / (i * (i - 1))

print(f"{soma:.2f}")
