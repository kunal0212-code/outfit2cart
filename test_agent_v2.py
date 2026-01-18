"""Test script for Outfit2Cart Agent"""
import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import config
from agent.outfit2cart_agent import Outfit2CartAgent


async def test_agent():
    print("\n" + "="*70)
    print(" OUTFIT2CART AGENT - ACTUAL DEVICE TEST")
    print("="*70)
    print("Provider: " + str(config.LLM_PROVIDER))
    print("Model: " + str(config.LLM_MODEL))
    print("Device ID: " + str(config.DEVICE_ID or 'auto-detect'))
    print("WhatsApp Contact: " + str(config.WHATSAPP_TARGET_CONTACT))
    print("Vision Enabled: " + str(config.VISION_ENABLED))
    print("Reasoning Enabled: " + str(config.REASONING_ENABLED))
    print("="*70)
    
    agent = Outfit2CartAgent()
    
    print("\n[1/2] Initializing agent...")
    try:
        init_result = await agent.initialize()
        
        if not init_result:
            print("Failed to initialize agent")
            return {"success": False, "error": "Initialization returned False"}
        
        print("Agent initialized successfully")
    except Exception as e:
        print("Error during initialization: " + str(e))
        return {"success": False, "error": str(e)}
    
    print("\n[2/2] Running workflow...")
    print("-" * 70)
    
    try:
        result = await agent.run_workflow()
    except Exception as e:
        print("Error during workflow: " + str(e))
        return {"success": False, "error": str(e)}
    
    print("-" * 70)
    
    if result is None:
        print("Workflow returned None")
        return {"success": False, "error": "Workflow returned None"}
    
    print("\nWORKFLOW RESULTS:")
    print("   Status: " + str(result.get('status')))
    print("   Message: " + str(result.get('message')))
    if result.get('provider'):
        print("   Provider Used: " + str(result.get('provider')))
    if result.get('contact'):
        print("   WhatsApp Contact: " + str(result.get('contact')))
    
    print("\n" + "="*70)
    if result.get('success'):
        print("Workflow completed successfully")
    else:
        print("Workflow failed")