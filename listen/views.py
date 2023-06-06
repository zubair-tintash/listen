"""
To render html web pages
"""

from django.http import HttpResponse

HTML_STRING = """
<h1>Hello World</h1>
"""


def home_view(request):
    """
    Take in a request and return html as a response
    :param request:
    :return:
    """
    return HttpResponse(HTML_STRING)
