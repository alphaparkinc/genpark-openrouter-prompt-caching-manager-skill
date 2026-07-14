from client import OpenRouterPromptCachingClient
client = OpenRouterPromptCachingClient()
print(client.check_cache("A"*600))