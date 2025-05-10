from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from datetime import datetime
from ..supabase_client import supabase
from ..models import DatosAmbientales

def parse_datos_ambi(data: dict) -> DatosAmbientales:
    return DatosAmbientales(
        id_transporte = data['id_transporte'],
        producto = data['producto'],
        temperatura_actual = float(data['temperatura_actual']),
        temperatura_max = float(data['temperatura_max']),
        temperatura_min = float(data['temperatura_min']),
        humedad_actual= float(data['humedad_actual']),
        humedad_min = float(data['humedad_min']),
        humedad_max = float(data['humedad_max'])
    )

@require_http_methods(["GET"])
def listar_datos_ambientales(request):
    response = supabase.table("monitoreo_temperatura_humedad").select("*").execute()
    return JsonResponse(response.data, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def crear_ambiente(request):
    try:
        data = json.loads(request.body)
        datos_ambientales = parse_datos_ambi(data)

        result = supabase.table("monitoreo_temperatura_humedad").insert(datos_ambientales.__dict__).execute()
        return JsonResponse(result.data, safe=False, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def actualizar_ambiente(request, transporte_id):
    try:
        data = json.loads(request.body)
        datos_ambientales['id_transporte'] = transporte_id

        datos_ambientales = parse_datos_ambi(data)
        result = supabase.table("monitoreo_temperatura_humedad").update(datos_ambientales.__dict__).eq("id_transporte", str(transporte_id)).execute()
        return JsonResponse(result.data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def eliminar_ambiente(request, transporte_id):
    try:
        result = supabase.table("monitoreo_temperatura_humedad").delete().eq("id_transporte", str(transporte_id)).execute()
        return JsonResponse(result.data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
