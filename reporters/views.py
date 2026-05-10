# django imports
from django.conf import settings

# restframework imports
from rest_framework.decorators import api_view
from rest_framework.response import Response

# models import
from .models import Reporter

REPORTER_FILE_PATH = "data/reporters.json"

# create a new user
@api_view(["POST"])
def create_reporter(request):
    payload = request.data

    # get details
    name = payload.get("name")
    email = payload.get("email")
    team = payload.get("team")

    # create new reporter
    try:
        reporter = create_new_reporter(name, email, team)
    except ValueError as e:
        return Response(data={"error": str(e)}, status=400)

    return Response(data=reporter, status=201)

def create_new_reporter(name, email, team):
    file_path = settings.BASE_DIR / REPORTER_FILE_PATH

    reporters = Reporter.read_all(file_path)

    id = Reporter.generate_id(reporters)
    reporter_obj = Reporter(id=id, name=name, email=email, team=team)
    reporter_obj.validate()
    reporters.append(reporter_obj.to_dict())

    Reporter.save_all(file_path, reporters)

    return reporter_obj.to_dict()

# get all the users
@api_view(["GET"])
def get_all_reporters(request):
    file_path = settings.BASE_DIR / REPORTER_FILE_PATH
    reporters = Reporter.read_all(file_path)
    return Response(data=reporters, status=200)

@api_view(["GET"])
def get_reporter_by_id(request):
    file_path = settings.BASE_DIR / REPORTER_FILE_PATH
    reporter_id = request.query_params.get("id")
    reporters = Reporter.read_all(file_path)

    reporter = {}
    for r in reporters:
        if int(reporter_id) == r["id"]:
            reporter = r

    return Response(data=reporter, status=200)
