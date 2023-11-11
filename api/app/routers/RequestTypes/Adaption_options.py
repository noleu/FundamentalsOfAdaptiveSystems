from pydantic import BaseModel


class AdaptionOptions(BaseModel):
    Knobs: Knobs
    totalCarCounter: int
    edgeAverageInfluence: float


class Knobs(BaseModel):
    routeRandomSigma: float
    explorationPercentage: float
    maxSpeedAndLengthFactor: int
    averageEdgeDurationFactor: int
    freshnessUpdateFactor: int
    freshnessCutOffValue: int
    reRouteEveryTicks: int
