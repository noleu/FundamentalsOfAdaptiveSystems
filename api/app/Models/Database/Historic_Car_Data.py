from sqlalchemy import Column, Integer, Float
from api.app.database import Base

class Historic_Config_Data(Base):
    __tablename__ = "historic_config_data"

    step = Column(Integer, primary_key=True, index=True)
    total_trips = Column(Integer)
    tick_duration = Column(Integer)
    routing_duration = Column(Integer)
    total_trip_overhead_average = Column(Float)
    total_trip_average = Column(Float)
    driving_car_counter = Column(Integer)