import requests
import time
import os
import logging
import json


class Conexao:
    # Método construtor.
    def __init__(self):

        # Configurações LOG.
        self.data_exec = time.strftime("%Y/%m/%d")
        self.log_folder = './LOGS/' + self.data_exec + '/'
        os.makedirs(os.path.dirname(self.log_folder), exist_ok=True)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%d/%m/%Y - %H:%M:%S',
                            filename=self.log_folder + 'Verificao_Processos.log',
                            filemode='a')
        self.logger = logging.getLogger('Processo')

        # Carrega o JSON config.
        try:
            with open('./config.json') as f:
                self.config = json.load(f)
            self.logger.info('Arquivo de configuração carregado com sucesso')
        except Exception as e:
            self.logger.error('Problemas ao carregar arquivo de configuração - ERROR: {}'.format(str(e)))
            exit(1)
        
        # Configurações MFT.
        try:
            self.host = self.config['MFT']['Host']
            self.user = self.config['MFT']['User']
            self.password = self.config['MFT']['Password']
            self.url = requests.get(self.host + '/administrators', auth=(self.user, self.password), verify=False)
            self.logger.info('MFT conectado com sucesso')
        except Exception as erro:
            self.logger.error('MFT: Problemas ao realizar requisições no MFT - ERROR: {}'.format(erro))
            exit(1)
        
        # Listas.
        self.usuarios_mft = []

    # Método que retorna os usuários do MFT. 
    def Retorna_Users(self):
        # Deixa os dados em formato JSON.
        data = self.url.json()

        # Passa pelo JSON e insere os campos específicos.
        for admin in data['administrators']:
            self.usuarios_mft.append(admin['loginName'])
        self.logger.info('Usuários MFT: {}'.format(self.usuarios_mft))

        print(self.usuarios_mft)

usuario = Conexao()
usuario.Retorna_Users()
