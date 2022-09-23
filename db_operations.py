import psycopg2
import pandas as pd
import os

host = os.environ['host']
user = os.environ['user']
password = os.environ['password']
db_name = os.environ['db_name']

def run_syntax(db_connection: psycopg2, syntax: str) -> None:
    """
    Run syntax.
    :param db_connection: Database connection object.
    :param syntax: Syntax for execution.
    """
    cur = db_connection.cursor()
    cur.execute(syntax)
    cur.close()

def populate_table(table_name: str, data: pd.DataFrame) -> None:
    """
    Populate a table in the database from a pandas dataframe.
    :param table_name: The name of the table in the DB that we will add the values in df to.
    :param df: The dataframe that we use for puplating the table.
    """
    db_connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name,
    )
    
    # Inject data
    for index, row in data.iterrows():
        run_syntax(db_connection=db_connection, syntax=f"INSERT INTO {table_name} VALUES{tuple(row.values)}")
    
    db_connection.commit()
    db_connection.close()

def read_data(table_name: str):
    db_connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name,
    )
    query = pd.read_sql_query(f"SELECT * FROM {table_name}",db_connection)
    df = pd.DataFrame(query,columns=['comment','updated_comment','prediction','score'])
    return(df)