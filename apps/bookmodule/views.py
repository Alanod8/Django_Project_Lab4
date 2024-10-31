
# Django views for bookmodule (Tasks 1, 2, 3, 4, 5, and 7)
from django.http import HttpResponse
from django.shortcuts import render

# Task 1: Basic index view with Hello World
def index(request):
    # Task 2: Retrieve 'name' parameter from request
    name = request.GET.get("name") or "world!"
    # Task 5: Render index.html with context variable 'name'
    return render(request, "bookmodule/index.html", {"name": name})

# Task 3: Second view with URL parameter
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

# Task 7: View to display a specific book's details based on bookId
def viewbook(request, bookId):
    # Example books
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    # Find target book based on bookId
    targetBook = book1 if bookId == book1['id'] else book2 if bookId == book2['id'] else None
    return render(request, 'bookmodule/show.html', {'book': targetBook})
