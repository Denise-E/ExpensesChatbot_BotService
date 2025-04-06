# ExpensesChatbot_BotService
This service is tasked with the analysis of incoming messages to identify and extract expense details before persisting these details into the database.

ExpensesChatbot_BotService is responsible for analyzing incoming messages to identify and extract expense details, which are then stored in a database.

It leverages a series of three lightweight AI models running locally through Ollama, built using LangChain and validated using Pydantic. The application is implemented in Python with Flask and integrates with a PostgreSQL database via SQLAlchemy.

## ⚙️ Technologies Used

- **Flask**: Web framework used to expose the API and handle requests.
- **SQLAlchemy**: ORM to interact with the PostgreSQL database.
- **LangChain**: Framework used to build and orchestrate the local language models.
- **Pydantic**: Used for validating and parsing the models’ outputs.
- **Ollama**: Local LLM runner that allows you to use models like Mistral or LLaMA3 offline.
- **Flask-Swagger-UI**: Tool used to expose Swagger documentation via a simple route.

## Running the Project

### Clone the repository

### 🐍 Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate  # On Windows
```

### 💾 Install Dependencies

```bash
pip install -r requirements.txt
```

### LLM Ollama
You will also need to download Ollama from the official website https://ollama.com/download.

Once downloaded, yo will need to install de models used in the proyect with the following commands

```bash
ollama run llama3
ollama run mistral
```

### .env Variables
Create a .env file in the root directory with the following content:

DB_PASS
DB_CONNECTION_STR=postgresql://<your_database_string>

### 🔑 Database Setup

The database must be created manually using the provided SQL scripts.

CREATE TABLE users (
"id" SERIAL PRIMARY KEY,
"telegram_id" text UNIQUE NOT NULL
);

CREATE TABLE expenses (
"id" SERIAL PRIMARY KEY,
"user_id" integer NOT NULL REFERENCES users("id"),
"description" text NOT NULL,
"amount" money NOT NULL,
"category" text NOT NULL,
"added_at" timestamp NOT NULL
);


### 📨 Endpoints

The project contains three endpoints:

#### 1. POST /api/expenses/create

This endpoint analyzes a user message to determine if it refers to an expense. If so, it extracts the amount and description, classifies the expense into one of the predefined categories, and stores it in the database.

**Request Body**:

```json
{
  "telegram_id": "123456",
  "text": "I spent 80 bucks on groceries"
}
```

**Response**:

```json
{
  "user_id": 1,
  "description": "Groceries",
  "amount": 80.0,
  "category": "Food",
  "added_at": "2025-04-04T12:34:56"
}
```

#### 2. POST /api/users/create

#### 3. POST /api/expenses/get/all


