from excel_supabase_crud_operations import ExcelSupabaseDataPipeline


operator = ExcelSupabaseDataPipeline(excel_table_filepath="/Users/rob/Downloads/data_migration_softapp(motory)-2.csv",table_name="motory")
from supabase_client import ConnectSupabaseInstance

operator.insert_rows_to_supabase_table()

#table_to_import = pd.read_csv("/Users/rob/Downloads/data_migration_softapp(List1)-4.csv",encoding="cp852",sep=";")

# Attempt to read the file with the correct encoding
# Function to create key-value pairs for each cell
# Function to create key-value pairs for each cell

