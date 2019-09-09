from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from done.models import ThisDone
def check_done(request):
    try:
        check = request.GET.get('check','')

        if check:
            if check.isdigit():
                checking = ThisDone.objects.get(id__exact = check)
            else:
                checking = None
        else:
            checking = ""
    except ObjectDoesNotExist:
        checking = None

    return render(request, 'done/checkdone.html',{"cheking":checking})