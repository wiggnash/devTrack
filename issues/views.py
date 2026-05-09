import json
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response

from .models import Reporter, Issue

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
    file_path = settings.BASE_DIR/REPORTER_FILE_PATH

    # read data from file
    with open(file_path, "r") as file:
        reporters = json.load(file)

    id = len(reporters) + 1
    reporter_obj = Reporter(
        id=id,
        name=name,
        email=email,
        team=team
    )
    reporter_obj.validate()
    reporters.append(reporter_obj.__dict__)

    # write the data to the file
    with open(file_path, "w") as file:
        json.dump(reporters, file)

    return reporter_obj.__dict__

# get all the users
# get user by id
