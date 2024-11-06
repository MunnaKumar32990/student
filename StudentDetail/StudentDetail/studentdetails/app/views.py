from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import details



def list_students(request):
    students = details.objects.all()  # Fetch all student details
    return render(request, 'list_students.html', {'students': students})

# Your existing add/edit student view
def details_form(request, details_id=None):
    if details_id:
        student = get_object_or_404(details, id=details_id)
    else:
        student = None

    if request.method == 'POST':
        name = request.POST.get('name')
        college_id = request.POST.get('college_id')
        email = request.POST.get('email')
        cgpa = request.POST.get('cgpa')
        branch = request.POST.get('branch')
        address = request.POST.get('address')

        if name and college_id and email and cgpa and branch and address:
            if student:
                student.name = name
                student.college_id = college_id
                student.email = email
                student.cgpa = cgpa
                student.branch = branch
                student.address = address
                student.save()
                return redirect('list_students')  # Redirect back to student list
            else:
                new_details = details(
                    name=name,
                    college_id=college_id,
                    email=email,
                    cgpa=cgpa,
                    branch=branch,
                    address=address
                )
                new_details.save()
                return redirect('list_students')
        else:
            return HttpResponse('Please fill all fields.')

    return render(request, 'index.html', {'student': student})
