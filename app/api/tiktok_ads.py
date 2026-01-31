import random
from api.errors import TikTokAPIError

def validate_music_id(music_id: str):
    """
    Simulates music ID validation
    """

    if music_id.startswith("invalid"):
        raise TikTokAPIError(400, "Music ID is not approved for ads")

    return True


def upload_custom_music():
    """
    Simulates music upload
    """

    return f"music_{random.randint(1000,9999)}"


def submit_ad(payload: dict):
    """
    Simulates ad submission
    """

    failure = random.choice([None, "geo", "auth"])

    if failure == "geo":
        raise TikTokAPIError(403, "Geo restriction")

    if failure == "auth":
        raise TikTokAPIError(401, "Invalid token")

    return {
        "status": "SUCCESS",
        "ad_id": f"ad_{random.randint(10000,99999)}"
    }
