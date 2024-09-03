from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature = 0,
    groq_api_key = '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',
    model_name = "llama-3.1-70b-versatile"
)

response = llm.invoke("The first person to landon the moon was ....")
print(response.content)