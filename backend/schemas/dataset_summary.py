from pydantic import BaseModel
from typing import Dict, List, Optional

class FeatureInfo(BaseModel):
    missing: str
    type: str
    range: Optional[str] = None
    categories: Optional[List[str]] = None
    target: Optional[bool] = False

class DatasetSummary(BaseModel):
    dataset_name: str
    num_rows: int
    features: Dict[str, FeatureInfo]
    time_span: str
