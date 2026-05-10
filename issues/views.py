# django imports
from django.conf import settings

# restframework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

# models import
from .models import Issue, CriticalIssue, LowPriorityIssue, IssueStatus, IssuePriority

ISSUES_FILE_PATH = "data/issues.json"

@api_view(["POST"])
def create_issue(request):
    payload = request.data

    title = payload.get("title")
    description = payload.get("description")
    status = payload.get("status")
    priority = payload.get("priority")
    reporter_id = payload.get("reporter_id")

    try:
        issue = create_new_issue(title, description, status, priority, reporter_id)
    except ValueError as e:
        return Response(data={"error": str(e)}, status=400)

    return Response(data=issue, status=201)

def create_new_issue(title, description, status, priority, reporter_id):
    file_path = settings.BASE_DIR / ISSUES_FILE_PATH

    issues = Issue.read_all(file_path)

    id = Issue.generate_id(issues)

    # set default values
    if not status:
        status = IssueStatus.OPEN

    if not priority:
        priority = IssuePriority.LOW

    if priority == IssuePriority.CRITICAL:
        issue_obj = CriticalIssue(
            id=id,
            title=title,
            description=description,
            status=status,
            priority=priority,
            reporter_id=reporter_id
        )
    elif priority == IssuePriority.LOW:
        issue_obj = LowPriorityIssue(
            id=id,
            title=title,
            description=description,
            status=status,
            priority=priority,
            reporter_id=reporter_id
        )
    else:
        issue_obj = Issue(
            id=id,
            title=title,
            description=description,
            status=status,
            priority=priority,
            reporter_id=reporter_id
        )
    issue_obj.validate()
    issue_dict = issue_obj.to_dict()

    issues.append(issue_dict)
    Issue.save_all(file_path, issues)

    issue_dict["message"] = issue_obj.describe()
    return issue_dict

@api_view(["GET"])
def get_all_issues(request):
    file_path = settings.BASE_DIR / ISSUES_FILE_PATH
    issues = Issue.read_all(file_path)
    return Response(data=issues, status=200)

@api_view(["GET"])
def get_issue_by_id(request):
    file_path = settings.BASE_DIR / ISSUES_FILE_PATH
    issue_id = request.query_params.get("id")
    issues = Issue.read_all(file_path)

    issue = None
    for i in issues:
        if int(issue_id) == i["id"]:
            issue = i

    if not issue:
        return Response(data={"error": "Issue not found"}, status=404)

    return Response(data=issue, status=200)
