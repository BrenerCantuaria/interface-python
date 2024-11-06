# Gerenciador de Dispositivos com Tkinter

Este projeto é uma aplicação de interface gráfica construída com a biblioteca Tkinter em Python. Ela permite a interação com dispositivos como ESP32 e Arduino, além de oferecer uma tela de gerenciamento de perfil de usuário.

## Funcionalidades

- **Tela de Gerenciamento da ESP32**: 
  - Verifica se um ID para o dispositivo ESP32 já existe.
  - Permite gerar um novo ID se nenhum existir.
  - Oferece a opção de gravar o novo ID no dispositivo com confirmação de gravação.
  
- **Tela de Gerenciamento do Arduino**: 
  - Exibe informações básicas do Arduino.

- **Tela de Perfil de Usuário**: 
  - Mostra informações básicas do perfil do usuário.

## Pré-requisitos

Para executar este projeto, você precisará de:
- Python 3.10  ou superior instalado em sua máquina.
- Tkinter instalado com Python (geralmente vem pré-instalado com as versões padrão do Python).

## Estrutura de Arquivos
```bash
/img
    ├── Arduino.png
    ├── energy-system.png
    ├── esp32.png
    └── perfil.png
/screens
    ├── __pycache__
    ├── __init__.py
    ├── arduino.py
    ├── centraliza_tela.py
    ├── config_screens.py
    ├── esp32.py
    ├── login.py
    └── perfil.py
/.gitignore
main.py
README.md
requirements.txt
```
# Comunicação Serial com ESP32 - Guia de Uso

## Introdução
Este é um script Python criado para facilitar a comunicação entre um computador e um dispositivo ESP32 via porta serial. Ele permite que você obtenha dados de um dispositivo ESP32, como nome do dispositivo e ID, além de enviar informações para o dispositivo.

Este documento vai te ajudar a entender o que o script faz, como ele funciona e como usá-lo, mesmo que você não tenha experiência com programação.

## Estrutura do Script
O script possui três funções principais:

- Abrir Conexão Serial (open_serial_connection): Inicia a conexão com o dispositivo ESP32.
- Obter Dados do Dispositivo (get_existing_data): Recebe informações do ESP32.
- Enviar Informações para o Dispositivo (send_device_info): Envia dados para o ESP32.

# Visão Geral das Funções
## 1. open_serial_connection(port)
  Esta função estabelece uma conexão serial com o dispositivo ESP32 em uma porta especificada.
- Parâmetros:
  - port (string): A porta onde o dispositivo ESP32 está conectado.
- Retornos:
  - serial_connection (objeto): O objeto de conexão serial se a conexão for bem-sucedida.
  - status (booleano): Retorna True se a conexão for estabelecida com sucesso, False se ocorrer um erro.
## 2. get_existing_data(serial_connection)
  Esta função solicita e recupera informações do dispositivo (ex.: nome e ID do dispositivo) do ESP32.

- Parâmetros:
  - serial_connection (objeto): Um objeto de conexão serial ativa.
- Retornos:
  - Um dicionário contendo o nome do dispositivo ("nome") e o ID do dispositivo ("id").None se nenhum dado for recebido ou se o formato dos dados estiver incorreto.
- Processo Exemplo:
```bash
  "ESP32 Dev Kit,777-111-222"
```
## 3. send_device_info(serial_connection, name, device_id)
  Esta função envia informações de identificação (nome e ID) para o ESP32.

- Parâmetros:

  - serial_connection (objeto): Um objeto de conexão serial ativa.
  - name (string): O nome do dispositivo.
  -  device_id (string): O ID único do dispositivo.
-  Processo:
  - A função formata name e device_id em uma única string, separada por uma vírgula. Envia a string de dados para o ESP32 através da conexão serial.

## Execução

Para rodar o programa, siga os passos abaixo:
1. Clone o repositório ou baixe os arquivos para sua máquina local.
   ```bash
     git clone https://github.com/BrenerCantuaria/interface-python.git
   ```
2. Navegue até o diretório do projeto.
  ```bash
    cd <nome-do-diretório-clonado>
  ```
3. Instale todas as dependências necessárias para rodar o projeto, utilizando o arquivo requirements.txt:
   ```bash
     pip install -r requirements.txt
   ```
4. Execute o comando abaixo no terminal ou prompt de comando:
   ```bash
     python main.py
   ```
