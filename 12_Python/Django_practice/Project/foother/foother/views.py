from django.shortcuts import render
from foods.models import FoodCategory
# from django.core.paginator import Paginator
from django.contrib.auth import get_user_model


def user_ranking():
    User = get_user_model()
    users = User.objects.all()
    if len(users) >3:
        while len(users) == 3:
            del users[-1]
    
    ranking = {
        'ranking' : users,
    }
    # return User.objects.all()
    return ranking
    # rankings = user_ranking()


def foother_index(request):
    rankings = user_ranking()
    foodsCategories = FoodCategory.objects.all()
    # emotion = Emotion.objects.get(name=Food.food_name).emotion
    # foods = emotion.food_set.all()

    context = {
        'foodsCategories' : foodsCategories,
        'rankings' : rankings
        # 'foods' : foods
    }
    return render(request,'foods/food_main.html', context)

#동규오빠 랭킹
# def make_users():
#     User = get_user_model()
#     users = User.objects.all()
#     if len(users) >5:
#         while len(users) == 5:
#             del users[-1]
    
#     context = {
#         'users' : users,
#     }
#     # return User.objects.all()
#     return context

# def ???(reuqest):
#     users = User.objects.all()
#     if len(users) >5:
#         while len(users) == 5:
#             del users[-1]
    
#     context = {
#         'users' : users,
#     }
#     return render(request, 'base.html', context)
