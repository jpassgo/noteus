from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from .serializers import NoteSerializer
from .models import Note

# @method_decorator(csrf_exempt, name='dispatch')
class Notes(APIView):

    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {'text_content': request.data.get('text_content'),}
        
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)