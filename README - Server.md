Descrição:
Este repositório contém a implementação de um modelo RPC em uma arquitetura cliente-servidor usando Python, com a biblioteca xmlrpc.
O sistema oferece uma função como serviço no servidor, capaz de realizar cálculos específicos a pedido do cliente. 
A função no servidor (calcular_funcao) calcula valores baseados em três parâmetros: X (tipo de operação - exponencial ou log), Y e Z.

Observações:

Certifique-se de ter o Python instalado.
O servidor estará aguardando chamadas no endereço http://localhost:8000.

Exemplo de Uso:
Calcular exponencial (X='exponencial') de Y elevado a Z:

função = 'exponencial'
y = 2
z = 3
Calcular logaritmo (X='log') de Y na base Z:

função = 'log'
y = 8
z = 2
