import random
from api.errors import TikTokAPIError

def get_access_token():
    """
    Simulates OAuth token retrieval
    """

    # Random failure simulation
    failure = random.choice([None, "expired", "missing_scope"])

    if failure == "expired":
        raise TikTokAPIError(401, "Access token expired")

    if failure == "missing_scope":
        raise TikTokAPIError(403, "Missing ads permission scope")

    return "mock_access_token_123"
