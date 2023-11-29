from sqlalchemy import Column, Integer, Float

from api.app.database import Base

class Historic_Config_Data(Base):
    __tablename__ = "historic_config_data"

    step = Column(Integer, primary_key=True, index=True)
    re_route_every_ticks = Column(Integer)
    max_speed_and_length_factor = Column(Float)
    freshness_cut_off_value = Column(Float)
    freshness_update_factor = Column(Float)
    total_car_counter = Column(Integer)
    edge_average_influence = Column(Integer)
    exploration_percentage = Column(Float)
    route_random_sigma = Column(Float)
    average_edge_duration_factor = Column(Float)
    total_complaints = Column(Integer)





