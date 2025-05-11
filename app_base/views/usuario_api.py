from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from ..supabase_client import supabase
from ..models.usuario import Usuario

def parse_usuario(data: dict) -> Usuario:
    return Usuario(
        nombre = data["nombre"],
        contra = data["contra"]
    )

@require_http_methods(["GET"])
def listar_usuarios(resquest):
    response = supabase.table("users").select("*").execute()
    return JsonResponse(response.data, safe = False)

@csrf_exempt
@require_http_methods(["POST"])
def crear_usuario(request):
    try:
        data = json.loads(request.body)
        usuario = parse_usuario(data)

        result = supabase.table("users").insert(usuario.__dict__).execute()
        return JsonResponse(result.data, safe = False, status = 201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)
    
@csrf_exempt
@require_http_methods(["PUT"])
def actualizar_usuario(request, nombre):
    try:
        data = json.loads(request.body)
        usuario = parse_usuario(data)

        result = supabase.table("users").update(usuario.__dict__).eq("name", str(nombre)).execute()
        return JsonResponse(result.data, safe = False, status = 201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)
    
@csrf_exempt
@require_http_methods(["DELTE"])
def eliminar_usuario(request, nombre):
    try:
        data = json.load(request.body)
        usuario = parse_usuario(data)

        result = supabase.table("users").delete().eq("name", str(nombre)).execute()
        return JsonResponse(result.body, safe = False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)