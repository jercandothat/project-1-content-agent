import streamlit as st
from prompts.youtube import generate_youtube_script
from prompts.tiktok import generate_tiktok_ideas
from prompts.instagram import generate_instagram_post
from briefs.generator import generate_creative_brief

from integrations.notion import push_to_notion
from integrations.slack import send_to_slack
from integrations.sheets import append_to_sheet

st.set_page_config(page_title="Project 1: Content Agent", layout="wide")

st.title("📺 Project 1 – AI Content Creation Agent")

platform = st.selectbox("Select Platform", ["youtube", "tiktok", "instagram"])
topic = st.text_input("Enter Content Topic", "")

st.markdown("## 🔧 Optional Integrations")

col1, col2, col3 = st.columns(3)

with col1:
    use_notion = st.checkbox("Send to Notion")
    notion_token = st.text_input("Notion Token", type="password") if use_notion else ""
    notion_page_id = st.text_input("Notion Page ID") if use_notion else ""

with col2:
    use_slack = st.checkbox("Send to Slack")
    slack_token = st.text_input("Slack Token", type="password") if use_slack else ""
    slack_channel = st.text_input("Slack Channel") if use_slack else ""

with col3:
    use_sheets = st.checkbox("Append to Google Sheets")
    sheet_id = st.text_input("Google Sheet ID") if use_sheets else ""
    creds_file = st.text_input("Path to credentials.json") if use_sheets else ""

if st.button("🚀 Generate Content"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        st.markdown("### 🎬 Script Output")
        if platform == "youtube":
            script = generate_youtube_script(topic)
        elif platform == "tiktok":
            script = generate_tiktok_ideas(topic)
        elif platform == "instagram":
            script = generate_instagram_post(topic)

        st.code(script, language="markdown")

        st.markdown("### 📝 Creative Brief")
        brief = generate_creative_brief(platform, topic, script)
        st.text_area("Creative Brief", value=brief, height=300)

        if use_notion and notion_token and notion_page_id:
            push_to_notion(brief, notion_page_id, notion_token)

        if use_slack and slack_token and slack_channel:
            send_to_slack(slack_channel, f"New {platform} content idea:\n{brief}", slack_token)

        if use_sheets and sheet_id and creds_file:
            append_to_sheet(sheet_id, [platform, topic, script], creds_file)

        from memory.supabase_memory import store_memory
        store_memory(platform, topic, script, brief)
        st.success("✅ Done! All selected integrations triggered.")