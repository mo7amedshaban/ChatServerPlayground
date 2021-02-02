from django.shortcuts import render
from public_chat.forms import PublicChatForm


# Create your views here.
def home_screen_view(request):
    return render(request, 'public_chat/home.html')


def public_chat(request, **kwargs):
    if reques.method == 'POST':
        form = PublicChatForm(request.POST)
        if form.is_valid():
            form.save()
