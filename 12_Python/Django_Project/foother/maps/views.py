from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator


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


@login_required
@require_http_methods(['GET', 'POST'])
def review_create(request):
    # user = request.user
    rankings = user_ranking()
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('accounts:profile', review.user.username)

    else:
        form = ReviewForm()
        # key = config('API_KEY')

    context = {
        'form' : form,
        # 'key' : key,
        'rankings' : rankings,
    }
    return render(request, 'maps/review_create.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def review_detail(request, username, review_pk):
    rankings = user_ranking()

    review = Review.objects.get(pk=review_pk)

    comments = Comment.objects.all()
    send_comments = []

    for comment in comments:
        if comment.review_id == review_pk:
            valid_comment = comment
            send_comments.append(valid_comment)

    for send in send_comments:
        print(send.review_id)
        print(send.contents)
        print(send.review.user.username)

    paginator = Paginator(send_comments, 5)
    page_number = request.GET.get('page')
    send_comments = paginator.get_page(page_number)
    
    context = {
        'review' : review,
        'comments' : comments,
        'rankings' : rankings,
        'send_comments' : send_comments,
    }

    return render(request, 'maps/review_detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def review_update(request, review_pk):
    rankings = user_ranking()
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            review = form.save()
            # (commit=False)
            # review.user = request.user
            # review.save()
            return redirect('maps:review-detail', review.user, review.pk)
    else:
        form = ReviewForm(instance=review)
       
    context = {
        'form' : form,
        'rankings' : rankings,
    }
    return render(request, 'maps/review_update.html', context)



@login_required
def like(request, review_pk):
    
    print(request)
    review = get_object_or_404(Review, pk=review_pk)
    
    print(review)
    user = request.user
    # review.like_users.filter(pk=user.pk).exist():

    if review in user.like_reviews.all():
        user.like_reviews.remove(review)
        liked = False

    else:
        user.like_reviews.add(review)
        liked= True

    context = {
        'msg' : 'like works',
        'liked' : liked,
       
    }

    return JsonResponse(context)


@login_required
def comment_create(request, comment_user_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        print("comment post 들어옴")
        form = CommentForm(request.POST)
        if form.is_valid():
            print("comment post_valid 들어옴")
            comment = form.save(commit=False)
            print(comment)
            comment.review = review
            comment.user = request.user
            comment.save()
            return render(request, 'maps/comment_complete.html')
    
    else:
        print("comment get 들어옴")
        form = CommentForm()
        context = {
            'form' : form,
            'review_pk' : review_pk,
            'comment_user_pk' : comment_user_pk,
            'review' : review,
        }
        print(form)
    
    return render(request, 'maps/comment_create.html',context)



def comment_complete(request):
    return render(request, 'maps/comment_complete.html')


def review_all(request):
    reviews = Review.objects.all()
    # paginator = Paginator(reviews, 12)
    
    # page_number = request.GET.get('page')
    # reviews = paginator.get_page(page_number)
    # for star in len(reviews.food_star):
    

    context = {
        'reviews' : reviews,
    }
    return render(request, 'maps/review_all.html', context)