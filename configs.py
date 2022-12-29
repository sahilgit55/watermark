# (c) @Antonx9

# Don't Forget That I Made This!
# So Give Credits!


import os


class Config(object):
	Session_String = os.environ.get("BOT_TOKEN", "5980925925:AAFNqaUEE6vpp4_k2ijoilJ5x870s7eIIx0")
	API_ID = int(os.environ.get("API_ID", "8256203"))
	API_HASH = os.environ.get("API_HASH", "45b3b561298ee72408e08a3c46d5f697")
	STREAMTAPE_API_PASS = os.environ.get("STREAMTAPE_API_PASS", "NoNeed")
	STREAMTAPE_API_USERNAME = os.environ.get("STREAMTAPE_API_USERNAME", "NoNeed")
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001628210353"))
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
	PRESET = os.environ.get("PRESET", "veryfast")
	OWNER_ID = int(os.environ.get("OWNER_ID", "5968806660"))
	CAPTION = "By @AHToolsBot"
	BOT_USERNAME = "ANTON"
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Manoj123:Manoj123@cluster0.z0c2mif.mongodb.net/?retryWrites=true&w=majority")
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	ALLOW_UPLOAD_TO_STREAMTAPE = bool(os.environ.get("ALLOW_UPLOAD_TO_STREAMTAPE", False))
	USAGE_WATERMARK_ADDER = """
Hi, I am Video Watermark Adder Bot!
**How to Added Watermark to a Video?**
**Usage:** First Send a JPG Image/Logo, then send any Video. Better add watermark to a MP4 or MKV Video.
__Note: I can only process one video at a time. As my server is Heroku, my health is not good. If you have any issues with Adding Watermark to a Video, then please Report at [Support Group](https://t.me/linux_repo).__
Desgined by @kkANTON
"""
	PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
