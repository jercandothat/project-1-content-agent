# Project 1: AI Content Agent

This is a production-ready, GPT-powered AI content system that helps automate research, ideation, scripting, and creative briefs for YouTube, TikTok, and Instagram.

Built for content creators, marketers, and teams who want to streamline content workflows using AI.

---

## 🔧 Features

- 🎯 Platform-specific content generation
  - YouTube long-form scripts
  - TikTok hooks + short-form viral ideas
  - Instagram captions, reels, and trends
- 🧠 Brand tone + audience config
- 📤 One-click export to:
  - Notion
  - Slack
  - Google Sheets
- 👥 Multi-user login system (Supabase Auth)
- 🚦 Usage limits based on user role (free, pro, admin)
- 💾 Persistent content memory via Supabase DB
- 🌐 Streamlit Web UI for easy access

---

## 🗂 Folder Structure

```
├── app.py                  # Streamlit frontend
├── main.py                 # CLI agent
├── prompts/                # YouTube, TikTok, IG logic
├── briefs/                 # Creative brief builder
├── config/                 # Brand tone config
├── integrations/           # Notion, Slack, Sheets APIs
├── memory/                 # Supabase memory layer
├── auth/                   # User login, limits, sessions
├── utils/                  # Shared helpers
├── requirements.txt        # Python dependencies
├── .env.example            # Example env file for secrets
├── README.md               # This file
├── LICENSE                 # MIT License
```

---

## 🚀 Setup & Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Or run from CLI:

```bash
python main.py --platform youtube --topic "How to grow a YouTube channel in 2025"
```

---

## 🔐 Environment Variables

You'll need a `.env` file or system-level env vars for:

- `OPENAI_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `NOTION_TOKEN`
- `SLACK_TOKEN`

See `.env.example` for reference.

---

## 📄 License

MIT — see `LICENSE` file.