# CRUD de uma API que calcula o melhor troco

Django e MongoDB

## Instalação:

- Clone ou baixe o repositório do projeto para sua máquina
- Instale o virtualenv
    - `$ sudo apt install virtualenv`
- No diretório raiz do projeto, crie um ambiente virtual
    - `$ virtualenv -p python3.6 venv`
- Ative o ambiente virtual venv
    - `$ source venv/bin/activate`
- Instale as dependências do projeto
    - `$ pip install -r requirements-dev.txt`
- Execute o servidor de teste
    - `$ python manage.py runserver`
- Teste a aplicação abrindo o link abaixo no seu navegador
    - http://127.0.0.1:8000/api/v1.0/payments/

## Funcionalidades

- Home da API: api/v1.0/payments/  
Nesta página são listados todos os registros de pagamentos no banco de dados. Cada registro de pagamento contém um identificador único (id), valor a ser pago (amount), valor efetivamente pago pelo cliente (amount_paid), troco (change), data e horário de inserção do registro (create_date) e a data e horário da última atualização (update_date). O melhor troco (best_change), com o menor número de cédulas, é calculado dinamicamente a partir das informações salvas no banco.  
Em "best_change" as chaves são o tipo de cédula e o valor é a quantidade ideal desta para obter o troco com o menor número de cédulas.

Exemplo de um registro:

    {
        "id": 2,
        "amount": "12.25",
        "amount_paid": "111.00",
        "change": 98.75,
        "best_change": [
            {
                "R$_50": 1
            },
            {
                "R$_10": 4
            },
            {
                "R$_5": 1
            },
            {
                "R$_1": 3
            },
            {
                "R$_0.5": 1
            },
            {
                "R$_0.1": 2
            },
            {
                "R$_0.01": 4
            }
        ],
        "create_date": "2019-11-14T08:51:02.064000Z",
        "update_date": "2019-11-14T13:27:46.990000Z"
    },

Além da listagem dos registros é possível adicionar um novo registro de pagamento via POST.

- As operações de exclusão e atualização podem ser realizadas em api/v1.0/payments/<id_registro>/


Contato:  
clebiano@alumni.usp.br