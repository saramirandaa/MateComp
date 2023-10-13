#Comprobar con los primeros cinco primos cuales son primos de mersenne y cuales son numeros perfectos 

primes = [2, 3, 5, 7, 13]
mersenne = []
perfects = []

def is_prime(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or (numero % 3 == 0 and numero != 3):
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect(num):
    for n in range(1,num):
        if num % n == 0:
            return True
    return False

[mersenne.append(2**(x)-1) for x in primes]

for n in mersenne:
    if is_prime(n):
        perfects.append(2**(n-1))
        if is_perfect(n):
            if perfects[-1]>10000000000:
                print(n, 'Es primo y su perfecto es un número muy grande para desplegarlo en pantalla')
            else:
                print(n, 'Es primo y su perfecto es ', perfects[-1])
    else:
        print(n, 'Es primo pero no es perfecto')



# print('Mersenne: ', mersenne)
# print('Perfects: ',perfects)