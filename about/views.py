from django.shortcuts import render
from .models import AboutPage


def about_page(request):
    """
    Render the about page with content from the database.

    Fetches the first AboutPage object to display on the about page.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered 'about/about.html' template with the AboutPage content.
    """
    about_content = AboutPage.objects.first()
    return render(request, 'about/about.html',
                  {'about_content': about_content})
