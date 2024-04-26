# API de Tarefas - Unibalsas 📒

[![Status](https://img.shields.io/badge/status-on-brightgreen)](https://ub-task-api.vercel.app/)

Esta é uma API de busca de tarefa na UB Virtual, plataforma da faculdade onde é postada as atividades. Ela permite que você recupere e se mantenha atualizada as atividades do portal, além de outros pontos como dados dos usuários e cursos. Hospedada provisoriamente para outros projetos em [https://ub-task-api.vercel.app/](https://ub-task-api.vercel.app/).

##### Projeto Reestruturado e Escalavel. 😎📱

### Swagger 📑
<img width="930" alt="2024-02-25_12h12_11" src="https://github.com/piedro404/ub-task-api/assets/88720549/2fd5279c-5c4b-4c44-a178-25f9f5d63533">

### Perfil 🙍
<img width="876" alt="2024-02-28_13h55_14" src="https://github.com/piedro404/ub-task-api/assets/88720549/5819b873-ff1f-474c-b9bd-5bf23a4d7b9c">

### Tarefas 📚
<img width="876" alt="2024-02-25_12h33_15" src="https://github.com/piedro404/ub-task-api/assets/88720549/88f70993-31d0-4855-97f9-6d6a8b78b2f9">

# Recursos da API 🔨
- Home: Dá as suas Boas-Vindas e traz informações relevantes sobre a API e Contatos.
- Docs: Local para aprender sobre a API e como utilizar de forma interativa e dinâmica.
- Task: Verifica se há tarefas e as retornas, como nome da matéria e da atividade, data de entrega e link da atividade.
- Profile: Verifica o perfil e retorna os dados visíveis do usuário, como nome e até e-mail.

#### Site Universitario para apresentação da instituição [Unibalsas](https://www.unibalsas.edu.br/)
<img width="930" alt="2024-02-25_12h38_47" src="https://github.com/piedro404/ub-task-api/assets/88720549/b1f23a17-0099-43de-9c58-b0c2ea81f7bb">

# Principais Tecnologias Utilizadas 🌐
- Flask: Framework utilizado para o desenvolvimento de aplicações web, proporcionando uma estrutura flexível e eficiente para a criação de APIs e interfaces de usuário.
- Python: Linguagem de programação principal, escolhida pela sua versatilidade, simplicidade e vasta comunidade de desenvolvedores.
- Request: Biblioteca utilizada para realizar requisições HTTP, facilitando a comunicação com APIs externas e a obtenção de dados online.
- BS4: Beautiful Soup, uma biblioteca em Python utilizada para fazer web scraping, permitindo a extração de informações de páginas HTML e XML de forma fácil e intuitiva.
- Cerberus: Biblioteca de validação de dados em Python, empregada para garantir a integridade e consistência dos dados manipulados pela aplicação.
- Outras Bibliotecas: O resto das bibliotecas pode ser encontradas no requirements.txt, incluindo diversas ferramentas e utilitários que complementam e aprimoram as funcionalidades da aplicação.

# Documentação 📃

Acesse a [documentação da API](https://ub-task-api.vercel.app/docs) para obter informações detalhadas sobre os endpoints, parâmetros e testes de requisições.

A aplicação funciona assim:
Quando a API receber uma solicitação URL com tal função, seja por GET ou POST, ela executa as funções conforme a rota pre-estabelecida, realiza o login e realiza uma busca a estrutura do site bruta, retornando uma resposta em formato JSON. 

## Como usar 💁‍♀️
1. Rota principal ("/"): Retorna um JSON com informações sobre a API. <br>(https://ub-task-api.vercel.app)

```bash
{
  "contact": {
    "email_personal": "pedro.henrique.martins404@gmail.com",
    "email_academic": "pedro.borges@alu.unibalsas.edu.br",
    "github": "piedro404",
    "linkedin": "pedrohenrique404"
  },
  "documentation": "/docs",
  "endpoints": {
    "home": "/",
    "ub": {
      "ub_profile": "/ub/profile",
      "ub_task": "/ub/task"
    }
  },
  "message": "Welcome to the UB API!",
  "status": true,
  "version": "3.0v"
}
```
2. Rota de Tarefas ("/ub/task"): Recebe a matricula/email(login) e senha(password) que deverá se enviada no body de uma requisição por POST e retorna um JSON com o resultado da pesquisa das tarefas. <br>(https://ub-task-api.vercel.app/ub/task)

```bash
{
  "status": true,
  "tasks": {
    "amount_task": 1,
    "description": "Há 1 atividade(s) pendente(s)!",
    "find_task": true,
    "list_tasks": [
      {
        "date": "6 março",
        "day_week": "quarta-feira",
        "matter": "LABORATÓRIO DE SISTEMAS OPERACIONAIS",
        "task_name": "Atividade - Mapa Conceitual sobre Sistemas de Arquivos (até 06/03) está marcado(a) para esta data",
        "time_limit": "18:59 PM",
        "url_task": "https://ead.unibalsas.edu.br/mod/assign/view.php?id=16236"
      }
    ]
  }
}
```
3. Rota de Perfil ("/ub/profile/"): Recebe a matricula/email(login) e senha(password) que deverá se enviada no body de uma requisição por POST e retorna um JSON com o resultado da pesquisa do perfil. <br>(https://ub-task-api.vercel.app/ub/profile)

```bash
{
  "profile": {
    "email": "augustomatheus233@gmail.com",
    "language": "português",
    "name": "Matheus Augusto Silva Dos Santos",
    "user_initials": "MA",
    "user_picture": "https://ead.unibalsas.edu.br/user/pix.php/2228/f1.jpg"
  },
  "status": true
}
```

#### Todas as resposta acima são de Status Code de 200. Veja a Documentação para poder capturar outros Status Codes como 400, 401, 422 e 500.

# Como Executar o Projeto Localmente 🛠️
1. Clone este repositório:
   
```bash
   git clone https://github.com/piedro404/ub-task-api.git
```

2. Ambiente Virtualizado (Opcional)
Para organização e facilitar em rodar o projeto, sugiro criar um ambiente virtualizado. Para isso, basta usar o comando abaixo:
```Bash
  python -m venv .venv
```
```Bash
  .venv\Scripts\activate
```

3. Instale as dependências: 

```bash
   pip install -r requirements.txt
```
   
4. Execute a aplicação: 

```bash
   python run.py
```

# Sobre 📒
Obrigado a todos, desejo ótimos estudos, caso queira, entre em contato em pedro.henrique.martins404@gmail.com;
