=== CUBIRDS - INSTRUÇÕES DE INSTALAÇÃO E EXECUÇÃO ===

Este é um jogo CuBirds implementado em Python com interface gráfica Tkinter.

PASSO A PASSO PARA EXECUTAR O JOGO:

1. Navegue até a pasta do projeto:
   cd cubirds

2. Crie um ambiente virtual:
   virtualenv venv

3. Ative o ambiente virtual:
   venv\Scripts\activate

4. Instale as dependências:
   pip install -r requirements.txt

5. Configure o jogo (gere o ID do jogo):
   cd config
   python generate_game_id.py
   cd ..

6. Execute o jogo:
   python cubirds.py