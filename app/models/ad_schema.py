from typing import Optional, Literal
from dataclasses import dataclass, asdict


# -------------------------
# Creative Schema
# -------------------------

@dataclass
class Creative:
    text: str
    cta: str
    music_id: Optional[str] = None


# -------------------------
# Ad Campaign Schema
# -------------------------

@dataclass
class AdCampaign:
    campaign_name: str
    objective: Literal["Traffic", "Conversions"]
    creative: Creative

    def to_payload(self) -> dict:
        """
        Converts the dataclass into a dict
        suitable for API submission.
        """
        return asdict(self)
