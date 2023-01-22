from django.urls import path
from .views import (
    Home,
    Create,
    Store,
    # Show,
    Edit,
    Update,
    Delete,
    BackupHistry,
)

urlpatterns = [
    path("", Home, name="admin.targets.index"),
    path("create", Create, name="admin.targets.create"),
    path("store", Store, name="admin.targets.store"),
    path("edit/<int:id>/", Edit, name="admin.targets.edit"),
    #path("show/<int:id>/", Show, name="admin.targets.show"),
    path("update/<int:id>/", Update, name="admin.targets.update"),
    path("delete/<int:id>/", Delete, name="admin.targets.delete"),
    path("backups/<int:id>/", BackupHistry, name="admin.targets.backups"),
]
