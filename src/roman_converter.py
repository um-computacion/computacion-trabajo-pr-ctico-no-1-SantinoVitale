def decimal_to_roman(decimal):
    # Si el valor no es un numero devolver TypeError
    if not isinstance(decimal, int):
        raise TypeError("El valor debe ser un número entero")
        
    # Si el decimal es mayor a 3999 o menor a 1 devolver ValueError
    if decimal < 1 or decimal > 3999:
        raise ValueError("El número debe estar entre 1 y 3999")
    
    # Definir los valores y símbolos romanos en orden descendente
    valores = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    simbolos = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    
    # Construir el número romano
    resultado = ""
    for i in range(len(valores)):
        # Mientras el número sea mayor o igual al valor actual
        while decimal >= valores[i]:
            # Agregar el símbolo correspondiente al resultado
            resultado += simbolos[i]
            # Restar el valor del número
            decimal -= valores[i]

    return resultado