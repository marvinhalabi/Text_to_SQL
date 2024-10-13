Here's the `README.md` content formatted for easy copy-pasting:

```markdown
# Text to SQL 🗃️

`Text to SQL` is a Streamlit app that converts natural language queries into SQL queries using OpenAI's GPT-4 model. The app provides an interactive interface for users to input their questions, and it returns both the SQL code and an explanation of the query. Additionally, users can input database schema information for more accurate SQL generation.

---

## Features 🚀

- **Natural Language to SQL**: Convert plain text queries into SQL.
- **Schema Support**: Optionally input your database schema for more precise SQL generation.
- **Random Example Queries**: Get random example queries to test the functionality.
- **SQL Server Toggle**: Connect to a SQL server to execute queries directly.

---

## Quick Start 💻

### 1. Clone the Repository
```bash
git clone https://github.com/marvinhalabi/text_to_SQL.git
cd text_to_SQL
```

### 2. Set Up the Environment
Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## How It Works ⚙️

- **Input Your Query**: Enter a question in plain language, like "Show all employees from the 'employees' table."
- **Optional Schema**: Paste your database schema for more accurate SQL generation.
- **SQL Generation**: The app generates an SQL query using OpenAI's GPT-4 model and returns the result in SQL format.

---

## Example Queries 📄

Here are some example queries that you can try:
- "Show all employees from the 'employees' table."
- "Find the total sales for each month."
- "List all products with a price greater than $50."
- "Get the number of orders placed in the last 30 days."
- "Retrieve the top 5 customers by total spend."

---

## Tools & Skills 🛠️

- **OpenAI**: GPT-4 Model for natural language to SQL conversion.
- **Python**: Backend logic using libraries like `sqlparse`.
- **Streamlit**: Provides an interactive UI for the app.
- **Environment Management**: Use `.env` to securely store API keys.

---

## Contributing 🤝

Feel free to contribute to the project by submitting a pull request or opening an issue. All contributions are welcome!

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

_Made with ❤️ by [Marvin Halabi](https://github.com/marvinhalabi)_
```

You can copy and paste this into your `README.md` file. Let me know if you need any further adjustments!
