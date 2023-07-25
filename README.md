# API de Tarefas - Unibalsas 

[![Status](https://img.shields.io/badge/status-on-brightgreen)](https://api-ub.pedroplayborges.repl.co)
[![GitHub license](https://img.shields.io/github/license/piedro404/cpf-validation-api)](https://github.com/piedro404/ub-task-api/blob/main/LICENSE)

Esta é uma API de busca de tarefa na UB Virtual, plataforma da faculdade onde é postada as atividades. Ela permite que você recupere e se mantenha atualizada as atividades do portal, além de outros pontos como dados dos usuários e cursos. Hospedada provisoriamente para testes em [https://api-ub.pedroplayborges.repl.co](https://api-ub.pedroplayborges.repl.co).

OBS: Foi feito usando FASTAPI e Webdriver, pelo fato de não ter acesso ao banco de dados, podendo ocasionar erros. A aplicação teste também pode cair a qualquer momento, pelo fato de ser provisoria

### Tarefas
![2023-07-25_18h44_55](https://github.com/piedro404/ub-task-api/assets/88720549/f3f03d18-f666-4aad-8d8b-c0e44ac109fe)
![2023-07-25_18h41_42](https://github.com/piedro404/ub-task-api/assets/88720549/ce3beaef-2208-42da-9129-adc527d6986e)

### Perfil
![2023-07-25_18h40_30](https://github.com/piedro404/ub-task-api/assets/88720549/b16e6162-e086-45aa-8e42-72f13029fa2b)

### Cursos
![2023-07-25_18h42_34](https://github.com/piedro404/ub-task-api/assets/88720549/e0833c94-4832-4bde-b1d7-ea6e4a7b8688)

## Recursos
- Tarefas: Verifica se há tarefas e as retornas, como nome da matéria e da atividade, data de entrega e link da atividade.
- Perfil: Verifica o perfil e retorna os dados visíveis do usuário, como nome e até e-mail.
- Cursos: Verifica os cursos que esta sendo realizado e retorna-as.

[UNIBALSAS](https://www.unibalsas.edu.br/)

A aplicação funciona assim:
Quando receber a solicitação URL com tal função, ela executa o WEBDRIVER junto do SELENIUM que busca as tags XPATH dos dados que tal função precisa e as retorna-os em formato JSON 

## Documentação

Acesse a [documentação da API](https://api-ub.pedroplayborges.repl.co/docs) para obter informações detalhadas sobre os endpoints, parâmetros e testes de requisições.

### Como usar
1. Rota principal ("/"): Retorna um JSON com uma descrição da API. <br>(https://api-ub.pedroplayborges.repl.co/)

```bash
{
  "Status": true,
  "Description": "API UB ON!",
  "Version": "2.0v"
}
```
2. Rota de Tarefas ("/ub/atv/{log}&{ps}"): Recebe a matricula(log) e senha(ps) e retorna um JSON com o resultado da pesquisa das tarefas. <br>(https://api-ub.pedroplayborges.repl.co/ub/atv/{log}&{ps})

```bash
{
  "status": true,
  "atv": false,
  "description": "Não tem atividade pendentes!",
  "qtd": 0,
  "list": null
}
```
3. Rota de Perfil ("/ub/perfil/{log}&{ps}"): Recebe a matricula(log) e senha(ps) e retorna um JSON com o resultado da pesquisa do perfil. <br>(https://api-ub.pedroplayborges.repl.co/ub/perfil/{log}&{ps})

```bash
{
  "status": true,
  "name": "PEDRO HENRIQUE MARTINS BORGES",
  "email": "pedro.borges@alu.unibalsas.edu.br",
  "cidade": "São Raimundo das Mangabeiras",
  "fuso_horario": "America/Araguaina"
}
```
4. Rota de Perfil ("/ub/mat/{log}&{ps}"): Recebe a matricula(log) e senha(ps) e retorna um JSON com o resultado da pesquisa do perfil. <br>(https://api-ub.pedroplayborges.repl.co/ub/mat/{log}&{ps})

```bash
{
  "status": true,
  "mat": true,
  "description": "Há 5 curso(s)!",
  "qtd": 5,
  "list": [
    {
      "name": "SER HUMANO, CULTURA E SOCIEDADE - SI",
      "link": "https://digital.unibalsas.edu.br/course/view.php?id=869"
    },
    {
      "name": "ALGORITMOS E PROGRAMAÇÃO AVANÇADA",
      "link": "https://digital.unibalsas.edu.br/course/view.php?id=870"
    },
    {
      "name": "SISTEMAS OPERACIONAIS",
      "link": "https://digital.unibalsas.edu.br/course/view.php?id=858"
    },
    {
      "name": "INOVAÇÃO E NEGÓCIOS COM SISTEMAS DE INFORMAÇÃO",
      "link": "https://digital.unibalsas.edu.br/course/view.php?id=855"
    },
    {
      "name": "LABORATÓRIO DE BANCO DE DADOS",
      "link": "https://digital.unibalsas.edu.br/course/view.php?id=856"
    }
  ]
}
```

## Instalação
### Pré-requisitos

Certifique-se de ter o Python 3 instalado. Você também pode criar um ambiente virtual para isolar as dependências do projeto.

1. Clone este repositório:
   
   ```bash
   git clone https://github.com/piedro404/ub-task-api.git
   ```
2. Instale as dependências:
   
   ```bash
   pip install -r requirements.txt
   ```

### Executando a API

1. Execute o seguinte comando para iniciar a API:

   ```bash
   python main.py
   ```
2. A API será executada localmente em http://localhost:8000.

## Licença
Este projeto está licenciado sob a Licença MIT. Por favor, inclua a seguinte referência no seu trabalho derivado:
<br>
- API de Tarefas - Unibalsas - desenvolvida por [Piedro404](https://github.com/piedro404) sob a Licença MIT.


Obrigado a todos, desejo otimos estudos, caso queira, entre em contato em pedro.henrique.martins404@gmail.com.
