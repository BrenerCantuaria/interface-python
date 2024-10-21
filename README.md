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

- `main.py`: Arquivo principal contendo o código da interface gráfica e lógica de gerenciamento.
- `img/`: Diretório contendo os ícones usados na interface gráfica.

## Execução

Para rodar o programa, siga os passos abaixo:
1. Clone o repositório ou baixe os arquivos para sua máquina local.
2. Navegue até o diretório do projeto.
3. Execute o comando abaixo no terminal ou prompt de comando:

   ```bash
   python main.py
