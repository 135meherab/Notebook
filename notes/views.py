from django.shortcuts import render

# Create your views here.
mynotes = [
    {'id' : 1, 'title' : 'First note', 'Entries':['Entries 1.1', 'Entries 1.2','Entries 1.3']},           
    {'id' : 2, 'title' : 'Second note', 'Entries':['Entries 2.1', 'Entries 2.2','Entries 2.3']} ,          
    {'id' : 3, 'title' : 'Third note', 'Entries':['Entries 3.1', 'Entries 3.2','Entries 3.3']}  ,         
           ]
def index(request):
    return render(request,'index.html')

def notes(request):
    notes = mynotes
    cntext = {'notes': notes}
    return render(request,'notes.html', cntext)

def note(request,note_id):
    for mynote in mynotes:
        if note_id == mynote['id']:
            note = mynote
    entries = note['Entries']
    context = {'note': note, 'entries': entries}
    return render (request,'note.html', context)
