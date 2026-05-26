# Nombre del estudiante: Daniela Gonzalez Barrera
# Grupo: 213022A_2201
# Programa: Ingeniería de telecomunicaciones
# Código Fuente: autoría propia

#Problema N3: Auditoría de inventario
 
# Función para calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Matriz de inventario [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    [101, "Lápiz", 20, 30],
    [102, "Cuaderno", 15, 20],
    [103, "Borrador", 50, 40],
    [104, "Regla", 5, 15],
    [105, "Marcador", 25, 25]
]
# Lista de pedidos
print("Lista de pedidos:")
for articulo in inventario:
    codigo, nombre, stock_actual, stock_minimo = articulo
    cantidad = calcular_pedido(stock_actual, stock_minimo)
    print(f"- {nombre}: {cantidad} unidades a pedir")

