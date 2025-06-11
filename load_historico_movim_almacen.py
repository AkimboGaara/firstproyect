import pandas as pd
from sqlalchemy import create_engine


def load_historico_movim_almacen(connection_string: str) -> pd.DataFrame:
    """Load HISTORICO_MOVIM_ALMACEN table into a DataFrame."""
    engine = create_engine(connection_string)
    query = "SELECT * FROM HISTORICO_MOVIM_ALMACEN"
    df = pd.read_sql(query, engine)
    return df


if __name__ == "__main__":
    conn_str = "sqlite:///example.db"  # Replace with your DB
    df = load_historico_movim_almacen(conn_str)
    print(df.head())
