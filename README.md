# 🏢 API de Empresas - FastAPI + PostgreSQL

API desenvolvida em **FastAPI** para **gerenciamento de empresas**, permitindo cadastrar, listar, filtrar e buscar informações com validação de duplicidade (CNPJ e e-mail).  
O projeto utiliza **SQLAlchemy** para ORM e **PostgreSQL** como banco de dados.

---

## 🚀 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [PostgreSQL](https://www.postgresql.org/)

---

## 📦 Funcionalidades da API

✅ Cadastrar uma nova empresa  
✅ Listar todas as empresas  
✅ Filtrar empresas por **cidade**, **ramo de atuação** e **nome**  
✅ Verificar duplicidade de **CNPJ** e **e-mail**  
✅ Retornar mensagens de erro apropriadas  

---

<h2>🛠️ Como Rodar o Projeto Localmente</h2>

<p>Siga os passos abaixo para executar a API na sua máquina 👇</p>

<h3>1️⃣ Clonar o repositório</h3>
<pre><code>git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
</code></pre>

<h3>2️⃣ Criar e ativar um ambiente virtual</h3>
<pre><code>python -m venv venv
</code></pre>
<p><strong>Ativar:</strong><br>
Windows: <code>venv\Scripts\activate</code><br>
Linux/macOS: <code>source venv/bin/activate</code>
</p>

<h3>3️⃣ Instalar as dependências</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>4️⃣ Configurar o banco de dados PostgreSQL</h3>
<p>Crie um banco no PostgreSQL (ex: <code>empresas_db</code>) e atualize o arquivo <code>config/db.py</code> com suas credenciais:</p>

<pre><code>SQLALCHEMY_DATABASE_URL = "postgresql://usuario:senha@localhost/empresas_db"
</code></pre>

<h3>5️⃣ Executar as migrações (se houver)</h3>
<pre><code>alembic upgrade head
</code></pre>

<h3>6️⃣ Rodar o servidor FastAPI</h3>
<pre><code>uvicorn main:app --reload
</code></pre>

<p>A API ficará disponível em:<br>
👉 <strong>http://127.0.0.1:8000</strong></p>

<h3>7️⃣ Testar no navegador ou Postman</h3>
<p>Você pode acessar a documentação automática:</p>
<ul>
  <li><strong>Swagger UI:</strong> <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a></li>
  <li><strong>Redoc:</strong> <a href="http://127.0.0.1:8000/redoc">http://127.0.0.1:8000/redoc</a></li>
</ul>

