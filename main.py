import argparse
from prompts.youtube import generate_youtube_script
from prompts.tiktok import generate_tiktok_ideas
from prompts.instagram import generate_instagram_post
from briefs.generator import generate_creative_brief

# Integration imports
from integrations.notion import push_to_notion
from integrations.slack import send_to_slack
from integrations.sheets import append_to_sheet

PLATFORMS = ['youtube', 'tiktok', 'instagram']

def run_agent(platform, topic, notion_token=None, notion_page_id=None,
              slack_token=None, slack_channel=None,
              sheet_id=None, creds_file=None):

    if platform not in PLATFORMS:
        raise ValueError(f"Unsupported platform '{platform}'. Choose from: {PLATFORMS}")

    print(f"\n🧠 Generating content for platform: {platform.upper()}")

    if platform == 'youtube':
        script = generate_youtube_script(topic)
    elif platform == 'tiktok':
        script = generate_tiktok_ideas(topic)
    elif platform == 'instagram':
        script = generate_instagram_post(topic)

    brief = generate_creative_brief(platform, topic, script)

    print("\n🎬 Content Output:\n")
    print(script)
    print("\n📝 Creative Brief:\n")
    print(brief)

    # Optional: Push to integrations
    if notion_token and notion_page_id:
        push_to_notion(brief, notion_page_id, notion_token)

    if slack_token and slack_channel:
        send_to_slack(slack_channel, f"New {platform} content idea:\n{brief}", slack_token)

    if sheet_id and creds_file:
        append_to_sheet(sheet_id, [platform, topic, script], creds_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the GPT Content Agent with integrations.")
    parser.add_argument('--platform', type=str, required=True, help="Platform: youtube, tiktok, instagram")
    parser.add_argument('--topic', type=str, required=True, help="Content topic or idea")
    parser.add_argument('--notion_token', type=str, help="Notion Integration Token")
    parser.add_argument('--notion_page_id', type=str, help="Target Notion Page ID")
    parser.add_argument('--slack_token', type=str, help="Slack Bot Token")
    parser.add_argument('--slack_channel', type=str, help="Slack Channel ID")
    parser.add_argument('--sheet_id', type=str, help="Google Sheet ID")
    parser.add_argument('--creds_file', type=str, help="Path to Google Service Account credentials.json")

    args = parser.parse_args()

    run_agent(
        platform=args.platform.lower(),
        topic=args.topic,
        notion_token=args.notion_token,
        notion_page_id=args.notion_page_id,
        slack_token=args.slack_token,
        slack_channel=args.slack_channel,
        sheet_id=args.sheet_id,
        creds_file=args.creds_file
    )