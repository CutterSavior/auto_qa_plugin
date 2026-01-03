"""
Kirara Auto QA Plugin
自動問答插件
"""

from kirara_ai.plugin_manager.plugin import Plugin
from kirara_ai.logger import get_logger
from kirara_ai.ioc.container import DependencyContainer

logger = get_logger("AutoQAPlugin")

class AutoQAPlugin(Plugin):
    """自動問答插件主類別"""
    
    def __init__(self, container: DependencyContainer):
        super().__init__()
        self.container = container
        self.name = "auto-qa-plugin"
        self.version = "1.0.0"
        self.qa_pairs = []
        
    def on_load(self):
        """插件載入時執行"""
        logger.info("?? AutoQA Plugin 載入成功！")
        
        # 預設問答配對
        self.qa_pairs = [
            {
                "keywords": ["你好", "嗨", "hello"],
                "response": "你好！我是自動問答機器人，很高興為你服務！??"
            },
            {
                "keywords": ["時間", "幾點", "現在時間"],
                "response": "我現在無法檢查時間，但我很樂意幫助你！"
            },
            {
                "keywords": ["謝謝", "thanks"],
                "response": "不客氣！很高興能幫到你！?"
            }
        ]
        
    def on_start(self):
        """插件啟動時執行"""
        logger.info("?? AutoQA Plugin 啟動成功！")
        
    def on_stop(self):
        """插件停止時執行"""
        logger.info("?? AutoQA Plugin 停止")
        
    async def handle_message(self, message):
        """處理訊息"""
        content = message.content
        
        # 指令處理
        if content == "/qa_test":
            await message.reply("?? AutoQA Plugin 運作正常！\n? 插件版本：1.0.0\n? 功能：關鍵字匹配+自動回覆")
            return True
            
        elif content == "/qa_start":
            await message.reply("?? 自動問答功能已啟動！")
            return True
            
        elif content == "/qa_stop":
            await message.reply("?? 自動問答功能已停止！")
            return True
            
        elif content == "/qa_status":
            status = "?? 運行中" 
            await message.reply(f"?? AutoQA 狀態：{status}\n?? 已載入 {len(self.qa_pairs)} 組問答配對")
            return True
            
        elif content.startswith("/qa_add "):
            # 新增問答配對功能
            try:
                parts = content.replace("/qa_add ", "").split("|")
                if len(parts) == 2:
                    keywords = [k.strip() for k in parts[0].split(",")]
                    response = parts[1].strip()
                    
                    self.qa_pairs.append({
                        "keywords": keywords,
                        "response": response
                    })
                    
                    await message.reply(f"? 已新增問答配對！\n?? 關鍵字：{keywords}\n?? 回覆：{response}")
                else:
                    await message.reply("? 格式錯誤！請使用：/qa_add 關鍵字1,關鍵字2|回覆內容")
            except Exception as e:
                await message.reply(f"? 新增失敗：{str(e)}")
            return True
            
        else:
            # 關鍵字匹配
            for qa_pair in self.qa_pairs:
                for keyword in qa_pair['keywords']:
                    if keyword.lower() in content.lower():
                        await message.reply(qa_pair['response'])
                        return True
                        
        return False
        
    def get_info(self):
        """取得插件資訊"""
        return {
            "name": self.name,
            "version": self.version,
            "qa_pairs_count": len(self.qa_pairs),
            "status": "active"
        }
