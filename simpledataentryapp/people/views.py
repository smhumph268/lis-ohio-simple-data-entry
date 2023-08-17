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
    confirmed_person = get_object_or_404(Person, pk=person_id)

    # for helping display fields
    person_fields_excluding_id = [field.name for field in Person._meta.fields]

    # an array of arrays to represent all people
    all_people = [
        [getattr(person, field) for field in person_fields_excluding_id]
        for person in Person.objects.all()
    ]

    return render(
        request,
        'people/confirmation.html',
        {
            'confirmed_person': confirmed_person,
            'all_people_arr': all_people,
            'table_headers': person_fields_excluding_id
        }
    )
