class ValidationError(Exception):
    """Raised when business rules are violated."""
    pass
def validate_campaign_data(state: dict):
    """
    Enforces all business rules before submission.
    Raises ValidationError if any rule is violated.
    """

    # Campaign name
    if not state.get("campaign_name") or len(state["campaign_name"]) < 3:
        raise ValidationError("Campaign name must be at least 3 characters long.")

    # Objective
    if state.get("objective") not in ["Traffic", "Conversions"]:
        raise ValidationError("Objective must be either Traffic or Conversions.")

    # Ad text
    if not state.get("ad_text"):
        raise ValidationError("Ad text is required.")
    if len(state["ad_text"]) > 100:
        raise ValidationError("Ad text must be 100 characters or less.")

    # CTA
    if not state.get("cta"):
        raise ValidationError("CTA (Call-To-Action) is required.")

    # 🎵 MUSIC LOGIC (CRITICAL)
    music_choice = state.get("music_choice")
    objective = state.get("objective")

    if objective == "Conversions" and music_choice == "none":
        raise ValidationError(
            "Music is required for Conversions campaigns. "
            "Please choose existing or custom music."
        )

    # If we reach here, data is valid
    return True
