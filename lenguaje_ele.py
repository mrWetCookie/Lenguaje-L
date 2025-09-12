def pertenece_al_lenguaje(cadena):
    if len(cadena) > 0 and cadena[0] == 'a' and cadena[-1] == 'x':
        return True
    return False

def main():
    print("=== Verificación de cadenas en el lenguaje L ===")
    cadenas = []

    for i in range(4):
        cadena = input(f"Digite la cadena num [{i+1}]: ")
        cadenas.append(cadena)

    print("\n============= Resultados =============")
    print("{:<15} {:<10} {:<10} {:<20}".format("Cadena", "Inicio", "Fin", "Pertenece a L"))
    print("-"*55)

    for cadena in cadenas:
        inicio = cadena[0] if len(cadena) > 0 else "Vacía"
        fin = cadena[-1] if len(cadena) > 0 else "Vacía"
        pertenece = "Sí ✅" if pertenece_al_lenguaje(cadena) else "No ❌"
        print("{:<15} {:<10} {:<10} {:<20}".format(cadena, inicio, fin, pertenece))

if __name__ == "__main__":
    main()