from  .models import Article
from django.shortcuts import render, redirect
from django.http import Http404


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if request.user != 'AnonymousUser':
        if request.method == "POST":
            form = {
                'text': request.POST["text"],
                'title': request.POST["title"]
            }
            not_unique = Article.objects.filter(title=form['title'])
            if not_unique:
                form['errors'] = u'Ошибка: Статья с таким названием уже существует. Придумайте другое.'
                return render(request, 'form.html', {'form': form})
            if form["text"] and form["title"]:
                Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return render(request, 'archive.html', {"posts": Article.objects.all()})
            else:
                form['errors'] = u"Ошибка: Не все поля заполнены."
                return render(request, 'form.html', {'form': form})
        else:
            return render(request, 'form.html', {})
    else:
        raise Http404