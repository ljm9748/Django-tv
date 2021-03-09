from django.shortcuts import render
import random

def lotto(request):
    lotto=random.sample(range(1,46),6)
    lotto.sort()
    context={'lotto':lotto,
          'greeting':'hello world'}
    return render(request, 'workshop0308/lotto.html',context)

# Create your views here.
