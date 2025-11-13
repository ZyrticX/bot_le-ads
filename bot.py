#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram Leads Bot - Leads Deal Management
"""

import logging
import os
from datetime import datetime
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand

# Load environment variables from .env file
load_dotenv()
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters
)
from airtable_manager import AirtableManager

# Setup Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# States for conversation handlers
(
    WAITING_FOR_CLIENT_NAME,
    WAITING_FOR_CLIENT_TYPE,
    WAITING_FOR_DEAL_DETAILS,
    WAITING_FOR_PAYMENT_AMOUNT,
    SELECT_DEAL_FOR_PAYMENT
) = range(5)

class LeadsBot:
    def __init__(self):
        self.airtable = AirtableManager()
        
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Start command"""
        user = update.effective_user
        
        # Create inline keyboard with main actions
        keyboard = [
            [
                InlineKeyboardButton("📝 New Deal", callback_data="menu_newdeal"),
                InlineKeyboardButton("👥 New Client", callback_data="menu_newclient")
            ],
            [
                InlineKeyboardButton("💳 Record Payment", callback_data="menu_payment"),
                InlineKeyboardButton("📊 Statistics", callback_data="menu_stats")
            ],
            [
                InlineKeyboardButton("📋 View Deals", callback_data="menu_deals"),
                InlineKeyboardButton("👤 View Clients", callback_data="menu_clients")
            ],
            [
                InlineKeyboardButton("❓ Help", callback_data="menu_help")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        welcome_message = f"""
👋 Hello {user.first_name}!

🤖 **Welcome to Leads Management Bot**

Your professional assistant for managing lead deals with Airtable CRM integration.

💡 **Quick Actions:**
Use the buttons below or type commands directly:

/newdeal - Create new deal
/newclient - Add client/supplier
/payment - Record payment
/deals - View all deals
/clients - List clients
/stats - Statistics
/help - How to use this bot

---
✨ Created By **Corporation2024**
        """
        await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode='Markdown')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Help command - explain how to use the bot"""
        help_message = """
📚 **Leads Management Bot - User Guide**

This bot helps you manage lead deals efficiently through Telegram, with automatic sync to Airtable CRM.

---

🎯 **MAIN FEATURES:**

1️⃣ **Create Deals** - Track buy/sell transactions
2️⃣ **Manage Clients** - Keep client & supplier database
3️⃣ **Record Payments** - Monitor cash flow
4️⃣ **Auto Calculations** - Profit, price per lead
5️⃣ **Statistics** - Real-time reports
6️⃣ **Airtable Sync** - All data backed up in cloud

---

📝 **HOW TO CREATE A DEAL:**

**Step 1:** Someone writes in chat:
`"20 leads Italy next Monday"`

**Step 2:** Reply to that message with:
`/newdeal`

**Step 3:** Select deal type:
• Buy (you're buying)
• Sell (you're selling)

**Step 4:** Send deal details:
```
Client: John Doe
Supplier: Mario Italy
Quantity: 20
Country: Italy
Date: 2025-11-15
Buy Price: 5
Sell Price: 8
```

**Step 5:** Bot confirms and calculates profit!
✅ Profit: $(8-5) × 20 = $60

---

👥 **HOW TO ADD CLIENT/SUPPLIER:**

1. Send `/newclient`
2. Choose: Client or Supplier
3. Enter name
4. Done! ✅

---

💳 **HOW TO RECORD PAYMENT:**

1. Send `/payment`
2. Select deal from list
3. Enter amount received
4. Confirmed! ✅

---

📊 **VIEW YOUR DATA:**

• `/deals` - See all deals
• `/clients` - List all clients
• `/stats` - View statistics (profit, deals, leads)

---

⚙️ **ALL COMMANDS:**

/start - Main menu
/help - This guide
/newdeal - Create new deal (Reply to message)
/newclient - Add client/supplier
/payment - Record payment
/deals - View all deals
/clients - List clients
/stats - Show statistics
/cancel - Cancel current operation

---

💡 **TIPS:**

✓ Always Reply to the original message when using /newdeal
✓ Keep client names consistent for better tracking
✓ Record payments immediately for accurate reporting
✓ Check /stats regularly to monitor performance
✓ All data is automatically saved to Airtable

---

🆘 **NEED HELP?**

• Use /help anytime to see this guide
• Type /cancel to stop any operation
• Contact support if you encounter issues

---

✨ Created By **Corporation2024**
🔗 Powered by Telegram Bot API & Airtable
        """
        await update.message.reply_text(help_message, parse_mode='Markdown')
    
    async def menu_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle menu button clicks"""
        query = update.callback_query
        await query.answer()
        
        action = query.data.replace("menu_", "")
        
        if action == "help":
            await self.help_command(update, context)
        elif action == "newdeal":
            await query.message.reply_text(
                "📝 **Create New Deal**\n\n"
                "To create a deal:\n"
                "1. Find the message with deal details\n"
                "2. Reply to it with `/newdeal`\n\n"
                "💡 Tip: The bot needs the original message context!",
                parse_mode='Markdown'
            )
        elif action == "newclient":
            await self.newclient_command(query, context)
        elif action == "payment":
            await self.payment_command(query, context)
        elif action == "stats":
            await self.stats_command(query, context)
        elif action == "deals":
            await self.deals_command(query, context)
        elif action == "clients":
            await self.clients_command(query, context)

    async def newdeal_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """New deal command - create new deal"""
        
        # Check if this is a Reply to a message
        if not update.message.reply_to_message:
            await update.message.reply_text(
                "❌ You must Reply to a message with deal details!\n\n"
                "Example: Tag the bot with /newdeal as Reply to a message:\n"
                "'20 leads Italy next Monday'"
            )
            return ConversationHandler.END
        
        # Save the original message content
        deal_text = update.message.reply_to_message.text
        context.user_data['deal_raw_text'] = deal_text
        context.user_data['deal_message_id'] = update.message.reply_to_message.message_id
        
        # Display deal type selection menu
        keyboard = [
            [
                InlineKeyboardButton("🛒 Buy (I'm buying)", callback_data="deal_type_buy"),
                InlineKeyboardButton("💰 Sell (I'm selling)", callback_data="deal_type_sell")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"📝 **New Deal**\n\n"
            f"Deal text:\n_{deal_text}_\n\n"
            f"Select deal type:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
        return WAITING_FOR_DEAL_DETAILS

    async def deal_type_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle deal type selection"""
        query = update.callback_query
        await query.answer()
        
        deal_type = "Buy" if query.data == "deal_type_buy" else "Sell"
        context.user_data['deal_type'] = deal_type
        
        # Request deal details
        await query.edit_message_text(
            f"✅ Deal type: **{deal_type}**\n\n"
            f"Now send the deal details in this format:\n\n"
            f"```\n"
            f"Client: Client name\n"
            f"Supplier: Supplier name (if relevant)\n"
            f"Quantity: 20\n"
            f"Country: Italy\n"
            f"Date: 2025-11-04\n"
            f"Buy Price: 100\n"
            f"Sell Price: 150\n"
            f"```\n\n"
            f"Or send in one line separated by commas",
            parse_mode='Markdown'
        )
        
        return WAITING_FOR_DEAL_DETAILS

    async def receive_deal_details(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Receive deal details and save to Airtable"""
        deal_details = update.message.text
        
        # Parse the text
        parsed = self._parse_deal_text(deal_details)
        
        if not parsed:
            await update.message.reply_text(
                "❌ Couldn't understand the details. Try again in this format:\n"
                "Client: name, Supplier: name, Quantity: 20, Country: Italy, Date: 2025-11-04, "
                "Buy Price: 100, Sell Price: 150"
            )
            return WAITING_FOR_DEAL_DETAILS
        
        # Add additional info
        parsed['deal_type'] = context.user_data.get('deal_type', 'Sell')
        parsed['raw_text'] = context.user_data.get('deal_raw_text', '')
        parsed['telegram_user'] = update.effective_user.username or update.effective_user.first_name
        parsed['telegram_group'] = update.effective_chat.title if update.effective_chat.type != 'private' else 'Private'
        
        # Calculate profit
        buy_price = parsed.get('buy_price', 0)
        sell_price = parsed.get('sell_price', 0)
        quantity = parsed.get('quantity', 0)
        
        profit = (sell_price - buy_price) * quantity
        price_per_lead = sell_price if sell_price > 0 else buy_price
        
        parsed['profit'] = profit
        parsed['price_per_lead'] = price_per_lead
        
        # Save to Airtable
        try:
            record = self.airtable.create_deal(parsed)
            
            summary = f"""
✅ **Deal added successfully!**

🆔 Deal ID: {record['id'][:8]}
👤 Client: {parsed.get('client', 'N/A')}
📦 Supplier: {parsed.get('supplier', 'N/A')}
🔢 Lead quantity: {quantity}
🌍 Country: {parsed.get('country', 'N/A')}
📅 Delivery date: {parsed.get('delivery_date', 'N/A')}

💵 Buy price: ${buy_price}
💰 Sell price: ${sell_price}
📊 Price per lead: ${price_per_lead}

{'💚 Profit' if profit >= 0 else '💔 Loss'}: ${profit}

🔗 Added to Airtable CRM

━━━━━━━━━━━━━━━━━━━━
Created By Corporation2024
            """
            
            await update.message.reply_text(summary, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Error creating deal: {e}")
            await update.message.reply_text(f"❌ Error saving deal: {str(e)}")
        
        return ConversationHandler.END

    def _parse_deal_text(self, text: str) -> dict:
        """Parse deal text to structured data"""
        data = {}
        
        # Try to identify structured format
        lines = text.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower()
                value = value.strip()
                
                if 'client' in key or 'customer' in key:
                    data['client'] = value
                elif 'supplier' in key or 'vendor' in key:
                    data['supplier'] = value
                elif 'quantity' in key or 'qty' in key or 'leads' in key or 'amount' in key:
                    data['quantity'] = int(''.join(filter(str.isdigit, value)))
                elif 'country' in key or 'location' in key:
                    data['country'] = value
                elif 'date' in key or 'delivery' in key:
                    data['delivery_date'] = value
                elif 'buy' in key or 'purchase' in key or 'cost' in key:
                    data['buy_price'] = float(''.join(filter(lambda x: x.isdigit() or x == '.', value)))
                elif 'sell' in key or 'sale' in key or 'price' in key:
                    data['sell_price'] = float(''.join(filter(lambda x: x.isdigit() or x == '.', value)))
        
        return data if data else None

    async def newclient_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """New client command - add client or supplier"""
        keyboard = [
            [
                InlineKeyboardButton("👤 Client", callback_data="client_type_customer"),
                InlineKeyboardButton("📦 Supplier", callback_data="client_type_supplier")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "👥 **Add New Client/Supplier**\n\n"
            "Select type:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
        return WAITING_FOR_CLIENT_TYPE

    async def client_type_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Select client/supplier type"""
        query = update.callback_query
        await query.answer()
        
        client_type = "Client" if query.data == "client_type_customer" else "Supplier"
        context.user_data['client_type'] = client_type
        
        await query.edit_message_text(
            f"✅ Adding: **{client_type}**\n\n"
            f"Send the {client_type} name:",
            parse_mode='Markdown'
        )
        
        return WAITING_FOR_CLIENT_NAME

    async def receive_client_name(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Receive client/supplier name and add to Airtable"""
        name = update.message.text.strip()
        client_type = context.user_data.get('client_type', 'Client')
        
        try:
            data = {
                'name': name,
                'type': client_type,
                'telegram_user': update.effective_user.username or update.effective_user.first_name,
                'added_date': datetime.now().isoformat()
            }
            
            record = self.airtable.create_client(data)
            
            await update.message.reply_text(
                f"✅ **{client_type} added successfully!**\n\n"
                f"📛 Name: {name}\n"
                f"🆔 ID: {record['id'][:8]}\n"
                f"📅 Added date: {datetime.now().strftime('%m/%d/%Y')}\n\n"
                f"🔗 Added to Airtable CRM\n\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"Created By Corporation2024",
                parse_mode='Markdown'
            )
            
        except Exception as e:
            logger.error(f"Error creating client: {e}")
            await update.message.reply_text(f"❌ Error adding {client_type}: {str(e)}")
        
        return ConversationHandler.END

    async def payment_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Payment command - record payment"""
        try:
            # Get recent deals
            deals = self.airtable.get_recent_deals(limit=10)
            
            if not deals:
                await update.message.reply_text("No active deals to record payment.")
                return ConversationHandler.END
            
            # Create buttons to select deal
            keyboard = []
            for deal in deals:
                fields = deal.get('fields', {})
                client = fields.get('Client', 'N/A')
                amount = fields.get('Sell Price', 0)
                date = fields.get('Delivery Date', 'N/A')
                
                button_text = f"{client} - ${amount} ({date})"
                keyboard.append([InlineKeyboardButton(button_text, callback_data=f"payment_deal_{deal['id']}")])
            
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                "💳 **Record Payment**\n\n"
                "Select deal:",
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
            
            return SELECT_DEAL_FOR_PAYMENT
            
        except Exception as e:
            logger.error(f"Error in payment command: {e}")
            await update.message.reply_text(f"❌ Error: {str(e)}")
            return ConversationHandler.END

    async def select_deal_for_payment(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Select deal for payment recording"""
        query = update.callback_query
        await query.answer()
        
        deal_id = query.data.replace("payment_deal_", "")
        context.user_data['payment_deal_id'] = deal_id
        
        await query.edit_message_text(
            "💵 **How much did you receive?**\n\n"
            "Send the payment amount (number only):"
        )
        
        return WAITING_FOR_PAYMENT_AMOUNT

    async def receive_payment_amount(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Receive payment amount and update"""
        try:
            amount = float(update.message.text.strip())
            deal_id = context.user_data.get('payment_deal_id')
            
            # Record payment in Airtable
            payment_data = {
                'deal_id': deal_id,
                'amount': amount,
                'date': datetime.now().isoformat(),
                'telegram_user': update.effective_user.username or update.effective_user.first_name
            }
            
            payment_record = self.airtable.create_payment(payment_data)
            
            await update.message.reply_text(
                f"✅ **Payment recorded successfully!**\n\n"
                f"💰 Amount: ${amount}\n"
                f"📅 Date: {datetime.now().strftime('%m/%d/%Y %H:%M')}\n"
                f"🆔 Payment ID: {payment_record['id'][:8]}\n\n"
                f"🔗 Updated in Airtable CRM\n\n"
                f"━━━━━━━━━━━━━━━━━━━━\n"
                f"Created By Corporation2024",
                parse_mode='Markdown'
            )
            
        except ValueError:
            await update.message.reply_text("❌ Please send a valid number")
            return WAITING_FOR_PAYMENT_AMOUNT
        except Exception as e:
            logger.error(f"Error recording payment: {e}")
            await update.message.reply_text(f"❌ Error recording payment: {str(e)}")
        
        return ConversationHandler.END

    async def deals_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Display all deals"""
        try:
            deals = self.airtable.get_all_deals()
            
            if not deals:
                await update.message.reply_text("No deals in the system.")
                return
            
            message = "📋 **All Deals:**\n\n"
            
            for deal in deals[:20]:  # Limit to 20 deals
                fields = deal.get('fields', {})
                client = fields.get('Client', 'N/A')
                quantity = fields.get('Quantity', 0)
                country = fields.get('Country', 'N/A')
                profit = fields.get('Profit', 0)
                
                message += f"👤 {client} | {quantity} leads | {country} | Profit: ${profit}\n"
            
            message += "\n━━━━━━━━━━━━━━━━━━━━\nCreated By Corporation2024"
            
            await update.message.reply_text(message, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Error fetching deals: {e}")
            await update.message.reply_text(f"❌ Error fetching deals: {str(e)}")

    async def clients_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Display list of clients"""
        try:
            clients = self.airtable.get_all_clients()
            
            if not clients:
                await update.message.reply_text("No clients in the system.")
                return
            
            message = "👥 **Clients and Suppliers List:**\n\n"
            
            for client in clients:
                fields = client.get('fields', {})
                name = fields.get('Name', 'N/A')
                client_type = fields.get('Type', 'N/A')
                
                icon = "👤" if client_type == "Client" else "📦"
                message += f"{icon} {name} ({client_type})\n"
            
            message += "\n━━━━━━━━━━━━━━━━━━━━\nCreated By Corporation2024"
            
            await update.message.reply_text(message, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Error fetching clients: {e}")
            await update.message.reply_text(f"❌ Error fetching clients: {str(e)}")

    async def stats_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Display statistics"""
        try:
            stats = self.airtable.get_statistics()
            
            message = f"""
📊 **Statistics**

🔢 Total deals: {stats['total_deals']}
💰 Total profit: ${stats['total_profit']:.2f}
📦 Total leads: {stats['total_leads']}
👥 Active clients: {stats['total_clients']}

📈 Average profit per deal: ${stats['avg_profit']:.2f}
📊 Average price per lead: ${stats['avg_price_per_lead']:.2f}

━━━━━━━━━━━━━━━━━━━━
Created By Corporation2024
            """
            
            await update.message.reply_text(message, parse_mode='Markdown')
            
        except Exception as e:
            logger.error(f"Error calculating stats: {e}")
            await update.message.reply_text(f"❌ Error calculating statistics: {str(e)}")

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Cancel operation"""
        await update.message.reply_text(
            "❌ Operation cancelled.\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "Created By Corporation2024"
        )
        return ConversationHandler.END


async def post_init(application: Application) -> None:
    """Set bot commands menu after initialization"""
    commands = [
        BotCommand("start", "Main menu"),
        BotCommand("help", "How to use this bot"),
        BotCommand("newdeal", "Create new deal (Reply to message)"),
        BotCommand("newclient", "Add new client/supplier"),
        BotCommand("payment", "Record payment"),
        BotCommand("deals", "View all deals"),
        BotCommand("clients", "List all clients"),
        BotCommand("stats", "Show statistics"),
        BotCommand("cancel", "Cancel current operation")
    ]
    await application.bot.set_my_commands(commands)
    logger.info("Bot commands menu set successfully")


def main():
    """Start the bot"""
    # Get Token from Environment Variables
    TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN not found in environment variables!")
        return
    
    # Create bot instance
    bot = LeadsBot()
    
    # Create Application with post_init callback
    application = Application.builder().token(TOKEN).post_init(post_init).build()
    
    # Add Handlers
    
    # Basic commands
    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(CommandHandler("help", bot.help_command))
    application.add_handler(CommandHandler("deals", bot.deals_command))
    application.add_handler(CommandHandler("clients", bot.clients_command))
    application.add_handler(CommandHandler("stats", bot.stats_command))
    
    # Menu callback handler
    application.add_handler(CallbackQueryHandler(bot.menu_callback, pattern="^menu_"))
    
    # Conversation Handler for new deal
    newdeal_conv = ConversationHandler(
        entry_points=[CommandHandler("newdeal", bot.newdeal_command)],
        states={
            WAITING_FOR_DEAL_DETAILS: [
                CallbackQueryHandler(bot.deal_type_callback, pattern="^deal_type_"),
                MessageHandler(filters.TEXT & ~filters.COMMAND, bot.receive_deal_details)
            ]
        },
        fallbacks=[CommandHandler("cancel", bot.cancel)]
    )
    application.add_handler(newdeal_conv)
    
    # Conversation Handler for new client
    newclient_conv = ConversationHandler(
        entry_points=[CommandHandler("newclient", bot.newclient_command)],
        states={
            WAITING_FOR_CLIENT_TYPE: [
                CallbackQueryHandler(bot.client_type_callback, pattern="^client_type_")
            ],
            WAITING_FOR_CLIENT_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, bot.receive_client_name)
            ]
        },
        fallbacks=[CommandHandler("cancel", bot.cancel)]
    )
    application.add_handler(newclient_conv)
    
    # Conversation Handler for payment
    payment_conv = ConversationHandler(
        entry_points=[CommandHandler("payment", bot.payment_command)],
        states={
            SELECT_DEAL_FOR_PAYMENT: [
                CallbackQueryHandler(bot.select_deal_for_payment, pattern="^payment_deal_")
            ],
            WAITING_FOR_PAYMENT_AMOUNT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, bot.receive_payment_amount)
            ]
        },
        fallbacks=[CommandHandler("cancel", bot.cancel)]
    )
    application.add_handler(payment_conv)
    
    # Start the bot
    logger.info("🚀 Bot is starting...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
