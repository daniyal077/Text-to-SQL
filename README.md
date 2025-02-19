# Text-to-SQL App

This is a **Text-to-SQL** web application built with **Streamlit**. It allows users to ask natural language questions, which are then converted into **SQL queries** and executed on an SQLite database. The app uses **LangChain** and **Groq's Llama3 model** to generate SQL queries from user input.

## Features
- Converts English questions into SQL queries using **LangChain** and **Groq API**.
- Queries an SQLite database (`student.db`) based on the generated SQL.
- Displays the SQL query and the retrieved data in a **Streamlit** interface.

## Technologies Used
- **Python**
- **Streamlit** (for the frontend UI)
- **SQLite** (for database management)
- **LangChain** (for query generation)
- **Groq API** (Llama3 model for text-to-SQL conversion)
- **dotenv** (for managing API keys)

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/daniyal077/Text-to-SQL-.git
cd Text-to-SQL
```

### 2. Create a Virtual Environment and Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and add your **Groq API key**:
```bash
GROQ_API_KEY=your_api_key_here
```

### 4. Download Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the App
```bash
streamlit run app.py
```

## Usage
1. Open the web app in your browser.
2. Enter your question in natural language (e.g., *"List all students studying Data Science"*).
3. Click on the **Generate SQL and Query DB** button.
4. The app will display the **SQL query** and the corresponding **results** from the database.

### Input:
- **User interface**
- ![image](https://github.com/user-attachments/assets/758909ee-5b01-4c2b-a331-25c80f261f19)


### Output:
- **Query and generated output**
- ![image](https://github.com/user-attachments/assets/593a5e09-ead0-4071-ab35-3cad7b5a7411)


## Contributing
Feel free to fork this repository and submit **pull requests** for improvements!

