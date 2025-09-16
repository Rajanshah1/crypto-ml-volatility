from pydantic import BaseModel
from typing import Optional

class DataConfig(BaseModel):
    default_ticker: str = "BTC-USD"
    start: str = "2018-01-01"
    end: Optional[str] = None

class AppConfig(BaseModel):
    default_source: str = "sample"
    lookback_days: int = 365

class RiskConfig(BaseModel):
    var_confidence: float = 0.95

class Settings(BaseModel):
    data: DataConfig = DataConfig()
    app: AppConfig = AppConfig()
    risk: RiskConfig = RiskConfig()
