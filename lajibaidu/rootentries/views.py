from django.http import HttpResponse
from django.template import loader

rooturls={
    "uservote":"uservote/"
}

def index(request):
    template = loader.get_template('rootentries/index.html')
    context = {
        'rooturls': rooturls,
    }
    return HttpResponse(template.render(context, request))


def navigation(request):
    template = loader.get_template('rootentries/navigation.html')
    context = {
        'rooturls': rooturls,
    }
    return HttpResponse(template.render(context, request))

