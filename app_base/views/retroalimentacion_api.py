from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import uuid
import json
from datetime import date
from ..supabase_client import supabase
from ..models import Retroalimentacion

def parse_retroalimentacion(data: dict) -> Retroalimentacion:
    return Retroalimentacion(
        folio_compra = uuid.UUID(data.get('folio_compra')) if data.get('folio_compra') else uuid.uuid4(),
        fecha_compra = date.fromisoformat(data['fecha_compra']),
        comprador = data['comprador'],
        comentarios = data['comentarios'],
        cantidad_comprada = data['cantidad_comprada'],
    )

@require_http_methods(["GET"])
def listar_retroalimentacion(request):
    response = supabase.table("feedback").select("*").execute()
    return JsonResponse(response.data, safe = False)

@csrf_exempt
@require_http_methods(["POST"])
def crear_retro(request):
    try:
        data = json.loads(request.body)
        retroalimentacion = parse_retroalimentacion(data)
        retro_dict = retroalimentacion.__dict__.copy()
        retro_dict["folio_compra"]  =  str(retroalimentacion.folio_compra)
        retro_dict["fecha_compra"]  =  retroalimentacion.fecha_compra.isoformat()

        result = supabase.table("feedback").insert(retro_dict).execute()
        return JsonResponse(result.data, safe = False, status = 201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)


@csrf_exempt
@require_http_methods(["PUT"])
def actualizar_retro(request, folio_compra):
    try:
        data = json.loads(request.body)
        retroalimentacion = parse_retroalimentacion(data)

        retro_dict = retroalimentacion.__dict__.copy()
        retro_dict["folio_compra"]  =  str(retroalimentacion.folio_compra)
        retro_dict["fecha_compra"]  =  retroalimentacion.fecha_compra.isoformat()

        
        result = supabase.table("feedback").update(retro_dict).eq("folio_compra", str(folio_compra)).execute()
        return JsonResponse(result.data, safe = False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)


@csrf_exempt
@require_http_methods(["DELETE"])
def eliminar_retro(request, folio_compra):
    try:
        result = supabase.table("feedback").delete().eq("folio_compra", str(folio_compra)).execute()
        return JsonResponse(result.data, safe = False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status = 400)
