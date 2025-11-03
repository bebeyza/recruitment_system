from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPosting, Candidate, Application


def home(request):
    return render(request, 'home.html')


# İŞ İLANI FONKSİYONLARI
def job_list(request):
    jobs = JobPosting.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})


def job_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        JobPosting.objects.create(title=title, description=description, location=location)
        return redirect('job_list')
    return render(request, 'job_form.html')


def job_update(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    if request.method == 'POST':
        job.title = request.POST['title']
        job.description = request.POST['description']
        job.location = request.POST['location']
        job.save()
        return redirect('job_list')
    return render(request, 'job_form.html', {'job': job})


def job_delete(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    job.delete()
    return redirect('job_list')


# ADAY FONKSİYONLARI
def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})


def candidate_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        Candidate.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone)
        return redirect('candidate_list')
    return render(request, 'candidate_form.html')


def candidate_update(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    if request.method == 'POST':
        candidate.first_name = request.POST['first_name']
        candidate.last_name = request.POST['last_name']
        candidate.email = request.POST['email']
        candidate.phone = request.POST['phone']
        candidate.save()
        return redirect('candidate_list')
    return render(request, 'candidate_form.html', {'candidate': candidate})


def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    candidate.delete()
    return redirect('candidate_list')


# BAŞVURU FONKSİYONLARI
def application_list(request):
    applications = Application.objects.all()
    return render(request, 'application_list.html', {'applications': applications})


def application_create(request):
    if request.method == 'POST':
        job_id = request.POST['job_posting']
        candidate_id = request.POST['candidate']
        status = request.POST['status']
        Application.objects.create(job_posting_id=job_id, candidate_id=candidate_id, status=status)
        return redirect('application_list')

    jobs = JobPosting.objects.all()
    candidates = Candidate.objects.all()
    return render(request, 'application_form.html', {'jobs': jobs, 'candidates': candidates})


def application_update(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        application.job_posting_id = request.POST['job_posting']
        application.candidate_id = request.POST['candidate']
        application.status = request.POST['status']
        application.save()
        return redirect('application_list')

    jobs = JobPosting.objects.all()
    candidates = Candidate.objects.all()
    return render(request, 'application_form.html',
                  {'application': application, 'jobs': jobs, 'candidates': candidates})


def application_delete(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.delete()
    return redirect('application_list')