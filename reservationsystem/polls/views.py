#from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from .models import Question

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)
#=================================================================================
# from django.http import HttpResponse
# from django.template import loader

# from .models import Question


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#==================================================================================
from django.shortcuts import render
from django.views import generic
from .models import Survey

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_survey_list"

    def get_queryset(self):
        """Return the last five published surveys."""
        return Survey.objects.order_by("-id")[:5]


class SurveyDetailView(generic.DetailView):
    model = Survey
    template_name = "polls/detail.html"