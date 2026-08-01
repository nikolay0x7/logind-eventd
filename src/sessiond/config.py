from dataclasses import dataclass
@dataclass(slots=True)
class Config:
    delay_seconds:int=1200
    action:str="suspend"
