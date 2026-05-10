from django.urls import path
from reporters.views import create_reporter, get_all_reporters, get_reporter_by_id

urlpatterns = [
    path("", get_reporter_by_id),
    path("create/", create_reporter),
    path("all/", get_all_reporters),
]
