
list1 = [1, 34, 53, 2, 23, 13]


def primero():
    print(list1)


def segundo():
    valor = int(input("Valor a Agregar: "))
    list1.append(valor)
    print(list1)


def tercero():
    primero()
    valor = int(input("Valor a Agregar: "))
    posic = int(
        input(f"Posicion para insertar (valida de 0 a {len(list1)-1}): "))
    list1.insert(posic, valor)
    print(list1)


def cuarto():
    primero()
    posic = int(
        input(f"Posicion para mostrar (valida de 0 a {len(list1)-1}): "))
    print(f"Valor de la posicion {posic}: {list1[posic]}")


def quinto():
    primero()
    posic = int(
        input(f"Posicion para eliminar (valida de 0 a {len(list1)-1}): "))
    print(f"Valor de la posicion eliminada {posic}: {list1[posic]}")
    list1.pop(posic)
    print(list1)


def sexto():
    list1.reverse()
    print(list1)


def septimo():
    list1.sort(reverse = True)
    print(list1)

def octavo():
    list1.sort()
    print(list1)

def test():
    ans = True
    while ans:
        print("""
======= Menú =======
1. Mostrar la lista actualmente
2. Adicionar un dato al final de la lista
3. Adicionar un dato en una posicion especificada de la lista
4. Consultar un dato de una posicion especifica
5. Eliminar el dato de una posicion especifica
6. Invertir el orden de la lista
7. Ordenar la lista de mayor a menor
8. Ordenar la lista de menor a mayor
9. Salir/Cerrar
====================
        """)
        ans = input("Que desea hacer?: ")
        if ans == "1":
            primero()
        elif ans == "2":
            segundo()
        elif ans == "3":
            tercero()
        elif ans == "4":
            cuarto()
        elif ans == "5":
            quinto()
        elif ans == "6":
            sexto()
        elif ans == "7":
            septimo()
        elif ans == "8":
            octavo()
        elif ans == "9":
            print("\n Goodbye")
            ans = None
        else:
            print("\n Opcion invalida, elija otra vez")


try:
    test()
except:
    print("Algo ha salido mal, por favor, intentelo de nuevo")
    test()
