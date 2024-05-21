def find_two_smallest(numbers):
    # Inicialize min1 e min2 como os dois primeiros elementos da lista
    min1 = min(numbers[0], numbers[1])
    min2 = max(numbers[0], numbers[1])

    # Itere sobre os elementos restantes da lista
    for num in numbers[2:]:
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    return min1, min2

# Exemplo de uso
lista = [5, 3, -220, 6, 0, 1, 2, -0, -0, 4, 10]
min1, min2 = find_two_smallest(lista)
print("Os dois menores valores são:", min1, "e", min2)
