from fastapi import APIRouter
import json


router = APIRouter(
    prefix="/adaptation_options",
    tags=["adaptation_options"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def adaptation_options_endpoint():

    return {"options": {"route_random_sigma":           {"start": 0.0,"stop": 1.0,"domain": "continuous"} , 
                        "exploration_percentage":       {"start": 0.0,"stop": 1.0,"domain": "continuous"}, 
                        "max_speed_and_length_factor":  {"start": 0.0,"stop": 2**31-1,"domain": "continuous"},
                        "average_edge_duration_factor": {"start": 0.0,"stop": 2**31-1,"domain": "continuous"}, 
                        "freshness_update_factor":      {"start": 1.0,"stop": 2**31-1,"domain": "continuous"}, 
                        "freshness_cut_off_value":      {"start": 1.0,"stop": 2**31-1,"domain": "continuous"},
                        "re_route_every_ticks":         {"start": 1,"stop": 2**31-1,"domain": "discrete"}, 
                        "total_car_counter":            {"start": 10,"stop": 2**31-1,"domain": "discrete"}, 
                        "edge_average_influence":       {"start": 0.0,"stop": 1.0,"domain": "continuous"}}}
