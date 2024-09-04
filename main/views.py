from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306203526',
        'name': 'Belva Ghani Abhinaya',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
