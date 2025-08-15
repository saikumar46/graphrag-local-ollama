encoding_model: cl100k_base
skip_workflows: []
llm:
    api_key: ${GRAPHRAG_API_KEY}
    type: openai_chat # or azure_openai_chat
    model: llama3
    model_supports_json: true 

# max_tokens: 4000

# request_timeout: 180.0
    api_base: http://localhost:11434/v1