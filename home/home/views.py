from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import random
#create your views here
def home(request):
    context = {'categories' : Category.objects.all()}
    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")
    return render(request, 'home.html', context)
def quiz(request):
    context = {'category' : request.GET.get('category')}
    return render(request, 'quiz.html', context)

def get_quiz(request):
    try:
        category_filter = request.GET.get('category')
        print("Category received:", category_filter)
        
        question_objs = Question.objects.all()
        if category_filter:
            question_objs = question_objs.filter(category__category_name__icontains=category_filter)

        print("Questions found:", question_objs)

        data = [{
            "uid": q.uid,
            "category": q.category.category_name,
            "question": q.question,
            "answers": q.get_answers()
        } for q in question_objs]

        return JsonResponse({'status': True, 'data': data})
    except Exception as e:
        print("Error:", e)
        return HttpResponse("Something went wrong")

'''
1
def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        if request.GET.get('category'):
            question_objs = question_objs.filter(category__category_name__icontains= request.GET.get('category'))
        question_objs = list(question_objs)
        data = []
        for question_obj in question_objs:
            data.append({
                "uid" : question_obj.uid,
                "category" : question_obj.category.category_name,
                "question" : question_obj.question,
                "answers" : question_obj.get_answers()
            })
        payload = {'status' : True, 'data' : data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
    return HttpResponse("Something went Wrong")

'''
