from django.shortcuts import render, redirect
from .models import Store, Product, News, Contact
import asyncio
import functools
import logging

import telegram
from django.conf import settings

news = News.objects.all()
store = Store.objects.all()
products = Product.objects.all()
all_info = {"news": news, "store": store, "product": products}


def main_page(request):
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


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('telephone')
        purpose = request.POST.get('purpose')
        text = request.POST.get('message')

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

    return render(request, 'contact.html')
