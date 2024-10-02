# core/views.py
from django.shortcuts import render, get_object_or_404
from .models import Project
from django.http import HttpResponse


def home_view(request):
    return render(request, "codenova/home.html")


def about_view(request):
    return render(request, "codenova/about.html")


def services_view(request):
    return render(request, "codenova/services.html")


def portfolio_view(request):
    return render(request, "codenova/portfolio.html")  # Make sure this template exists


def blog_view(request):
    return render(request, "codenova/blogs.html")


def contact_view(request):
    return render(request, "codenova/contact.html")  # Make sure this template exists


def project_details_view(request):
    return render(
        request, "codenova/project-details.html"
    )  # Make sure this template exists


def project_details_view2(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "codenova/project-details.html", {"project": project})


def blog_details_view(request):
    return render(
        request, "codenova/blog-details.html"
    )  # Make sure this template exists


def download_file_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Check if the file exists
    if project.file:
        response = HttpResponse(project.file, content_type="application/octet-stream")
        response["Content-Disposition"] = f'attachment; filename="{project.file.name}"'
        return response
    else:
        return HttpResponse("File not found.")
