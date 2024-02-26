
"""
To render html web pages
"""
from django.http import HttpResponse
from articles.models import Article
from random import randint
from django.template.loader import render_to_string

HTML_STRING = """
<h1>Hello World</h1>
"""

def home_view(request, id=None, *args, **kwargs):

    num = randint(1,4)
    article_obj = Article.objects.get(id=num)
    articles = Article.objects.all()
    my_list = articles
    context = {
        "title": article_obj.title,
        "content": article_obj.content,
        "my_list": my_list,
    }
    # HTML_STRING = """
    # <h1>{title}</h1> <h2>is title and this is {content}</h2> """.format(**context)
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)
