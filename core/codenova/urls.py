# core/urls.py
from django.urls import path
from .views import (
    home_view,
    about_view,
    services_view,
    portfolio_view,
    blog_view,
    contact_view,
    project_details_view,
    project_details_view2,
    blog_details_view,
    download_file_view,
)  # Import your views

urlpatterns = [
    path("", home_view, name="home"),  # Home page
    path("about/", about_view, name="about"),  # About page
    path("services/", services_view, name="services"),  # Services page
    path("portfolio/", portfolio_view, name="portfolio"),  # Portfolio page
    path("blog/", blog_view, name="blogs"),  # Blog page
    path("contact/", contact_view, name="contact"),  # Contact page
    path(
        "project_details/", project_details_view, name="project_details"
    ),  # Contact page
    path("blog-details/", blog_details_view, name="blog-details"),
    path("project/<int:project_id>/", project_details_view2, name="project_details"),
    path(
        "project/<int:project_id>/download/", download_file_view, name="download_file"
    ),  # Add this line
]
