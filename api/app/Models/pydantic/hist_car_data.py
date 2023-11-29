from pydantic import BaseModel


class HistCarData(BaseModel):
    step: int
    total_trips: int
    tick_duration: int
    routing_duration: int
    total_trip_overhead_average: float
    total_trip_average: float
    driving_car_counter: int

    class Config:
        orm_mode = True
        # schema_extra = {
        #     "example": {
        #         "step": 0,
        #         "total_trips": 0,
        #         "tick_duration": 0,
        #         "routing_duration": 0,
        #         "total_trip_overhead_average": 0.0,
        #         "total_trip_average": 0.0,
        #         "driving_car_counter": 0
        #     }
        # }
