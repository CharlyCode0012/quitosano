from supabase import create_client, Client
from pydantic.dataclasses import dataclass


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

class Users(BaseTable):
    def __init__(self, db : Supabase):
        super().__init__(db, "users")
    
    def add(self, name: str, password : str):
         self.insert({"name" : name, "password" : password}) 
    
class Transporte(BaseTable):
    def __init__(self, db : Supabase):
        super().__init__(db, "transporte_quitosano")

    def add(self, id_trasnporte: str, origen: str, destino: str, producto: str, cantidad_kg: int):
        self.insert({
            "id_transporte" : id_trasnporte,
            "origen" : origen, 
            "destino" : destino,
            "producto" : producto,
            "cantidad_kg" : cantidad_kg
        })

#need sensor to gather data
"""class TempMon(BaseTable):
    def __init__(self, db : Supabase):
        super().__init__(db, "monitoreo_temperatura_humedad")

    #def getCurrentTemp(self) -- missing data"""