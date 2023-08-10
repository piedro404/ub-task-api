# API de Tarefas - Unibalsas 

[![Status](https://img.shields.io/badge/status-on-brightgreen)](https://api-ub.pedroplayborges.repl.co)

Esta é uma API de busca de tarefa na UB Virtual, plataforma da faculdade onde é postada as atividades. Ela permite que você recupere e se mantenha atualizada as atividades do portal, além de outros pontos como dados dos usuários e cursos. Hospedada provisoriamente para testes em [https://api-ub.pedroplayborges.repl.co](https://api-ub.pedroplayborges.repl.co).

OBS: Foi feito usando FASTAPI e Webdriver, pelo fato de não ter acesso ao banco de dados, podendo ocasionar erros. A aplicação teste também pode cair a qualquer momento, pelo fato de ser provisoria

![2023-08-10_10h04_27](https://github.com/piedro404/ub-task-api/assets/88720549/74004a25-6ec8-458d-84ea-f83b04ccb33b)

### Tarefas
![2023-08-10_01h19_34](https://github.com/piedro404/ub-task-api/assets/88720549/96ec8d1d-7e26-4ac5-8d4f-e66296fddb16)

### Perfil
![2023-08-10_01h20_07](https://github.com/piedro404/ub-task-api/assets/88720549/b0ba6187-1b07-4da1-9421-a0a315753a56)

### Cursos
![2023-08-10_01h20_28](https://github.com/piedro404/ub-task-api/assets/88720549/ef1f9596-b79d-4369-89b2-26e70f583651)

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
  "Version": "2.5v"
}
```
2. Rota de Tarefas ("/ub/atv/{log}&{ps}"): Recebe a matricula(log) e senha(ps) e retorna um JSON com o resultado da pesquisa das tarefas. <br>(https://api-ub.pedroplayborges.repl.co/ub/atv/{log}&{ps})

```bash
{
  "status": true,
  "atv": true,
  "description": "Há 1 atividade(s) pendente(s)!",
  "qtd": 1,
  "list": [
    {
      "mat": "ANÁLISE E ENGENHARIA DE SISTEMAS",
      "name": "Trabalho escrito: instruções sobre pesquisa acadêmica. está marcado(a) para esta data",
      "day_week": "segunda-feira",
      "date": "14 agosto",
      "time_limit": "00:00  AM",
      "link_atv": "https://ead.unibalsas.edu.br/mod/assign/view.php?id=8601"
    }
  ]
}
```
3. Rota de Perfil ("/ub/perfil/{log}&{ps}"): Recebe a matricula(log) e senha(ps) e retorna um JSON com o resultado da pesquisa do perfil. <br>(https://api-ub.pedroplayborges.repl.co/ub/perfil/{log}&{ps})

```bash
{
  "status": true,
  "name": "PEDRO HENRIQUE MARTINS BORGES",
  "email": "pedro.borges@alu.unibalsas.edu.br",
  "language": "português"
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
      "name": "ANÁLISE E ENGENHARIA DE SISTEMAS",
      "link": "https://ead.unibalsas.edu.br/course/view.php?id=2055"
    },
    {
      "name": "EMPREENDEDORISMO",
      "link": "https://ead.unibalsas.edu.br/course/view.php?id=2335"
    },
    {
      "name": "LABORATÓRIO DE REDES E AUTOMAÇÃO",
      "link": "https://ead.unibalsas.edu.br/course/view.php?id=2353"
    },
    {
      "name": "PARADIGMAS DE PROGRAMAÇÃO E INTERFACES",
      "link": "https://ead.unibalsas.edu.br/course/view.php?id=2355"
    },
    {
      "name": "REDES DE COMPUTADORES",
      "link": "https://ead.unibalsas.edu.br/course/view.php?id=2336"
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

## Sobre
Obrigado a todos, desejo otimos estudos, caso queira, entre em contato em pedro.henrique.martins404@gmail.com.
