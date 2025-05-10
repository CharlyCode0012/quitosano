from supabase import create_client, Client
from pydantic.dataclasses import dataclass
from datetime import datetime

@dataclass
class Supabase:
    url : str
    key : str
    
    def __post_init__(self):
        self.client: Client = create_client(self.url, self.key)

class BaseTable:
    def __init__(self, db : Supabase, table_name : str):
        self.table = db.client.table(table_name)
    
    def insert(self, data : dict):
        self.table.insert(data).execute()

    def delete_by_field(self, field: str, value):
        self.table.delete().eq(field, value).execute()
    
    def find_one_by_field(self, field : str, value):
        return self.table.select("*").eq(field, value).execute()
    
    def list_all(self):
        return self.table.select("*").execute()
    
    def get_last_record(self, field: str, field_2: str):
        return self.table.select(field).order(field_2, desc=True).limit(1).execute()

class Users(BaseTable):
    def __init__(self, db : Supabase):
        super().__init__(db, "users")
    
    def add(self, name: str, password : str):
         self.insert({"name" : name, "password" : password}) 
    
class Transporte(BaseTable):
    def __init__(self, db : Supabase):
        super().__init__(db, "transporte_quitosano")

    def add(self, origen: str, destino: str, producto: str, cantidad_kg: int):
        current_year = str(datetime.now().year)
        current_date = str(datetime.now())
        last_id = self.get_last_record("id_transporte", "Fecha")
        last_id = last_id.data[0]["id_transporte"]
        last_id = str(last_id).split("-")[-1]
        last_id = int(last_id) + 1
        next_id = str(last_id).zfill(3)
        id_transporte = "TR-"+current_year+"-"+next_id
        self.insert({
            "id_transporte" : id_transporte,
            "origen" : origen, 
            "destino" : destino,
            "producto" : producto,
            "cantidad_kg" : cantidad_kg,
            "Fecha" : current_date
        })

#need sensor to gather data
"""class TempMon(BaseTable):
    def __init__(self, db : Supabase):
        super().__init__(db, "monitoreo_temperatura_humedad")

    #def getCurrentTemp(self) -- missing data"""
