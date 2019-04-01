# Desafio Guiabolso - Deploy Events API

Esse projeto é focado na resolução do desafio proposto para o Guiabolso para realizar o cadastro de determinados "eventos" que correspondem à execuções de deploys.

## Vamos começar!

As instruções à baixo irão mostrar como realizar a instalação de depêndencias e a execução da aplicação.

### **Pré-requisitos e instalação**

É necessário possuir docker e docker-compose instalados. [docker](https://docs.docker.com/v17.12/install/) [docker-compose](https://docs.docker.com/compose/install/)

Será necessário clonar o repositório para o seu ambiente, escolha a pasta de sua preferência:
```
git clone https://github.com/mathv96/desafio_guiabolso.git
```

### **Configurações**

Passando pelos requisitos necessários, vamos às configurações.

- Caso queira, pode alterar algumas váriaveis com relação à base de dados no arquivo *conf.env*.

- Além disso, nas configurações atuais, o docker-compose sobe a aplicação somente local, não escutando requisições externas, mas pode ser modificado facilmente. [info](https://docs.docker.com/compose/extends/#example-use-case)

### **Execução**

Execute o docker-compose na raiz do projeto, para subir a aplicação e o banco de dados com o seguinte comando:
```
docker-compose up -d
```

## **Testando a aplicação**

1) Verificando se a API está funcionando:
```
curl http://localhost:5000
```
Resposta esperada:
```
{
  "result": "API is working."
}
```

2) Realizando a inserção de um eventos:
```
curl -H "Content-Type: application/json" -X POST -d '{"component":"teste", "version":"0.5", "responsible":"Jhon", "status":"okay"}' http://localhost:5000/insert_event
```
Resposta esperada:
```
{
  "result": "Event saved."
}
```

3) Consulta dos eventos cadastrados: (traz todos os dados já cadastrados)
```
curl http://localhost:5000/list_events
```
Resposta esperada:
```
{
  "result": [
        {
        "component": "teste", 
        "date": "2018-09-30 03:58:01", 
        "id": "1", 
        "responsible": "Jhon", 
        "status": "okay",
        "version": "0,5"
        }
    ]
}
```

## **Feito com...**

* [Python](https://www.python.org/doc/) - The language used
* [Flask](http://flask.pocoo.org/docs/1.0/) - The framework used
* [Docker](https://docs.docker.com/) - The container manager used
* [Virtualenv](https://virtualenv.pypa.io/en/stable/) - The virtual enviroment to test the application

## **Autores**

* **Matheus Martins** 


