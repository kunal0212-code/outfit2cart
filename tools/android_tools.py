"""Android automation tools for Outfit2Cart using Droidrun"""

import logging
from typing import Optional, Dict, Any

from droidrun import DroidAgent, AdbTools  # use actual public classes
from config import DROIDRUN_CONFIG

# Setup logging
logger = logging.getLogger(__name__)


class AndroidToolsWithDroidrun:
    """Wrapper for Droidrun Android device automation"""

    def __init__(self) -> None:
        self.agent: Optional[DroidAgent] = None
        self.tools: Optional[AdbTools] = None

        try:
            # AdbTools handles low-level ADB/device interaction.
            self.tools = AdbTools()
            logger.info("✅ Droidrun AdbTools initialized successfully")

            # High-level agent that will run goals on the device.
            self.agent = DroidAgent(
                goal=DROIDRUN_CONFIG.get(
                    "default_goal", "Control the Android device"
                ),
                llms={
                    "primary": {
                        "provider": DROIDRUN_CONFIG.get("llm_provider"),
                        "model": DROIDRUN_CONFIG.get("llm_model"),
                        "api_key": DROIDRUN_CONFIG.get("llm_api_key"),
                    }
                },
            )

            logger.info("✅ Droidrun agent initialized successfully")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Droidrun: {e}")
            self.agent = None
            self.tools = None

    def connect_to_device(self) -> bool:
        """Check that Droidrun is ready to control a device.

        Returns:
            bool: True if initialization is OK, False otherwise.
        """
        if self.agent is None or self.tools is None:
            logger.error("Droidrun not initialized")
            return False

        # Agent + AdbTools setup succeeded; actual ADB connection
        # is handled internally when running goals/commands.
        logger.info("✅ Droidrun is ready to control the Android device")
        return True

    def disconnect(self) -> bool:
        """Disconnect from Android device.

        Droidrun does not expose a simple 'disconnect' like AndroidDevice,
        so this method just clears local references.
        """
        try:
            self.agent = None
            self.tools = None
            logger.info("✅ Droidrun references cleared (logical disconnect)")
            return True
        except Exception as e:
            logger.error(f"❌ Disconnection failed: {e}")
            return False

    def get_device_info(self) -> Optional[Dict[str, Any]]:
        """Get basic device information via ADB tools.

        Returns:
            Optional[Dict[str, Any]]: Device information or None if failed.
        """
        try:
            if self.tools is None:
                logger.error("Droidrun tools not initialized")
                return None

            # There is no direct 'get_info' in AdbTools; this is a simple
            # example using shell commands to retrieve info.
            brand = self.tools.shell("getprop ro.product.brand")
            model = self.tools.shell("getprop ro.product.model")
            android_version = self.tools.shell("getprop ro.build.version.release")

            info: Dict[str, Any] = {
                "brand": brand.strip() if brand else None,
                "model": model.strip() if model else None,
                "android_version": (
                    android_version.strip() if android_version else None
                ),
            }
            logger.info("✅ Device info retrieved successfully")
            return info
        except Exception as e:
            logger.error(f"❌ Failed to get device info: {e}")
            return None

    def install_app(self, app_path: str) -> bool:
        """Install APK on connected device.

        Args:
            app_path (str): Path to APK file.

        Returns:
            bool: True if installation successful, False otherwise.
        """
        try:
            if self.tools is None:
                logger.error("Droidrun tools not initialized")
                return False

            logger.info(f"Installing app: {app_path}")
            # AdbTools exposes an 'install' helper for APKs.
            result = self.tools.install(app_path)
            logger.info("✅ App installed successfully")
            return result
        except Exception as e:
            logger.error(f"❌ Failed to install app: {e}")
            return False

    def execute_command(self, command: str) -> Optional[str]:
        """Execute shell command on device.

        Args:
            command (str): Shell command to execute.

        Returns:
            Optional[str]: Command output or None if failed.
        """
        try:
            if self.tools is None:
                logger.error("Droidrun tools not initialized")
                return None

            logger.info(f"Executing command: {command}")
            result = self.tools.shell(command)
            logger.info("✅ Command executed successfully")
            return result
        except Exception as e:
            logger.error(f"❌ Failed to execute command: {e}")
            return None
