import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
import random
import sqlparse

# Load .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Functions

def generate_sql_query(natural_language_query, database=None, schema_info=None):
    """Generates an SQL query and explanation based on the natural language query."""
    prompt = f"Convert this request into a SQL query: '{natural_language_query}'"
    if schema_info:
        prompt += f" based on the database schema: {schema_info}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    full_response = response.choices[0].message.content

    # Separate explanation and SQL query
    explanation, sql_query = full_response.rsplit('SQL Query:', 1) if 'SQL Query:' in full_response else (full_response, "")
    return explanation.strip(), sql_query.strip()


def get_random_example():
    """Returns a random example query."""
    examples = [
        "Show all employees from the 'employees' table.",
        "Find the total sales for each month.",
        "List all products with a price greater than $50.",
        "Get the number of orders placed in the last 30 days.",
        "Retrieve the top 5 customers by total spend."
    ]
    return random.choice(examples)


def handle_query_submission():
    """Handles the submission of a natural language query, generating the SQL and displaying the result."""
    
    # Ensure the Answer header is shown first
    st.write("")  # Adding a blank line for spacing
    st.header("Answer", divider="blue")

    if st.session_state.query_input:
        with st.spinner("Generating SQL query..."):
            try:
                explanation, sql_query = generate_sql_query(
                    st.session_state.query_input, database=None, schema_info=st.session_state.get("schema_input", None)
                )

                # Display SQL query first
                if sql_query:
                    st.subheader("Generated SQL Query:")
                    st.code(sqlparse.format(sql_query, reindent=True, keyword_case='upper'), language='sql')
                
                # Display the explanation
                if explanation:
                    st.markdown(f"{explanation}")
            except Exception as e:
                st.error(f"Error generating SQL: {str(e)}")
    else:
        st.warning("⚠️ Please enter a query.")


# Streamlit Layout

# Check if the session state for the query is initialized
if 'query_input' not in st.session_state:
    st.session_state.query_input = ""

# Check if the example query button was clicked before rendering the widget
if st.session_state.get('example_clicked', False):
    st.session_state.query_input = get_random_example()
    st.session_state.example_clicked = False

# Page configuration
st.set_page_config(page_title="Text to SQL", layout="centered", page_icon="🗃️", initial_sidebar_state="expanded")

# Sidebar content

# SQL Server toggle and connection inputs
sql_toggle = st.sidebar.toggle("Connect SQL Server")
if sql_toggle:
    server = st.sidebar.text_input("Server")
    database = st.sidebar.text_input("Database")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

st.sidebar.title("About :material/info:")
st.sidebar.markdown("""
`Text to SQL` is a tool to convert natural language into SQL queries using AI.

:blue-background[Quick Use:]
1. Type your query 💬
2. Paste your schema 📑 (optional)
3. Click Generate :gear:.

:blue-background[Tools & Skills:]
- `OpenAI:` GPT-4 Model for query conversion.
- `Schema Support:` Input your database schema for precision.
- `Streamlit:` Interactive UI and SQL code generation.
- `Python:` Backend logic with libraries like `sqlparse`.

---
_https://github.com/marvinhalabi_
""")


# Main layout
st.title("Text to SQL 🗃️")
st.subheader("*Convert your question into a SQL query*", divider="blue")

# Input field for natural language query
col1, col2 = st.columns([5, 1])
with col1:
    query = st.text_input(
        label="Enter a question", label_visibility="collapsed",
        value=st.session_state.query_input, placeholder="Type here...", key="query_input"
    )

with col2:
    # The button now fills the input, but does not submit the query
    if st.button(label=":material/autorenew:", key="example_button", help="Use an Example", type="primary"):
        st.session_state.example_clicked = True
        st.rerun()  # Reruns the app to update the input

# Optional input for database schema
with st.expander("Database schema"):
    schema_info = st.text_area(
        label="Schema", label_visibility="collapsed", 
        placeholder="Paste your schema here...", key="schema_input"
    )

# Generate SQL button
if st.button("Generate :gear:", type="secondary", help="Submit"):
    handle_query_submission()

# Show SQL output after generating
if st.session_state.query_input:
    handle_query_submission()
