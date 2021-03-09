from django.shortcuts import render
from django.http.response import HttpResponse
import random
import requests,json

def var_route(request, value):
    
    return HttpResponse(value)

# Create your views here.
def lotto(request, when):
    
    
    # 1. 현실 로또 번호를 가져온다.
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={ when }'
    results = requests.get(url).json()
    lotto=[results['drwtNo1'], results['drwtNo2'], results['drwtNo3'], results['drwtNo4'], results['drwtNo5'], results['drwtNo6']]
    bonus=results['bnusNo']
    data={'when': when,'bonus':bonus, 'lotto':lotto}
    cnt_win=[0]*5   
    looser=0
    for i in range(10000):
        wincount=0
        tmp_lotto=random.sample(range(1,46),6)
        for lotto_num in tmp_lotto:
            if lotto_num in lotto:
                wincount += 1
        if wincount == 6:
            cnt_win[0] += 1
        elif wincount == 5:
            if bonus in tmp_lotto:
                cnt_win[1] += 1
            else:
                cnt_win[2] += 1
        elif wincount == 4:
            cnt_win[3] += 1
        elif wincount == 3:
            cnt_win[4] += 1
        else:
            looser +=1
    data['winners']=cnt_win
    data['looser']=looser
    return render(request, 'practice0309/lotto.html', data)

def ping(request):
    return render(request, 'practice0309/ping.html')

def pong(request):
    
    kr_name=request.GET['kor-name']
    en_name=request.GET['eng-name']
    context={
        'kr_name':kr_name,
        'en_name':en_name,
        'full_name': kr_name + en_name
    }
    return render(request, 'practice0309/pong.html', context)