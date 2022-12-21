from django.shortcuts import render
from django.http import HttpResponse
from voters.models import Voter
from django.utils import timezone
from django.db import IntegrityError, transaction
from django.contrib.auth.decorators import login_required

from .forms import VoteForm

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required
def send_vote(request):
    is_user_voted_earlier = Voter.objects.filter(user=request.user).exists()
    if (is_user_voted_earlier):
        return render(request,"vote_second_time.html")

    form = VoteForm(request.POST or None)
    ip = '';
    if form.is_valid():
        try:
            ip = get_client_ip(request)
        except Exception as e:
            print("Błąd pobierani IP")
            print(e)
        try:
            with transaction.atomic():
                Voter.objects.create(pk=request.user.id, user=request.user, created=timezone.now(), user_agent=request.META['HTTP_USER_AGENT'], ip=ip)
                instance = form.save(commit=False)
                instance.save()
        except IntegrityError:
            print(IntegrityError)
            return render(request,"vote_second_time.html")

        return render(request,"vote_saved.html")

    context = {"form": form}
    return render(request,"vote.html",context)

def vote_help_view(request):
    return render(request, "pomoc.html",{"header": "Pomoc"})
