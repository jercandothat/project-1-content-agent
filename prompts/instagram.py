import openai
from config.brand_profile import get_brand_profile
from utils.helpers import format_script_output

def generate_instagram_post(topic: str) -> str:
    brand = get_brand_profile()

    system_prompt = f'''
You are a top Instagram content strategist and copywriter.
You craft compelling Instagram Reels scripts and post captions that:
- Match the tone: {brand['tone']}
- Speak to: {brand['audience']}
- Support content pillars: {', '.join(brand['pillars'])}
- Align with visual-first, short-form storytelling
'''

    user_prompt = f'''
Topic: "{topic}"

Deliver:
1. 2 Instagram Reel concepts (title + short description)
2. 1 suggested voiceover script for a 30-second Reel
3. 2 engaging post captions with emoji, CTAs, and hashtags
'''

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": user_prompt.strip()}
        ],
        temperature=0.85,
        max_tokens=1200
    )

    ig_raw = response['choices'][0]['message']['content']
    return format_script_output(ig_raw)