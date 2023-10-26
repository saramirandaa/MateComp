
def residual_class(num_Z):
    print("\n\tClases Residuales\n")
    print(f"m: {num_Z}")
    divisibilities = []
    num_Zm = []
    new = 0
    for i in range(num_Z):
        num_Zm.append(i)
        if (i == num_Z - 1):
            break

    print("Zm =",num_Zm)
    iterative_numsZ = set()
    for i in num_Zm:
        new = num_Zm[i] * (-1)
        iterative_numsZ.add(new)
        iterative_numsZ.add(num_Zm[i])

    #Cambiar el residuo deseado de la lista de Zm
    for i in num_Zm:
        wished_residue = i
        for j in iterative_numsZ:
            new = num_Z * j + wished_residue
            divisibilities.append(new)
        print(f"Da como residuo {wished_residue} = {divisibilities}")
        divisibilities.clear()


def main():
    residual_class(7)
    
if __name__ == '__main__':
    main()