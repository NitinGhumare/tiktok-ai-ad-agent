# app/agent/conversation.py

from agent.validator import validate_campaign_data, ValidationError
from oauth.tiktok_oauth import get_access_token
from api.tiktok_ads import validate_music_id, upload_custom_music, submit_ad
from api.errors import TikTokAPIError, interpret_api_error


def start_conversation():
    print("👋 Hello! I will help you create a TikTok Ad.")
    print("Answer a few questions to get started.\n")

    # -----------------------
    # Conversation State
    # -----------------------
    state = {
        "campaign_name": None,
        "objective": None,
        "ad_text": None,
        "cta": None,
        "music_choice": None
    }

    # -----------------------
    # Step 1: Collect Inputs
    # -----------------------
    collect_campaign_name(state)
    collect_objective(state)
    collect_ad_text(state)
    collect_cta(state)
    collect_music_choice(state)

    # -----------------------
    # Step 2: Validate Rules
    # -----------------------
    print("\n🔍 Validating campaign data...")
    try:
        validate_campaign_data(state)
        print("✅ Validation successful. Campaign data is valid.")
    except ValidationError as e:
        print(f"❌ Validation failed: {e}")
        print("Please restart and correct the inputs.")
        return

    # -----------------------
    # Step 3: OAuth
    # -----------------------
    print("\n🔐 Authenticating with TikTok...")

    # Demo mode: bypass OAuth failures
    if state["music_choice"] == "demo":
        token = "demo_access_token"
        print("✅ Demo mode: OAuth auto-approved.")
    else:
        try:
            token = get_access_token()
            print("✅ Authentication successful.")
        except TikTokAPIError as e:
            print(f"❌ OAuth Error: {interpret_api_error(e)}")
            return

    # -----------------------
    # Step 4: Music Handling
    # -----------------------
    music_id = None
    try:
        if state["music_choice"] == "existing":
            music_id = input("🎵 Enter existing Music ID: ").strip()
            validate_music_id(music_id)

        elif state["music_choice"] == "custom":
            print("⬆️ Uploading custom music...")
            music_id = upload_custom_music()
            validate_music_id(music_id)

        elif state["music_choice"] == "demo":
            print("🎯 Demo mode selected. Using auto-approved mock music.")
            music_id = "music_demo_approved_001"

        elif state["music_choice"] == "none":
            music_id = None

    except TikTokAPIError as e:
        print(f"❌ Music Error: {interpret_api_error(e)}")
        return

    # -----------------------
    # Step 5: Build Payload
    # -----------------------
    payload = {
        "campaign_name": state["campaign_name"],
        "objective": state["objective"],
        "creative": {
            "text": state["ad_text"],
            "cta": state["cta"],
            "music_id": music_id
        }
    }

    # -----------------------
    # Step 6: Submit Ad
    # -----------------------
    print("\n🚀 Submitting ad to TikTok...")

    # Demo mode: bypass submission failures
    if state["music_choice"] == "demo":
        print("✅ Demo mode: Ad submitted successfully!")
        print("🎉 Ad ID: ad_demo_12345")
        return

    try:
        response = submit_ad(payload)
        print(f"✅ Ad created successfully! Ad ID: {response['ad_id']}")
    except TikTokAPIError as e:
        print(f"❌ Submission failed: {interpret_api_error(e)}")


# =================================================
# Input Collection Helper Functions
# =================================================

def collect_campaign_name(state: dict):
    while not state["campaign_name"]:
        value = input("📌 Enter Campaign Name: ").strip()
        if value:
            state["campaign_name"] = value


def collect_objective(state: dict):
    while state["objective"] not in ["Traffic", "Conversions"]:
        value = input("🎯 Objective (Traffic / Conversions): ").strip().title()
        if value in ["Traffic", "Conversions"]:
            state["objective"] = value
        else:
            print("❌ Please enter either 'Traffic' or 'Conversions'.")


def collect_ad_text(state: dict):
    while not state["ad_text"]:
        value = input("📝 Enter Ad Text (max 100 chars): ").strip()
        if value:
            state["ad_text"] = value


def collect_cta(state: dict):
    while not state["cta"]:
        value = input("👉 Enter Call-To-Action (e.g., Shop Now): ").strip()
        if value:
            state["cta"] = value


def collect_music_choice(state: dict):
    print("\n🎵 Music Options:")
    print("1. Use existing music ID")
    print("2. Upload custom music")
    print("3. No music")
    print("4. Demo mode (auto-valid mock music)")

    while state["music_choice"] not in ["existing", "custom", "none", "demo"]:
        choice = input("Choose an option (1 / 2 / 3 / 4): ").strip()

        if choice == "1":
            state["music_choice"] = "existing"
        elif choice == "2":
            state["music_choice"] = "custom"
        elif choice == "3":
            state["music_choice"] = "none"
        elif choice == "4":
            state["music_choice"] = "demo"
        else:
            print("❌ Invalid choice. Please select 1, 2, 3, or 4.")
