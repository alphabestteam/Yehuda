from django.shortcuts import render
from django.http import HttpResponse
import random as rnd
from datetime import datetime



rnd_num = rnd.random()
now = datetime.now()


def home(request):
    return HttpResponse("hello django")

def random_number(request):
    return HttpResponse(f"ok 200 {rnd_num}")

def random_number_user(request,number):
    if number.isnumeric() :      
        rnd_num = rnd.uniform(0 , int(number))
        return HttpResponse(f"ok 200 {rnd_num}")
    else:
        return HttpResponse("pls enter only number ")
 
def serverTime(request):
    current_time = now.strftime("%H:%M:%S")
    return HttpResponse(f'200 ok Current Time = {current_time}' )

def LengthOfWord(request,word):
    if word.isalpha():
        return HttpResponse(f"ok 200 the len of the word is :  {len(word)}")
    else:
        return HttpResponse("pls enter only letter !")
          
 