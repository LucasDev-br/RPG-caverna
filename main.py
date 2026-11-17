def ponto_de_espaco():
    ponto_de_espaco = "-"

    print(ponto_de_espaco * 118)
    print()

def inventario():
    n = 5
    inventario = []
    for i in range(n):
        inventario.append(0)
    return inventario

def mostrar_inventario(inventario):
    print("Inventário:")
    m = 0
    for i in range(len(inventario)):
        if inventario[i] > 0:
            m += 1
    if m == 0:
        print("O inventário está vazio.")
    else:
        print(f"Total de itens: {m}")
        for i in range(len(inventario)):
            
    
