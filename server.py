from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def calcular_funcao(x, y, z):
    if x == 'exponencial':
        resultado = y ** z
    elif x == 'log':
        resultado = pow(y, 1/z)
    else:
        resultado = None
    return resultado

server = SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler)
server.register_introspection_functions()
server.register_function(calcular_funcao, 'calcular_funcao')

print("Servidor RPC aguardando chamadas...")
server.serve_forever()
