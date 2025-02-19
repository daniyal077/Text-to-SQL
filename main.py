import streamlit as st
import sqlite3
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def text_to_sql(user_query):
    sys_prompt = ChatPromptTemplate.from_template(
        """
        You are an expert in converting English questions to SQL queries.
        The SQL database is named STUDENT and contains the columns NAME, COURSE, SECTION, and MARKS.
        For example:
        - "How many records are present?" should yield: SELECT COUNT(*) FROM STUDENT;
        - "List all students studying Data Science" should yield: SELECT * FROM STUDENT WHERE COURSE="Data Science";
        **Only output the SQL command, without any additional text or formatting.**
        Now, convert this question to a valid SQL query: {user_query}
        """
    )

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama3-8b-8192"
    )

    chain = sys_prompt | llm | StrOutputParser()
    sql_query = chain.invoke({"user_query": user_query})

    return sql_query.strip()  


def get_data_from_database(sql_query):
    database = "student.db"
    with sqlite3.connect(database) as conn:
        return conn.execute(sql_query).fetchall()


def main():
    st.set_page_config(page_title="Text To SQL")
    st.header("Chat with Database")

    user_query = st.text_input("Enter your question:")
    submit = st.button("Generate SQL and Query DB")

    if submit:
        sql_query = text_to_sql(user_query)
        retrieved_data = get_data_from_database(sql_query)
        
        st.subheader(f"SQL Query: `{sql_query}`")
        if retrieved_data:
            st.header("Result")
            for row in retrieved_data:
                st.write(row)
        else:
            st.write("No results found.")

if __name__ == '__main__':
    main()
