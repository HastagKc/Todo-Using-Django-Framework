from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo


# Define the view function for the homepage
def home(request):
    # Fetch all Todo objects from the database
    todos = Todo.objects.all()
    # Create a dictionary containing the fetched todos
    content = {"todos": todos}
    # Render the 'index.html' template with the todos passed in the context
    return render(request, "index.html", context=content)


# defining the view function for the createpage
def create(request):
    if request.method == "POST":
        # print(request.POST)
        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.get("status")
        Todo.objects.create(name=name, description=description, status=status)
        return redirect("home")
    return render(request, "create.html")


# defining the view for edit page
def edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get("name")
        des = request.POST.get("description")
        status = request.POST.get("status")
        todo.name = name
        todo.description = des
        todo.status = status
        todo.save()
        return redirect("home")
    content = {"todo": todo}
    return render(request, "edit.html", context=content)


from django.contrib import messages


def delete(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        messages.success(request, "Todo item deleted successfully.")
    except Todo.DoesNotExist:
        messages.error(request, "Todo item does not exist.")

    return redirect("home")
