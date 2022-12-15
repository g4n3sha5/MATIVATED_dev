from django.shortcuts import render, redirect
from .models import TrainingSession, TrainingSessionForm, Technique, addTechniqueForm
from django.contrib import messages
# Create your views here.
def BJJournalIndex (request):

    context = {
        'user' : request.user
    }
    return render(request, "BJJournal/BJR_index.html", context)

def dashboard(request):

    context = {

    }

    return render (request, "BJJournal/BJR_dashboard.html", context)


def addSession(request):
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST)

        if form.is_valid():
            tp = form.cleaned_data["type"]
            leng = form.cleaned_data["length"]
            dat = form.cleaned_data["date"]
            loc = form.cleaned_data["location"]
            nots = form.cleaned_data["notes"]
            # ts = TrainingSession(name=n)
            # ts.save()
            # t.user_lists.add(request.user)

    else:
        form = TrainingSessionForm()

    context = {
        'BJRform': form,
        'techniquesList': Technique.objects.all()
    }
    return render(request, "BJJournal/BJR_addSession.html", context)

def techniques(request):
    if request.method == 'POST':
        form = addTechniqueForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Added your technique")
            return redirect('/techniques')

        else:
            messages.error(request, "Invalid form. ")

    else:
        form = addTechniqueForm()


    context = {
        'TechForm': form,
        'techniquesList': Technique.objects.all()
    }
    return render(request, "BJJournal/BJR_Techniques.html", context)


def singleTechniqueView(request):
    print("hujj")
    # technique = Technique.objects.get(pk=id)

    context = {
        # 'technique': technique
    }
    return render(request, "BJJournal/BJR_Techniques_singleTechniqueView.html", context)

# def addTechnique(request):
#     if request.method == 'POST':
#         form = addTechniqueForm(request.POST)
#         if form.is_valid():
#             tp = form.cleaned_data["type"]
#             leng = form.cleaned_data["length"]
#             dat = form.cleaned_data["date"]
#             loc = form.cleaned_data["location"]
#             # ts = TrainingSession(name=n)
#             # ts.save()
#             # t.user_lists.add(request.user)
#     #
#     # else:
#     #     form = TrainingSessionForm()
#
#     # context = {
#     #     'BJRform': form,
#     #     'techniquesList': Technique.objects.all()
#     # }
#     return render(request, "BJJournal/BJR_addSession.html", context)


