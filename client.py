import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")

def calcular_no_servidor(x, y, z):
    resultado = proxy.calcular_funcao(x, y, z)
    return resultado

# Exemplo de uso
funcao = 'exponencial'  # ou 'log'
y = 2
z = 3

resultado = calcular_no_servidor(funcao, y, z)
print(f"Resultado do cálculo no servidor: {resultado}")
