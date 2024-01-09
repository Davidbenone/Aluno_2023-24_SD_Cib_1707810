![Uma imagem contendo Texto Descrição gerada automaticamente](https://github.com/Davidbenone/Aluno_2023-24_SD_Cib_1707810/blob/main/Imagens/logo.png)

Relatório do Trabalho prático

Sistemas Distribuídos

Servidor RPC calcular e retornar o seu valor

Aluno: David Sávio Benone Sabbá De Lima

Número: 1707810

GitHub: https://github.com/Davidbenone/Aluno_2023-24_SD_Cib_1707810

Email: davidbenone08@gmail.com

Sumário

**Descrição do Trabalho** 1

**Funcionamento do trabalho** 2

**Funcionamento do trabalho** **3**

**Conclusão** 4

**Bibliografia** 4

## Descrição do Trabalho

![Diagrama Descrição gerada automaticamente](https://github.com/Davidbenone/Aluno_2023-24_SD_Cib_1707810/blob/main/Imagens/modelo.png)O projeto consiste na implementação de uma arquitetura cliente-servidor com um modelo RPC (Remote Procedure Call). O servidor oferece uma função como serviço, calcular_funcao, capaz de realizar cálculos específicos baseados em parâmetros fornecidos pelo cliente. A função pode executar operações como exponenciação ou logaritmo, dependendo do valor de X, que é enviado pelo cliente. A comunicação entre o cliente e o servidor é facilitada pela biblioteca xmlrpc do Python.

**Implementação do Trabalho**

A implementação do trabalho está organizada em dois principais componentes: o servidor (server.py) e o cliente (client.py). O servidor utiliza a biblioteca xmlrpc para criar um servidor RPC, enquanto o cliente se comunica remotamente com o servidor para realizar cálculos específicos. O código é modular e segue as melhores práticas de organização.

![Texto Descrição gerada automaticamente](https://github.com/Davidbenone/Aluno_2023-24_SD_Cib_1707810/blob/main/Imagens/1.1.png)![Texto Descrição gerada automaticamente](media/9cf89ebf374d6d84f80a24cab6e1e171.png)  
Funcionamento do trabalho

O funcionamento do sistema envolve a execução do servidor, que aguarda chamadas remotas da função calcular_no_servidor feitas pelo cliente. O cliente especifica o tipo de operação (X), e os valores (Y e Z) necessários para o cálculo. O servidor recebe esses parâmetros, executa a operação correspondente na função calcular_funcao e retorna o resultado ao cliente.

![Texto Descrição gerada automaticamente](media/ef32d5ae9046b5fac1b871727ab43f96.png)![Texto Descrição gerada automaticamente](media/8facc844df81224cf5c90dbc095abe01.png)

## Conclusão

O funcionamento do sistema envolve a execução do servidor, que aguarda chamadas remotas da função calcular_no_servidor feitas pelo cliente. O cliente especifica o tipo de operação (X), e os valores (Y e Z) necessários para o cálculo. O servidor recebe esses parâmetros, executa a operação correspondente na função calcular_funcao e retorna o resultado ao cliente.

Bibliografia

[1] Paulo Vieira - Servidor RPC - <https://moodle.ipg.pt/mod/folder/view.php?id=71813>

[2] Documentação da biblioteca xmlrpc do Python: Python xmlrpc

[3] ChatGPT - Consultas sobre o python, verificação do código - <https://chat.openai.com/>
