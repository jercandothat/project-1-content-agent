from supabase import create_client, Client
import os

def connect_to_supabase():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)

def store_memory(platform, topic, script, brief):
    supabase = connect_to_supabase()
    data = {
        "platform": platform,
        "topic": topic,
        "script": script[:8000],
        "brief": brief[:8000]
    }
    response = supabase.table("content_memory").insert(data).execute()
    return response