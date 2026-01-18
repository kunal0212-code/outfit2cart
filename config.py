"""Configuration for Outfit2Cart agent"""
import os
from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "Gemini")  # Gemini, OpenAI, Anthropic
LLM_MODEL = os.getenv("LLM_MODEL", "models/gemini-2.5-pro-preview-05-06")
LLM_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Device Configuration
DEVICE_ID = os.getenv("DEVICE_ID", "")  # Leave empty for auto-detect single device

# App Package Names (configurable for different regions)
PINTEREST_PACKAGE = "com.pinterest"
FLIPKART_PACKAGE = "com.flipkart.android"
WHATSAPP_PACKAGE = "com.whatsapp"



# Agent Configuration
AGENT_TIMEOUT = 120  # seconds
MAX_RETRIES = 2
VISION_ENABLED = True
REASONING_ENABLED = True

# WhatsApp Configuration
WHATSAPP_TARGET_CONTACT = "My Notes"
