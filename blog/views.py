from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm


def postList(request):
    allPost = Post.objects.all()

    context = {
        'allPost': allPost
    }

    return render(request, 'blog/postList.html', context)

def postDetail(request, id):
    postDetail = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=postDetail)


    if request.method == 'POST':
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            newCommentForm = commentForm.save(commit=False)
            newCommentForm.user = request.user
            newCommentForm.post = postDetail
            newCommentForm.save()            
    else:
        commentForm = CommentForm()
        

    context = {
        'postDetail': postDetail,
        'comments': comments,
        'commentForm': commentForm
    }

    return render(request, 'blog/postDetail.html', context)


