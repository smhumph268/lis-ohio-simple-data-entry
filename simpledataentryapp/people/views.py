from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import NewPersonForm
from .models import Person


def new_user(request):
    """
    Allows user to add a new person
    """
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NewPersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()

            # direct user to confirmation page
            return HttpResponseRedirect(reverse('people:confirmation', kwargs={'person_id': form.instance.id}))
        else:
            return render(request, 'people/new_person.html', {'form': form})
    else:
        form = NewPersonForm()
        return render(request, 'people/new_person.html', {'form': form})


def confirmation(request, person_id):
    """
    Confirmation page that displays details of the created person and a table of all other people in the database
    """
    get_object_or_404(Person, pk=person_id)
    return render(request, 'people/confirmation.html', {'person_id': person_id})
