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
