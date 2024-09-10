from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import MST_Student, MST_Subject


def student_list(request):
    students = MST_Student.objects.all()

    query = request.GET.get('q')
    if query:
        students = students.filter(student_name__icontains=query)

    filter_remarks = request.GET.get('filter')
    if filter_remarks:
        students = students.filter(remarks=filter_remarks)

    return render(request, 'student_grades/student_list.html', {'students': students})


def insert_example_data(request):
    # Insert some example subjects
    math = MST_Subject.objects.get_or_create(subject_key='MATH101', subject_name='Mathematics')[0]
    science = MST_Subject.objects.get_or_create(subject_key='SCI101', subject_name='Science')[0]

    # Insert some example students with grades
    student_1 = MST_Student.objects.get_or_create(student_key='STU001', student_name='John Doe', subject_name=math, grade=85)
    student_2 = MST_Student.objects.get_or_create(student_key='STU002', student_name='Jane Smith', subject_name=science, grade=65)

    return render(request, 'student_grades/insert_success.html')
