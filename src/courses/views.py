from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import CourseModelForm
from .models import Course
# BASE VIEW CLASS = VIEW

class CourseCreateView(View):
    template_name = 'courses/course_create.html' # DetailView
    def get(self, request, *args, **kwargs):
        # GET method
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        # POST method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()
    
    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)
    

class CourseView(View):
    template_name = 'courses/course_detail.html' # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        if id is not None:
            obj = get_object_or_404(Course, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)

    # def post(request, *args, **kwargs):
    #     return render(request, 'about.html', {})


# HTTP METHODS

def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})