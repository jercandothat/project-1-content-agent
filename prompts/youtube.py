import openai
from config.brand_profile import get_brand_profile
from utils.helpers import format_script_output

def generate_youtube_script(topic: str) -> str:
    brand = get_brand_profile()

    system_prompt = f'''
You are a top-performing YouTube content strategist and scriptwriter.
You specialize in creating high-retention videos that align with the following brand profile:

Brand Tone: {brand['tone']}
Audience: {brand['audience']}
Content Pillars: {', '.join(brand['pillars'])}
'''

    user_prompt = f'''
Topic: "{topic}"

Generate a full YouTube video script including:
1. Title (click-worthy, curiosity-driven)
2. Hook (first 5–10 seconds)
3. Full Script Outline (3–5 segments)
4. Call to Action
5. Optional: Thumbnail idea
'''

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": user_prompt.strip()}
        ],
        temperature=0.85,
        max_tokens=1600
    )

    script_raw = response['choices'][0]['message']['content']
    return format_script_output(script_raw)