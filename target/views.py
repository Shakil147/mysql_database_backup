from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import (
    Target,
    TargetForm,
)

from core.models import BackupHistory
from django.contrib import messages
from django.utils.text import slugify


@login_required(login_url="/admin/login")  # Check login
def Home(request):
    context = {
        "targets": Target.objects.all().order_by("-priority"),
    }
    return render(request, "backend/targets/index.html", context)


@login_required(login_url="/admin/login")
def Create(request):
    context = {}
    return render(request, "backend/targets/add.html", context)


@login_required(login_url="/admin/login")
def Store(request):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = TargetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            if request.POST.get("submit") == "s&c":
                return HttpResponseRedirect(url)
            else:
                return HttpResponseRedirect("/admin/targets")
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
@login_required(login_url="/admin/login")
def Edit(request, id):
    context = {
        "target": Target.objects.get(id=id),
    }
    return render(request, "backend/targets/edit.html", context)


@login_required(login_url="/admin/login")
def Update(request, id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        old_data = Target.objects.get(id=id)
        form = TargetForm(request.POST, request.FILES, instance=old_data)
        if form.is_valid():
            form.save()
            data = Target.objects.get(id=id)
            data.save()
            messages.success(request, "Updated Successfully")
            if request.POST.get("submit") == "s&c":
                return HttpResponseRedirect(url)
            else:
                return HttpResponseRedirect("/admin/targets")
        else:
            messages.warning(request, "Somthing Went wrong ! Try Again")
    else:
        messages.warning(request, "Somthing Went wrong ! Try Again")
    return HttpResponseRedirect(url)


@login_required(login_url="/admin/login")
def Delete(request, id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        data = Target.objects.get(id=id)
        if data:
            data.delete()
            messages.success(request, "Removed Successfully")
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, "Somthing Went wrong ! Try Again")
    else:
        messages.warning(request, "Somthing Went wrong ! Try Again")
    return HttpResponseRedirect(url)


@login_required(login_url="/admin/login")
def BackupHistry(request, id):
    context = {
        "target": Target.objects.get(id=id),
        "backups": BackupHistory.objects.all().filter(target_id=id).order_by("-created_at"),
    }
    return render(request, "backend/targets/backups.html", context)
