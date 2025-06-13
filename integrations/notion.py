from notion_client import Client

def push_to_notion(content: str, page_id: str, notion_token: str):
    notion = Client(auth=notion_token)

    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": content[:2000]}}]
                }
            }
        ]
    )
    print(f"[SUCCESS] Content pushed to Notion page {page_id}")