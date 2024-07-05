import csv
import io
import pandas as pd
from supabase_client import ConnectSupabaseInstance

#supabase_instance = ConnectSupabaseInstance()


class ExcelSupabaseDataPipeline:
    """
    defining class which reads an csv output of
    formated Excel table from a given file
    """
    def __init__(self,excel_table_filepath: str, table_name: str):
        self.supabase_instance = ConnectSupabaseInstance()
        self.filepath = excel_table_filepath
        self.table_name = table_name

        with open(self.filepath,"rb") as file:
            csv_bytes = file.read()

        csv_buffer = io.BytesIO(csv_bytes)
        try:
            self.df = pd.read_csv(csv_buffer, sep=";", encoding="utf-8",quotechar='"', quoting=csv.QUOTE_MINIMAL)
        except UnicodeError:
            csv_buffer.seek(0)
            self.df = pd.read_csv(csv_buffer, sep=";", encoding="latin1",quotechar='"',quoting=csv.QUOTE_MINIMAL)


    def create_key_value_pairs(self) -> list:
        result = []
        for _, row in self.df.iterrows():
            row_dict = {column: row[column] for column in self.df.columns}
            result.append(row_dict)
        return result


    #Receives a list of key,value pairs and INSTERTS it to
    #Supabase database table

    def insert_rows_to_supabase_table(self):
        key_value_pairs = self.create_key_value_pairs()
        # Insert the key-value pairs to the Supabase database table
        # Output the result
        for item in key_value_pairs:
            #print(item)
            # Print each item with UTF-8 encoding
            print({k: v for k, v in item.items()})
            self.supabase_instance.supabase.table(self.table_name).insert(item).execute()

