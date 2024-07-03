import os
from supabase import create_client, Client

class ConnectSupabaseInstance:
    def __init__(self):
        self.csv_filepath = "credentials/credentials.csv"
        self.supabase = None
        with open(self.csv_filepath,"r") as csv_file:
            whole_string = csv_file.readlines()
            url = list(whole_string)[0].split(sep=",")[0]
            api_key = list(whole_string)[0].split(sep=",")[1]

        url: str = os.environ.get("SUPABASE_URL",url)
        key: str = os.environ.get("SUPABASE_KEY",api_key)
        self.supabase: Client = create_client(url, key)



#data, count = supabase_instance.supabase.table('countries').insert({"id": 1, "name": "Denmark"}).execute()



