class OpenRouterPromptCachingClient:
    def check_cache(self, prompt_text: str) -> dict:
        return {"is_cached": len(prompt_text) > 500, "discounted_rate": 0.5}