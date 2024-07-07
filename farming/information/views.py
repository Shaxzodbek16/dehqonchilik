from django.shortcuts import render, redirect
from .models import Store, Product, News, Contact, Options
import asyncio
import functools
import logging

import telegram
from django.conf import settings

news = News.objects.all()
store_items = Store.objects.all()
products = Product.objects.all()
options = Options.objects.all()
store_items_true = len(Store.objects.filter(is_active=True))
if store_items_true == 0: store_items_true = True

all_info = {"news": news, "store_items": store_items, "products": products, "options": options,
            "store_items_true": store_items_true}


def main_and_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('tel')
        purpose = request.POST.get('purpose')
        text = request.POST.get('text')
        information = Contact(name=name, telephone=telephone, purpose=purpose, text=text)
        message = f'Name: {name}\nTelephone: {telephone}\nPurpose: {purpose}\nMessage: {text}'
        information.save()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        for chat_id in settings.TELEGRAM_CHAT_IDS:
            loop.run_in_executor(
                None,
                functools.partial(asyncio.run, send_telegram_message(message, chat_id))
            )

        return redirect('confirm')
    else:
        return render(request, "index.html", context=all_info)


def confirm(request):
    return render(request, 'confirm.html')


def _404(request):
    return render(request, '404.html', status=404)


logger = logging.getLogger(__name__)


async def send_telegram_message(message, chat_id):
    try:
        bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=chat_id, text=message)
    except telegram.error.TelegramError as e:
        logger.error(f"Error sending Telegram message to {chat_id}: {e}")
