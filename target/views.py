from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import (
    Property,
    PropertyForm,
    PropertyImage,
    PropertyImageForm,
    PropertyFeature,
    PropertyFeatureForm,
)
from django.contrib import messages
from django.utils.text import slugify
from location.models import Location
from type.models import Type
from room.models import Room
from ShebaProject.models import Project


@login_required(login_url="/admin/login")  # Check login
def Home(request):
    context = {
        "properties": Property.objects.all().order_by("-xsort"),
    }
    return render(request, "backend/properties/index.html", context)


@login_required(login_url="/admin/login")
def Create(request):
    context = {
        "projects": Project.objects.all().filter(status=1).order_by("-xsort"),
        "locations": Location.objects.all().filter(status=1).order_by("-xsort"),
        "types": Type.objects.all().filter(status=1).order_by("-xsort"),
        "rooms": Room.objects.all().filter(status=1).order_by("-xsort"),
    }
    return render(request, "backend/properties/add.html", context)


@login_required(login_url="/admin/login")
def Store(request):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            if request.POST.get("submit") == "s&c":
                return HttpResponseRedirect(url)
            else:
                return HttpResponseRedirect("/admin/properties")
        else:
            context = {
                "form": form,
            }
            messages.warning(request, "Somthing Went wrong ! Try Again")
            return HttpResponseRedirect(url, context)
    else:
        messages.warning(request, "Somthing Went wrong ! Try Again")
    return HttpResponseRedirect(url)


@login_required(login_url="/admin/login")
def Show(request, id):
    data = Property.objects.get(id=id)
    images = PropertyImage.objects.filter(property=id)
    context = {
        "property": data,
        "images": images,
    }
    return render(request, "backend/properties/show.html", context)


@login_required(login_url="/admin/login")
def Edit(request, id):
    context = {
        "property": Property.objects.get(id=id),
        "projects": Project.objects.all().filter(status=1).order_by("-xsort"),
        "locations": Location.objects.all().filter(status=1).order_by("-xsort"),
        "types": Type.objects.all().filter(status=1).order_by("-xsort"),
        "rooms": Room.objects.all().filter(status=1).order_by("-xsort"),
    }
    return render(request, "backend/properties/edit.html", context)


@login_required(login_url="/admin/login")
def Update(request, id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        old_data = Property.objects.get(id=id)
        old_image = old_data.image
        old_image_2 = old_data.image_2

        form = PropertyForm(request.POST, request.FILES, instance=old_data)
        if form.is_valid():
            form.save()
            data = Property.objects.get(id=id)
            data.save()
            if old_image != data.image:
                old_image.delete(save=False)
            if old_image_2 != data.image_2:
                old_image_2.delete(save=False)
            messages.success(request, "Updated Successfully")
            if request.POST.get("submit") == "s&c":
                return HttpResponseRedirect(url)
            else:
                return HttpResponseRedirect("/admin/properties")
        else:
            messages.warning(request, "Somthing Went wrong ! Try Again")
    else:
        messages.warning(request, "Somthing Went wrong ! Try Again")
    return HttpResponseRedirect(url)


@login_required(login_url="/admin/login")
def Delete(request, id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        data = Property.objects.get(id=id)
        if data:
            data.image.delete()
            data.image_2.delete()
            data.delete()
            messages.success(request, "Removed Successfully")
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, "Somthing Went wrong ! Try Again")
    else:
        messages.warning(request, "Somthing Went wrong ! Try Again")
    return HttpResponseRedirect(url)


@login_required(login_url="/admin/login")
def ImageUpload(request):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = PropertyImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, "The request is not valid.")
    else:
        messages.warning(request, "Somthing Went wrong ! Try Again")
    return HttpResponseRedirect(url)


@login_required(login_url="/admin/login")
def DeleteImage(request, id):
    url = request.META.get("HTTP_REFERER")
    data = PropertyImage.objects.get(id=id)
    if data:
        data.image.delete()
        data.delete()
        messages.success(request, "Removed Successfully")
        return HttpResponseRedirect(url)
    else:
        messages.warning(request, "Somthing Went wrong ! Try Again")


@login_required(login_url="/admin/login")
def FeatureUpload(request):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = PropertyFeatureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, "The request is not valid.")
    else:
        messages.warning(request, "Somthing Went wrong ! Try Again")
    return HttpResponseRedirect(url)


@login_required(login_url="/admin/login")
def DeleteFeature(request, id):
    url = request.META.get("HTTP_REFERER")
    data = PropertyFeature.objects.get(id=id)
    if data:
        data.image.delete()
        data.delete()
        messages.success(request, "Removed Successfully")
        return HttpResponseRedirect(url)
    else:
        messages.warning(request, "Somthing Went wrong ! Try Again")
