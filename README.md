# New Life Bank

## Aula 04/10/2021

### 1) Criar um repositório no GitHub com o nome ```new_life_bank```
* .gitignore
* LICENCE
* README.md

### 2) Abra seu Power Shell e faça um clone do repositório ```new_life_bank``` em seu ambiente CITRIX.
```
git clone https://github.com/<your name>/new_life_bank.git
```
### 3) Entre no diretório:
```
cd new_life_bank
```
### 4) Abra o vscode através do terminal.
```
code .
```
### 5) Habilite o terminal no modo Git Bash. <br/><br/>

### 6) No terminal do vscode verifique a versão do Python
```
python --version
```
### 7) Instalar o ambiente virtual
```
pip3 install virtualenv
```
### 8) Verifique a versão do virtualenv
```
virtualenv --version
```
### 9) Crie um ambiente virtual
```
python -m virtualenv venv
```
### 10) Ativar o ambiente virtual
```
source venv/Scripts/activate
```
```(venv)  ```

### 11) Verificando as bibliotecas instaladas.
```
pip3 freeze
```
### 12) Bibliotecas built-in. No interpretador do Python:
```python```
```
>> import datetime
```
### 13) Instalando as bibliotecas:
```
pip3 install fastapi uvicorn
```
### 14) Verifique as bibliotecas instaladas.
```
pip3 freeze
```
### 15) Arquivo requirements:
```
pip3 freeze >> requirements.txt
```
### 16) Escrever o primeiro servidor. <br/><br/>

### 17) Para rodar o servidor:
```
uvicorn main:app --reload
```
### 18) Para realizar uma consulta no servidor:
* browser (http://127.0.0.1:8000/) 
* browser (http://127.0.0.1:8000/health/)
* browser (http://127.0.0.1:8000/docs/)
* curl 127.0.0.1:8000/health
* postman







