from fastapi import APIRouter
from sqlalchemy.orm import Session

from api.app.Models.Database import Historic_Car_Data
from api.app.Models.pydantic.hist_car_data import HistCarData

router = APIRouter(
    prefix="/monitor",
    tags=["monitor"],
    responses={404: {"description": "Not found"}},
)

# https://fastapi.tiangolo.com/tutorial/sql-databases/
@router.get("/car", response_model=HistCarData)
def get_historic_car_data(db: Session, skip: int = 0, limit: int = 100):

    return db.query(Historic_Car_Data).order_by(Historic_Car_Data..offset(skip).limit(limit).all(


@router.get("/car/total_trips")
def get_historic_car_total_trips_data(db: Session, skip: int = 0, limit: int = 100):

    return db.query().with_entities(Historic_Car_Data.total_trips, Historic_Car_Data.steps)
            .order_by(Historic_Car_Data.steps).offset(skip).limit(limit).all()


@router.get("/config")
def get_historic_config_data():
    pass