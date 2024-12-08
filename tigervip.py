import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# 启用日志记录
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# 你的 Bot Token
TOKEN = "7651787339:AAEPhks50IzOP3eI_FeXO9Oh2X_-b8Xcl7k"

# 处理 /start 命令
async def start(update: Update, context: CallbackContext) -> None:
    # 定义按钮
    keyboard = [
        [
            InlineKeyboardButton(
                "存款/出款服务 人工服务",
                url="https://tawk.to/chat/66a1e8b732dca6db2cb56e6f/1i3k7a3lg",
            ),
        ],
        [
            InlineKeyboardButton(
                "Tigervip 每日活动奖励",
                url="https://tigervip.com/home/canReceive?tabItem=discount",
            ),
        ],
        [
            InlineKeyboardButton(
                "活动介绍",
                callback_data="activity",
            ),
        ],
        [
            InlineKeyboardButton(
                "关注频道 每日领取兑换码奖金",
                url="https://t.me/tigervipcom",
            ),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # 发送带按钮的欢迎消息
    welcome_message = (
        "亲爱的玩家，这里是TIGERVIP 客服，有什么可以帮到您？\n\n"
        "点击以下按钮快速访问："
    )
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# 处理活动介绍按钮
async def show_activity(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    # 回复活动介绍
    activity_message = (
        "🎉 活动介绍：\n\n"
        "1️⃣ 新人活动：注册立即领取 R$5 🎁\n"
        "2️⃣ 每月5号和20号：大奖金回馈日，送给所有玩家！💰"
    )
    await query.message.reply_text(activity_message)

# 主函数
def main() -> None:
    # 创建 Application 对象并传入 Token
    application = Application.builder().token(TOKEN).build()

    # 添加处理器
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(show_activity, pattern="^activity$"))

    # 启动机器人
    application.run_polling()

if __name__ == "__main__":
    main()
