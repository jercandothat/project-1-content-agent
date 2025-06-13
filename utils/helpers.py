def format_script_output(script_text: str) -> str:
    cleaned = script_text.replace("**", "").replace("###", "").strip()
    return "\n".join([line.strip() for line in cleaned.splitlines() if line.strip()])

def get_brand_profile():
    import json
    with open('config/brand_profile.json', 'r') as f:
        return json.load(f)