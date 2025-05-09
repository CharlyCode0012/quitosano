from supabase import create_client
from decouple import config
import sys

try:
    SUPABASE_URL = config("SUPABASE_URL")
    SUPABASE_KEY = config("SUPABASE_KEY")
except Exception as e:
    print("❌ Error cargando variables:", e)
    sys.exit("Variables de entorno faltantes")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("❌ Variables vacías:")
    print("SUPABASE_URL =", SUPABASE_URL)
    print("SUPABASE_KEY =", SUPABASE_KEY)
    sys.exit("❌ No se encontraron las variables necesarias")

print("✅ SUPABASE_URL leída correctamente:", SUPABASE_URL)

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
