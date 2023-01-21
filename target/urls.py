from django.urls import path
from .views import (
    Home,
    Create,
    Store,
    Show,
    Edit,
    Update,
    Delete,
    ImageUpload,
    DeleteImage,
    FeatureUpload,
    DeleteFeature,
)

urlpatterns = [
    path("", Home, name="admin.properties.index"),
    path("create", Create, name="admin.properties.create"),
    path("store", Store, name="admin.properties.store"),
    path("edit/<int:id>/", Edit, name="admin.properties.edit"),
    path("show/<int:id>/", Show, name="admin.properties.show"),
    path("update/<int:id>/", Update, name="admin.properties.update"),
    path("delete/<int:id>/", Delete, name="admin.properties.delete"),
    path("image-upload", ImageUpload, name="admin.properties.image-upload"),
    path("delete-image/<int:id>/", DeleteImage, name="admin.properties.delete-image"),
    path("feature-upload", FeatureUpload, name="admin.properties.feature-upload"),
    path(
        "delete-feature/<int:id>/",
        DeleteFeature,
        name="admin.properties.delete-feature",
    ),
]
