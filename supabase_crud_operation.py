import pandas as pd
from supabase_client import ConnectSupabaseInstance

supabase_instance = ConnectSupabaseInstance()
table_to_import = pd.read_csv("/Users/rob/Downloads/data_migration_softapp(List1)-4.csv",encoding="cp852",sep=";")

# Attempt to read the file with the correct encoding
# Function to create key-value pairs for each cell
# Function to create key-value pairs for each cell
def create_key_value_pairs(df):
    result = []
    for _, row in df.iterrows():
        row_dict = {column: row[column] for column in df.columns}
        result.append(row_dict)
    return result

# Create key-value pairs
key_value_pairs = create_key_value_pairs(table_to_import)


# Output the result
for item in key_value_pairs:
    #print(item)
    # Print each item with UTF-8 encoding
    print({k: v for k, v in item.items()})
    data, count = supabase_instance.supabase.table('motory').insert(item).execute()
