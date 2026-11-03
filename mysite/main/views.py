
from django.shortcuts import render, redirect
from .forms import StudentForm, ClacForm
from .models import Student


def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form = StudentForm()

    return render(request, 'main/home.html', {'form': form})


def result(request):
    students = Student.objects.all()
    return render(request, 'main/result.html', {'students': students})

# def calc(request)
#     result()
#     if request.method == 'POST':
#         form = ClacForm(request.POST)
#
#     return render(request, 'main/clac', {'forms': form})
