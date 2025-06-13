import openai
from config.brand_profile import get_brand_profile
from utils.helpers import format_script_output

def generate_tiktok_ideas(topic: str) -> str:
    brand = get_brand_profile()

    system_prompt = f'''
You are a viral TikTok content strategist and hook writer.
You specialize in 15–60 second videos that:
- Grab attention in the first 1.5 seconds
- Align with current trends
- Are on-brand for: {brand['tone']}
- Speak to: {brand['audience']}
- Focus on: {', '.join(brand['pillars'])}
'''

    user_prompt = f'''
Topic: "{topic}"

Create:
1. 3 TikTok video ideas (title + description)
2. 3 viral hooks (first 1–3 seconds of dialogue)
3. Optional trend or sound suggestions
4. 1 sample script (30–45 seconds)
'''

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt.strip()},
            {"role": "user", "content": user_prompt.strip()}
        ],
        temperature=0.9,
        max_tokens=1000
    )

    ideas_raw = response['choices'][0]['message']['content']
    return format_script_output(ideas_raw)