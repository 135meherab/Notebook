from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.index, name = 'index'),
    path('notes/', views.notes, name = 'notes'),
    path('note/<int:note_id>', views.note, name = 'note'),
]