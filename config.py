"""Configuration for Outfit2Cart agent"""

import os
from dotenv import load_dotenv

load_dotenv()

# ===== LLM Configuration =====
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "Gemini")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.5-pro-preview-05-06")
LLM_API_KEY = os.getenv("GEMINI_API_KEY")

# Validate API key is set
if not LLM_API_KEY:
    raise EnvironmentError(
        "❌ CRITICAL: GEMINI_API_KEY not set. Set it in .env or environment."
    )

# ===== Device Configuration =====
DEVICE_ID = os.getenv("DEVICE_ID", None)

# ===== App Package Names =====
PINTEREST_PACKAGE = "com.pinterest"
FLIPKART_PACKAGE = "com.flipkart.android"
WHATSAPP_PACKAGE = "com.whatsapp"

# ===== Agent Configuration =====
AGENT_TIMEOUT = 120
MAX_RETRIES = 2
VISION_ENABLED = True
REASONING_ENABLED = True

# ===== WhatsApp Configuration =====
WHATSAPP_TARGET_CONTACT = "My Notes"

# ===== Droidrun Configuration =====
DROIDRUN_HOST = os.getenv("DROIDRUN_HOST", "localhost")
DROIDRUN_PORT = int(os.getenv("DROIDRUN_PORT", "5037"))

DROIDRUN_CONFIG = {
    "device_host": DROIDRUN_HOST,
    "device_port": DROIDRUN_PORT,
    "enable_logging": True,
    "timeout": 30,
    "retry_attempts": 3,
    
    # LLM settings for Droidrun
    "llm_provider": LLM_PROVIDER,
    "llm_model": LLM_MODEL,
    "llm_api_key": LLM_API_KEY,
}
