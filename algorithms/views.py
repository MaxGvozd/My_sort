from django.shortcuts import render

from .forms import InputForm
from .models import Execution
from .methods import *
import json

METHODS = {
    'Bubble': Bubble(),
    'Insertion': Insertion(),
    'Merge': Merge(),
    'Quick_sort': Quick_sort()
}


def main(request):
    if request.method == 'GET':
        form = InputForm()
        return render(request, 'main.html', context={
            "form": form,
        })
    elif request.method == 'POST':
        data = request.POST
        method_name = data['method']
        uploaded_file = request.FILES['file']
        temp = uploaded_file.read().split()
        my_list = [int(i) for i in temp if i.isdigit()]
        method = METHODS.get(method_name)
        method.sort(my_list)
        sort_list = method.result
        result = json.dumps(sort_list)
        execution = Execution(
            name=uploaded_file.name,
            method=method_name,
            result=result,
        )
        execution.save()
        form = InputForm()
        return render(request, 'main.html', context={
            "form": form,
        })
