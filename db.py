from supabase import create_client, Client
from pydantic.dataclasses import dataclass
from datetime import datetime
import uuid

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
    
    #not on web
    def delete_by_name(self, name: str):
        self.delete_by_field("name", name)
    
    #not on web
    def find_one_by_name(self, name : str):
        return self.find_one_by_field("name", name)
    
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
    
    #not on web
    def delete_one(self, id_transporte: str):
        self.delete_by_field("id_transporte", id_transporte)

    def find_all(self):
        self.list_all()

#need sensor to get data
"""class TempMon(BaseTable):
    def __init__(self, db : Supabase):
        super().__init__(db, "monitoreo_temperatura_humedad")

    #def getCurrentTemp(self) -- missing data"""



#not on web 
"""class Compras(BaseTable):
    def __init__(self, db : Supabase):
        super().__init__(db, "Compras")

    def add(self, comprador : str, cantidad : int, comentarios : str):
        folio_compra = uuid.uuid4()
        fecha = datetime.now()
        fecha = fecha.isoformat()
        self.insert({
            "Comprador" : comprador,
            "Cantidad" : cantidad,
            "Fecha" : fecha, 
            "Folio de compra" : str(folio_compra),
            "Comentarios" : comentarios
        })

    def delete_one(self, name : str):
        self.delete_by_field("Comprador", name)

    def find_one_name(self, name : str):
        return self.find_one_by_field("Comprador", name)
    
    def find_one_folio(self, folio : str):
        return self.find_one_by_field("Folio de compra", folio)"""

#not on web
"""class Envios(BaseTable):
    def __init__(self, db : Supabase):
        super().__init__(db, "envios")

    def add(self, origen : str, destino : str, temp_objetivo : float, temp_unit : str,
            nombre_producto : str, cantidad : int, unit : str, medio_transporte : str,notas : str):
        id_envio = uuid.uuid4()
        fecha_salida = datetime.now()
        fecha_salida = fecha_salida.isoformat()
        self.insert({
            "id_envio" : str(id_envio),
            "origen" : origen,
            "fechaHora_salida" : fecha_salida,
            "destino" : destino,
            "temperatura_objetivo" : temp_objetivo,
            "unidad_temperatura" : temp_unit,
            "nombre_producto" : nombre_producto,
            "cantidad" : cantidad,
            "unidad" : unit,
            "medio_transporte" : medio_transporte,
            "notas" : notas
        })

    def delete_one_id_envio(self, id_envio : str):
        self.delete_by_field("id_envio",id_envio)
    
    def find_one_id_envio(self, id_envio : str):
        return self.find_one_by_field("id_envio", id_envio)"""
    

