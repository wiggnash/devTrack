from datetime import datetime
from devtrack.models import BaseEntity

class IssueStatus:
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class IssuePriority:
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Issue(BaseEntity):
    ISSUE_STATUSES = [IssueStatus.OPEN, IssueStatus.IN_PROGRESS, IssueStatus.RESOLVED, IssueStatus.CLOSED]
    ISSUE_PRIORITIES = [IssuePriority.LOW, IssuePriority.MEDIUM, IssuePriority.HIGH, IssuePriority.CRITICAL]

    def __init__(self, id, title, description, status, priority, reporter_id):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.reporter_id = reporter_id
        self.created_at = datetime.now().isoformat()

    def validate(self):
        if not self.title:
            raise ValueError("Title is required for the Issue")

        if self.status not in self.ISSUE_STATUSES:
            raise ValueError("Give Correct Status")

        if self.priority not in self.ISSUE_PRIORITIES:
            raise ValueError("Give Correct Priority")

    def describe(self):
            return f"{self.title} [{self.priority}]"

class CriticalIssue(Issue):
    def describe(self):
        return f"[URGENT] {self.title} — needs immediate attention"

class LowPriorityIssue(Issue):
    def describe(self):
        return f"{self.title} — low priority, handle when free"
