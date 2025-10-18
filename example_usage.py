"""
Example: Using xml_extractor in your experiment script.
"""

from xml_extractor import extract_from_xml, format_article_for_llm


# Load an article
article = extract_from_xml("Annotated_Dataset/text001.xml")

# Get the text ready for LLM
text_for_llm = format_article_for_llm(article)

# Now you can use it with your prompt
baseline_prompt = """You are a genre analyst..."""  # Your prompt from the document

full_prompt = baseline_prompt + "\n\n" + text_for_llm

print("Ready to send to API:")
print(f"- Article: {article['article_id']}")
print(f"- Sentences: {len(article['sentences'])}")
print(f"- Prompt length: {len(full_prompt)} characters")
print("- Prompt preview:" + full_prompt)
