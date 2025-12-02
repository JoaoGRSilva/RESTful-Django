# 📝 Django BlogPost REST API

Uma API REST simples desenvolvida com **Django** e **Django REST Framework**, conectada a um banco de dados **MySQL** para persistência dos dados.  
O projeto permite criar, listar, atualizar, deletar e buscar posts usando endpoints RESTful.
Projeto inspirado no __roadmap__: https://roadmap.sh/projects/blogging-platform-api

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Django 5**
- **Django REST Framework**
- **MySQL 8+**
- **mysqlclient** (driver Python ↔ MySQL)
- **DBeaver** (opcional: visualização das tabelas)

---

## 🗃 Banco de Dados — MySQL

Este projeto utiliza **MySQL** como banco de dados principal.

A conexão é configurada no `settings.py` usando:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_api',
        'USER': 'root',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}
```
__Dependência necessária:__
Instale o driver:
```bash
pip install mysqlclient
```
__Por que MySQL?__
- Melhor escalabilidade que SQLite
- Suporte a múltiplas conexões simultâneas
- Ótimo para APIs reais em produção
- Fácil integração com ferramentas como DBeaver, Workbench e Adminer

## Modelo de Dados (BlogPost)

A API trabalha com o modelo BlogPost, contendo:
| Campo         | Tipo        | Descrição                     |
| ------------- | ----------- | ----------------------------- |
| id            | Integer PK  | Identificador único           |
| post_title    | CharField   | Título do post                |
| post_content  | CharField   | Conteúdo                      |
| post_category | ChoiceField | Categoria (Tech, Cook, Music) |
| post_tag      | ChoiceField | Tag relacionada               |
| created_at    | DateTime    | Gerado automaticamente        |
| updated_at    | DateTime    | Atualizado automaticamente    |

O Django traduz automaticamente este modelo em uma tabela MySQL via **migrations**.

## 📡 Endpoints da API
__🔍 API Overview__

`GET /api/`

Retorna um dicionário com todas as rotas disponíveis.

__📌 Listar posts__

`GET /api/all/`

Retorna todos os posts ou filtra via query params:

__🔎 Buscar post por ID__

`GET /api/posts/<pk>/`

**➕ Criar post**

`POST /api/posts/`

Body JSON:
```json
{
  "post_title": "Meu primeiro post",
  "post_content": "Conteúdo do post",
  "post_category": "Tech",
  "post_tag": "Programming"
}
```
**✏ Atualizar post**

`PUT /api/posts/<pk>/`

**🗑 Deletar post**

`DELETE /api/posts/<pk>/`

## 📄 Licença

**MIT © 2025**
