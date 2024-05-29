from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest) -> HttpResponse:
    your_name = "ivencic"
    return HttpResponse(f"""<h1>Hello, {your_name}</h1>""")
