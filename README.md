# New Life Bank

## Aula 11/10/2021

### 1) Abra o vscode através do terminal e acesse a pasta new_life_bank.
```
code .
```
### 2) Habilite o terminal no modo Git Bash. <br/><br/>

### 3) Ativar o ambiente virtual
```
source venv/Scripts/activate
```
```(venv)  ```

### 4) Para rodar o servidor no terminal
```
python main.py
```

### 5) Realizar testes no servidor:
* browser (http://127.0.0.1:8000/)
* browser (http://127.0.0.1:8000/docs/)
* browser (http://127.0.0.1:8000/health/)
* curl 127.0.0.1:8000/health
### O que aparece  no / ?
* [GET]   thunder-client (http://127.0.0.1:8000/)
### Realizar testes no /health
* [GET]   thunder-client (http://127.0.0.1:8000/health)
### Buscar todas contas cadastradas:
* [GET]   thunder-client (http://127.0.0.1:8000/accounts)
### Realizar testes com diferentes IDs:
* [GET]   thunder-client (http://127.0.0.1:8000/accounts/{id})
### Realizar testes com diferentes CPFs:
* [GET]   thunder-client (http://127.0.0.1:8000/accounts/{cpf})
### Adicionar uma nova conta:
* [POST]  thunder-client (http://127.0.0.1:8000/accounts/)
