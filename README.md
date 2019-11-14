# App "TODO List" em python/flask, jQuery e SQLite

As interações com as tarefas são feitas via javascript para não renderizar uma página nova a cada request/atualização das tarefas.

Instalação:

- Clone ou baixe o repositório do projeto para sua máquina
- Instale o virtualenv
    - `$ sudo apt install virtualenv`
- No diretório raiz do projeto, crie um ambiente virtual
    - `$ virtualenv -p python3.6 venv`
- Ative o ambiente virtual venv
    - `$ source venv/bin/activate`
- Instale as dependências do projeto
    - `$ pip install -r requirements-dev.txt`
- Inicialize as migrações para o banco de dados
    - `$ python manage.py db init`
- Migre as alterações para o banco de dados
    - `$ python manage.py db migrate`
    - `$ python manage.py db upgrade`
- Execute o servidor de teste
    - `$ python manage.py runserver`
- Teste a aplicação abrindo o link abaixo no seu navegador
    - http://127.0.0.1:5000/todolist

Deploy da APP em AWS: http://3.86.142.40:8080/todolist

Contato:  
clebiano@alumni.usp.br