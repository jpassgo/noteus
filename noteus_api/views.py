from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Note
import json

@method_decorator(csrf_exempt, name='dispatch')
class Notes(View):

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        text_content = data.get('text_content')

        note = Note.objects.create(text_content)

        data = {
            "message": f"New note added with id: {note.id}"
        }
        return JsonResponse(data, status=201)