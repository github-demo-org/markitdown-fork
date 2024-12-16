from markitdown import MarkItDown

markitdown = MarkItDown()
# result = markitdown.convert("https://techcommunity.microsoft.com/blog/azure-ai-services-blog/prep-your-data-for-rag-with-azure-ai-search-content-layout-markdown-parsing--imp/4303538")
result = markitdown.convert("https://learn.microsoft.com/ja-jp/azure/ai-services/agents/quotas-limits?view=azure-python-preview")
print(result.text_content)