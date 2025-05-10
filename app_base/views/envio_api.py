# app_base/views/envio_api.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import uuid
from datetime import datetime
from ..supabase_client import supabase
from ..models.envio import Envio

def parse_envio(data: dict) -> Envio:
    return Envio(
        id_envio=uuid.UUID(data.get('id_envio')) if data.get('id_envio') else uuid.uuid4(),
        fechaHora_salida=datetime.fromisoformat(data['fechaHora_salida']),
        origen=data['origen'],
        destino=data['destino'],
        temperatura_objetivo=float(data['temperatura_objetivo']),
        unidad_temperatura=data['unidad_temperatura'],
        nombre_producto=data['nombre_producto'],
        cantidad=float(data['cantidad']),
        unidad=data['unidad'],
        medio_transporte=data['medio_transporte'],
        notas=data.get('notas', '')
    )

@require_http_methods(["GET"])
def listar_envios(request):
    response = supabase.table("envios").select("*").execute()
    return JsonResponse(response.data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def crear_envio(request):
    try:
        data = json.loads(request.body)
        envio = parse_envio(data)
        result = supabase.table("envios").insert(envio.__dict__).execute()
        return JsonResponse(result.data, safe=False, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def actualizar_envio(request, envio_id):
    try:
        data = json.loads(request.body)
        envio = parse_envio(data)
        result = supabase.table("envios").update(envio.__dict__).eq("id_envio", str(envio_id)).execute()
        return JsonResponse(result.data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def eliminar_envio(request, envio_id):
    try:
        result = supabase.table("envios").delete().eq("id_envio", str(envio_id)).execute()
        return JsonResponse(result.data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
