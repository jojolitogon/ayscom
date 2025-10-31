# source/transform.py
import pandas as pd

from source.utils import to_numeric

def convert_to_numeric(col):
    return to_numeric(col)
# def transform_data(df: pd.DataFrame) -> pd.DataFrame:
#     """Limpia y transforma el DataFrame según las reglas del ejercicio."""

#     # Eliminar duplicados
#     df = df.drop_duplicates()

#     # Convertir strings a minúsculas
#     for col in df.select_dtypes(include=["object"]).columns:
#         df[col] = df[col].str.lower()

#     # Crear columna 'total' = quantity * price
#     if "quantity" in df.columns and "price" in df.columns:
#         df["total"] = df["quantity"] * df["price"]
#     else:
#         raise ValueError("El DataFrame no contiene las columnas 'quantity' o 'price'.")

#     return df
