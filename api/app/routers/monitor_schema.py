from fastapi import APIRouter
import json


router = APIRouter(
    prefix="/monitor_schema",
    tags=["monitor_schema"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def monitor_schema():
    data = None

    with open("/code/specifications/monitor_schema.json") as json_file:
        data = json.load(json_file)
        print(data)

    return data
