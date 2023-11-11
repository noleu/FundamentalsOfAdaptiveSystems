from fastapi import APIRouter
import json


router = APIRouter(
    prefix="/adaption_options",
    tags=["adaption_options"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def adaption_options_endpoint():

    return {"options": ["routeRandomSigma", "explorationPercentage", "maxSpeedAndLengthFactor",
                        "averageEdgeDurationFactor", "freshnessUpdateFactor", "freshnessCutOffValue",
                        "reRouteEveryTicks", "totalCarCounter", "edgeAverageInfluence"]}
