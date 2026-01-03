from kirara_ai.plugin_manager.plugin import Plugin
from kirara_ai.logger import get_logger

logger = get_logger("AutoQAPlugin")

class AutoQAPlugin(Plugin):
    def __init__(self, container):
        super().__init__()
        self.container = container

    def on_load(self):
        logger.info("AutoQAPlugin loaded successfully!")

    async def handle_message(self, message):
        if message.content == "/qa_test":
            await message.reply("🎉 AutoQA Plugin is working!")
            return True
        return False
