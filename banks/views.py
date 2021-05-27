from django.shortcuts import render
# from .populate import do_branch, do_bank
# Create your views here.

populate = False
def HomeView(request):
    if populate:
        pass
        # do_bank()
        # do_branch()
    return render(request, 'home.html')

