# PROJETO PYTHON: Conexão LDAP

> Modelo de Script de conexão com o sistema LDAP, que retorna os usuários encontrados de cada grupo.

# Tecnologias Utilizadas

* **_VScode_**;

* **_Python3;_** 

  

# Bibliotecas e Configurações

### Bibliotecas Utilizadas

```python
import requests
import time
import os
import logging
import json
```

### Configurações

> O script foi feito com base na estrutura POO.

```python
class Conexao:
    def __init__(self):

usuario = Conexao()
usuario.Retorna_Users()
```

# Fontes

> http://apidocs.axway.com/swagger-ui-st/admin-20/

# Detalhes de Processo

### LOG

```python
# Configuração da LOG.
1. self.data_exec = time.strftime("%Y/%m/%d")
2. self.log_folder = self.dirScripts + 'LOGS/' + self.data_exec + '/'
3. os.makedirs(os.path.dirname(self.log_folder), exist_ok=True)
4. logging.basicConfig(level=logging.INFO,
5.                   format='%(asctime)s %(name)-12s %(levelname)-8s  (message)s',
6.                   datefmt='%d/%m/%Y - %H:%M:%S',
7.                   filename=self.log_folder + 'Conexao_LDAP.log',
8.                   filemode='a')
9. self.logger = logging.getLogger('Processo')
```

> Linha 1: Cria uma variável que recebe o Ano / Mês / Dia atual.
>
> Linha2:   Cria uma variável com o diretório que a LOG vai seguir.
>
> Linha 3: Cria o diretório.
>
> Linha 4, 5, 6, 7, 8: Faz a configuração da LOG (Formato / Data-Hora / Nome / Tipo) .
>
> Linha 9:  Nome de cada etapa da LOG.

### Configuração JSON

```json
{
    "MFT":{
        "Host": "",
        "User": "",
        "Password": ""
    }
}
```

> O arquivo config.json serve para armazenar as configurações de conexão do LDAP, isso ajuda a não ter que alterar dentro do script toda vez que algum parâmetro for trocado, podendo apenas modificar o JSON.

> Objetos que são armazenados:
>
> __Host:__ Onde que será conectado (12.345.67.890 ou host.com.br)
>
> __User:__ usuário que está conectando no LDAP (Fulano A, Fulano B, ...)
>
> __Password:__ A senha que é usada para se conectar com o LDAP.
>

``` python
1. try:
2.   with open('./config.json') as f:
3.    self.config = json.load(f)
4.    self.logger.info('Arquivo de configuração carregado com sucesso')
5. except Exception as error:
6.    self.logger.error('Problemas ao carregar arquivo de configuração - ERROR: {}'.format(str(error)))
7.    exit(1)
```

> Linha 1: Chama a função de Try.
>
> Linha 2:  Abre o arquivo __config.json__ e coloca em uma variável chamada __f__.
>
> Linha 3:  Cria uma variável  que recebe arquivo carregado como JSON.
>
> Linha 4: Faz uma chamada de LOG com tipo INFO.
>
> Linha 5:  Chama a Exceção e da uma apelido de __error__ (criado junto com o Try), serve para retornar caso tenha algum erro de execução.
>
> Linha 6: Faz uma chamada de LOG com tipo ERROR.
>
> Linha 7: Fecha o programa com o comando __exit()__.



### Configurações MFT

```python
1  try:
2.    self.host = self.config['MFT']['Host']
3.    self.user = self.config['MFT']['User']
4.    self.password = self.config['MFT']['Password']
5.    self.url = requests.get(self.host + '/administrators', auth=(self.user, self.password), verify=False)
6.    self.logger.info('MFT conectado com sucesso')
7. except Exception as erro:
8.    self.logger.error('MFT: Problemas ao realizar requisições no MFT - ERROR: {}'.format(erro))
9.    exit(1)
```

> Linha 1:  Chama a função de Try.
>
> Linha 2: Pega o host de conexão no config.json
>
> Linha 3: Pega o nome do usuário no config.json
>
> Linha 4: Pega a senha do usuário no config.json
>
> Linha 5: Faz a operação __GET__ na URL -> (<host>, /administrators, auth=(<user>, <password>), verify=False)
>
> Linha 6: Faz uma chamada de LOG com tipo INFO.
>
> Linha 7: Chama a Exceção.
>
> Linha 8: Faz uma chamada de LOG com tipo ERROR.
>
> Linha 9: Fecha  o programa.

# Listas

```python
# Cria uma lista onde será armazenado os usuários.
self.usuarios_mft = []
```

# Retorno dos Dados

```python
1. def Retorna_user(self):
2.    data = self.url.json()
3.	  
4.    for admin in data['administrators']:
5.       self.usuarios_mft.append(admin['loginName'])
6.   self.logger.info('Usuários MFT: {}'.format(self.usuarios_mft))
7.
8.   print(self.usuarios_mft)
```

> Linha 1: Cria a função __Retorna_Users__.
>
> Linha 2: Cria uma variável que recebe os dados obtidos em formato JSON.
>
> Linha 4: Cria um laço que passa pelo objeto __administrators.__
>
> Linha 5: Insere na lista o objeto __LoginName__ dos usuários.
>
> Linha 6: Faz uma chamada de LOG com tipo INFO.
>
> Linha 8: Retorna a lista de __usuários MFT__ .