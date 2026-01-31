class TikTokAPIError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(message)


def interpret_api_error(error: TikTokAPIError) -> str:
    """
    Converts raw API errors into human-readable explanations
    """

    if error.code == 401:
        return "Authentication failed. Your access token is invalid or expired. Please re-authenticate."

    if error.code == 403:
        return "This action is not allowed in your region (geo-restriction)."

    if error.code == 400:
        return f"Bad request: {error.message}"

    return "An unknown error occurred while communicating with TikTok Ads API."
