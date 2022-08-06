import psycopg2
import pandas as pd

def run_syntax(db_connection: psycopg2, syntax: str) -> None:
    """
    Run syntax.
    :param db_connection: Database connection object.
    :param syntax: Syntax for execution.
    """
    cur = db_connection.cursor()
    cur.execute(syntax)
    cur.close()


def create_table(schema: str, table: str) -> None:
    """
    Create a table in the DB based on a schema.
    :param schema: The table schema.
    :param schema: The schema.
    :param table: The name of the table.
    """
    db_connection = psycopg2.connect(
        host='ec2-34-227-120-79.compute-1.amazonaws.com',
        user='niwisgpkanhoxg',
        password='db78f028a6f0ef2daba54675f2aa2da4991abc7d1d56d9fde96d78927602002c',
        dbname='ddieop547ho0p4',
    )

    # Create table if it does not yet exist
    run_syntax(db_connection=db_connection, syntax=f"CREATE TABLE IF NOT EXISTS {table}({schema})")

    db_connection.commit()
    db_connection.close()


def populate_table(table_name: str, data: pd.DataFrame) -> None:
    """
    Populate a table in the database from a pandas dataframe.
    :param table_name: The name of the table in the DB that we will add the values in df to.
    :param df: The dataframe that we use for puplating the table.
    """
    db_connection = psycopg2.connect(
        host='ec2-34-227-120-79.compute-1.amazonaws.com',
        user='niwisgpkanhoxg',
        password='db78f028a6f0ef2daba54675f2aa2da4991abc7d1d56d9fde96d78927602002c',
        dbname='ddieop547ho0p4',
    )
    
    # Inject data
    for index, row in data.iterrows():
        run_syntax(db_connection=db_connection, syntax=f"INSERT INTO {table_name} VALUES{tuple(row.values)}")
        db_connection.commit()
    db_connection.close()

def read_data(table_name: str):
    db_connection = psycopg2.connect(
    host='ec2-34-227-120-79.compute-1.amazonaws.com',
    user='niwisgpkanhoxg',
    password='db78f028a6f0ef2daba54675f2aa2da4991abc7d1d56d9fde96d78927602002c',
    dbname='ddieop547ho0p4',
    )
    query = pd.read_sql_query(f"SELECT * FROM {table_name}",db_connection)
    df = pd.DataFrame(query,columns=['comment','updated_comment','prediction','score'])
    return(df)