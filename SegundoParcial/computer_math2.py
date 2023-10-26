

class Computer_math2:
    def __init__(self):
        pass
    def number_theory(self):
        #Introducción a la teoría de números 
        pass
    def max_common_divisor(self):
        #El algoritmo de la división, máximo común divisor y mínimo común múltiplo 
        pass
    def prime_numbers(self):
        '''
        2.3. Números primos 

            2.3.1.Divisores 

            2.3.2.Obtención de números primos 

            2.3.3.Factorización prima 
        '''
        pass
    def euclides_extended(self):
        #euclides y euclides extendido
        pass
    def modular_aritmetic(self):
        #Aritmética Modular
        pass
    def residual_class(self,num_Z):
        print("\n\tClases Residuales\n")
        print(f"m: {num_Z}")

        divisibilities = []
        num_Zm = []
        new = 0
        iterative_numsZ = set()

        for i in range(num_Z):
            num_Zm.append(i)
            if (i == num_Z - 1):
                break

        print("Zm =",num_Zm)
        for i in num_Zm:
            new = num_Zm[i] * (-1)
            iterative_numsZ.add(new)
            iterative_numsZ.add(num_Zm[i])

        for i in num_Zm:
            wished_residue = i
            for j in iterative_numsZ:
                new = num_Z * j + wished_residue
                divisibilities.append(new)
            print(f"Zm ( {wished_residue} ) = {divisibilities}")
            divisibilities.clear()

    def induction_math(self):
        #Inducción Matemática
        pass

    def permutations_combinations(self):
        #Permutaciones y combinaciones
        pass


'''
    2.1. Introducción a la teoría de números 

    2.2. El algoritmo de la división, máximo común divisor y mínimo común múltiplo 

    2.3. Números primos 

        2.3.1.Divisores 

        2.3.2.Obtención de números primos 

        2.3.3.Factorización prima 

    2.4. Euclides extendido 

    2.5. Aritmética Modular 

    2.6. Inducción Matemática

    2.7 Permutaciones y combinaciones
'''