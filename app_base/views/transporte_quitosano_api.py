# app_base/views/envio_api.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from datetime import datetime
from ..supabase_client import supabase
from ..models.transporte_quitosano import TransporteQuitosano

def parse_transporte(data: dict) -> TransporteQuitosano:
    return TransporteQuitosano(
        id_transporte = data['id_envio'],
        origen = data['origen'],
        destino = data['destino'],
        producto = data['producto'],
        cantidad = float(data['cantidad']),
        fecha = datetime.fromisoformat(data['fecha']),
    )

@require_http_methods(["GET"])
def listar_transportes(request):
    response = supabase.table("transporte_quitosano").select("*").execute()
    return JsonResponse(response.data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def crear_transporte(request):
    try:
        data = json.loads(request.body)
        transporte = parse_transporte(data)
        transporte_dict = transporte.__dict__.copy()
       
        transporte_dict["fecha"] = transporte.fecha.isoformat()

        result = supabase.table("transporte_quitosano").insert(transporte_dict).execute()
        return JsonResponse(result.data, safe = False, status = 201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)


@csrf_exempt
@require_http_methods(["PUT"])
def actualizar_transporte(request, transporte_id):
    try:
        data = json.loads(request.body)
        transporte = parse_transporte(data)
        transporte_dict = transporte.__dict__.copy()
        
        transporte_dict["fecha"] = transporte.fecha.isoformat()

        result = supabase.table("tansporte_quitosano").update(transporte_dict).eq("id_transporte", str(transporte_id)).execute()
        return JsonResponse(result.data, safe = False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)


@csrf_exempt
@require_http_methods(["DELETE"])
def eliminar_transporte(request, transporte_id):
    try:
        result = supabase.table("transporte_quitosano").delete().eq("id_transporte", str(transporte_id)).execute()
        return JsonResponse(result.data, safe = False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)
