from pydantic import BaseModel


class HistConfigData(BaseModel):
    step: int
    re_route_every_ticks: int
    max_speed_and_length_factor: float
    freshness_cut_off_value: float
    freshness_update_factor: float
    total_car_counter: int
    edge_average_influence: int
    exploration_percentage: float
    route_random_sigma: float
    average_edge_duration_factor: float
    total_complaints: int

    class Config:
        orm_mode = True
