from typing import Text
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from .forms import MemoryForm
from .models import Memory
from django.views.generic import CreateView

MEMORIES_PAGE_SIZE = 30


@login_required
def list(request: HttpRequest):
    """
    Display the index page containing the list of all the current user memories.
    """

    user_memories = Memory.objects.filter(owner=request.user)

    paginator = Paginator(user_memories, MEMORIES_PAGE_SIZE)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    return render(request, "memories/list.html", {"memory_page": page})


@login_required
def details(request: HttpRequest, memory_id: Text):
    """
    Display a specific memory details or throw 404 if the memory does not exist.
    """

    memory = get_object_or_404(Memory, pk=memory_id)
    return render(request, "memories/details.html", {"memory": memory})


@login_required
def create(request: HttpRequest):
    """
    Displays the create page for GET request and handles the request for POST request.
    """
    if request.method == "POST":
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MemoryForm()
    return render(request, "memories/create.html", {"form": form})
