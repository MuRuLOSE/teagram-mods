from googletrans import Translator

from telethon.types import Message

from .. import loader, utils

#required: googletrans

def set_default_lang(db):
    
    return db.get("teagram.loader", "lang", "ru")

@loader.module(name="Translator", author="teagram_mods", version=1) 
class TranslatorMod(loader.Module):                          
    """Translate text"""

    @loader.command(alias="tr")
    async def translate(self, message: Message, args: str):
        ''' - <lang to translate> <text> If you reply to message and you dont write text, userbot translate reply text, else userbot translate text in your command'''
        args = args.split()
        translator = Translator()
        reply = await message.get_reply_message()
        dest = 'язык'
        try:
            args[1]
        except IndexError:
            try:
                args[0]
            except IndexError:
                dest = set_default_lang(self.db)
            else:
                dest = args[0]
            if reply:
                text = reply.raw_text
                translated_text = translator.translate(
                    text=text, 
                    dest=dest
                )

                await utils.answer(
                    message,
                    f"Translated:\n{translated_text.text}"
                )
        else:
            try:
                args[0]
            except IndexError:
                dest = set_default_lang(self.db)
            else:
                dest = args[0]
            text = ' '.join(args[1:])

            translated_text = translator.translate(
                text=text, 
                dest=dest
            )

            await utils.answer(
                message,
                f"Translated:\n{translated_text.text}"
            )

