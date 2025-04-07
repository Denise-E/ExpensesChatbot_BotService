# ExpensesChatbot_BotService

ExpensesChatbot_BotService is a Python-based backend service responsible for analyzing and interpreting incoming Telegram messages to identify, extract, and classify expense data. It leverages a pipeline of lightweight local language models orchestrated via LangChain and executed through Ollama to determine whether a message is information about an expense, extract relevant details (such as amount and description), categorize the expense, and store the results in a PostgreSQL database. It serves as the core processing engine of the ExpensesChatbot system, communicating with the ConnectorService through a REST API.

### Related Repository

- [ExpensesChatbot_ConnectorService](https://github.com/Denise-E/ExpensesChatbot_ConnectorService): Handles Telegram interactions and forwards messages to this service for processing.

## ⚙️ Technologies Used

- **Flask**: Web framework used to expose the API and handle requests.
- **SQLAlchemy**: ORM to interact with the PostgreSQL database.
- **LangChain**: Framework used to build and orchestrate the local language models.
- **Pydantic**: Used for validating and parsing the models’ outputs.
- **Ollama**: Local LLM runner that allows you to use models like Mistral or LLaMA3 offline.
- **Flask-Swagger-UI**: Tool used to expose Swagger documentation via a simple route.

## Running the Project

### Clone the repository

### Prerequisites

Ensure you have [Python 3.11](https://www.python.org/downloads) or higher installed on your system.

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

DB_PASS=your_database_password
DB_CONNECTION_STR=postgresql://your_database_string

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

### 🚀 Run the Project

```bash
flask run
```

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

This endpoint registers a new Telegram user in the database using their unique telegram_id. If the user already exists, the request is ignored or handled accordingly.

**Request Body**:

```json
{
  "telegram_id": "1234567891",
}
```

**Response**:

```json
{
    "id": 1,
    "telegram_id": "1234567891"
}
```

#### 3. GET /api/expenses/<telegram_id>/all

This endpoint retrieves all the expenses associated with a given Telegram user. It expects the telegram_id as a path parameter and returns a list of all recorded expenses for that user.

**Response**:

```json
{
    "expenses": [
        {
            "added_at": "Thu, 03 Apr 2025 09:51:35 GMT",
            "amount": "$150.02",
            "category": "General",
            "description": "example",
            "id": 1,
            "user_id": 1
        },
  ]
}
```

If the user don't have any expense saved, the endpoint will return an empty list in the key "expenses".
