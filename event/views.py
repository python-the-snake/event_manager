from django.shortcuts import render
import numba



def main_app(request):
    return render(request, 'main_app.html')