from django.urls import path
from issues.views import create_issue, get_all_issues, get_issue_by_id

urlpatterns = [
    path("create/", create_issue),
    path("all/", get_all_issues),
    path("", get_issue_by_id),
]
