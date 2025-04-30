# architecture

* sauce-man is services which includes:
    * bot: a discord bot to make discord app bertter to:        
        * Fix Links Previews
        * reverse image search
        * query user messages
        and also:
        * prometheus metrics
        * opentelemetry instrumentation
    * api: a FastAPI to interact with bot
    * bot management dashboard: matain bots via api
    * mcp-server: MCP is an open protocol that standardizes how applications provide context to LLMs.