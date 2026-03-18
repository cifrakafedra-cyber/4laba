import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from telegram import Update, User, Message, Chat
from bot.bot import TelegramBot


@pytest.fixture
def bot():
    """Фикстура для создания экземпляра бота"""
    return TelegramBot(token="test_token_123456")


@pytest.fixture
def mock_update():
    """Фикстура для создания мок-объекта Update"""
    update = MagicMock(spec=Update)
    update.effective_user = MagicMock(spec=User)
    update.effective_user.id = 12345
    update.message = MagicMock(spec=Message)
    update.message.reply_text = AsyncMock()
    return update


@pytest.fixture
def mock_context():
    """Фикстура для создания мок-объекта Context"""
    return MagicMock()


@pytest.mark.asyncio
async def test_start_command(bot, mock_update, mock_context):
    """Тест команды /start"""
    await bot.start_command(mock_update, mock_context)
    
    mock_update.message.reply_text.assert_called_once()
    call_args = mock_update.message.reply_text.call_args[0][0]
    assert "Привет" in call_args
    assert "/start" in call_args


@pytest.mark.asyncio
async def test_search_command(bot, mock_update, mock_context):
    """Тест команды /search"""
    await bot.search_command(mock_update, mock_context)
    
    mock_update.message.reply_text.assert_called_once()
    call_args = mock_update.message.reply_text.call_args[0][0]
    assert "поиска" in call_args


@pytest.mark.asyncio
async def test_chat_command(bot, mock_update, mock_context):
    """Тест команды /chat"""
    await bot.chat_command(mock_update, mock_context)
    
    mock_update.message.reply_text.assert_called_once()
    call_args = mock_update.message.reply_text.call_args[0][0]
    assert "чата" in call_args


@pytest.mark.asyncio
async def test_basic_command(bot, mock_update, mock_context):
    """Тест команды /basic"""
    await bot.basic_command(mock_update, mock_context)
    
    mock_update.message.reply_text.assert_called_once()
    call_args = mock_update.message.reply_text.call_args[0][0]
    assert "Версия" in call_args


def test_bot_initialization():
    """Тест инициализации бота"""
    token = "test_token"
    bot = TelegramBot(token)
    assert bot.token == token
    assert bot.application is None


@pytest.mark.asyncio
async def test_all_commands_respond(bot, mock_update, mock_context):
    """Тест что все команды отвечают"""
    commands = [
        bot.start_command,
        bot.search_command,
        bot.chat_command,
        bot.basic_command
    ]
    
    for command in commands:
        mock_update.message.reply_text.reset_mock()
        await command(mock_update, mock_context)
        assert mock_update.message.reply_text.called