"""Outfit2Cart Agent - Main agentic workflow"""
import asyncio
import logging
from typing import Dict, Any, Optional
import config

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


SYSTEM_PROMPT = """You are Outfit2Cart, a shopping automation agent controlling an Android phone using Droidrun.

Your role:
- Analyze screenshots and UI text to understand the current state
- Control apps like Pinterest, Flipkart, and WhatsApp through UI automation
- Help users find fashion items they like on Pinterest and add them to Flipkart cart
- Send WhatsApp notifications with product details

Constraints:
- NEVER attempt to make actual purchases or payments
- ONLY add items to cart, do not proceed to checkout
- NEVER send messages to unknown contacts (only to My Notes or configured recipient)
- If something fails, communicate the failure clearly to the user

Your workflow:
1. OBSERVE: Examine the current screen (should be showing a Pinterest product/outfit)
2. DESCRIBE: Generate a text description of the item you see
3. SEARCH: Open Flipkart and search for the item
4. COMPARE: Find the most similar item
5. ADD TO CART: Open the best match and tap Add to Cart
6. CAPTURE: Note the product details (Title, Price, Rating)
7. NOTIFY: Open WhatsApp and send a summary message

Message format: Outfit2Cart: Found [Title] for Rs[Price] with [Rating]/5 rating. Added to cart!
"""


class Outfit2CartAgent:
    """Main agent for Pinterest -> Flipkart -> WhatsApp workflow"""
    
    def __init__(self):
        self.config = config
        self.initialized = False
    
    async def initialize(self) -> bool:
        """Initialize the agent"""
        try:
            logger.info("Initializing Outfit2Cart agent...")
            logger.info(f"LLM Provider: {config.LLM_PROVIDER}")
            logger.info(f"LLM Model: {config.LLM_MODEL}")
            logger.info(f"Device ID: {config.DEVICE_ID or 'auto-detect'}")
            logger.info(f"WhatsApp Contact: {config.WHATSAPP}")
            self.initialized = True
            return True
        except Exception as e:
            logger.error(f"Failed to initialize agent: {e}")
            return False

