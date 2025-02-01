from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

LANGUAGES = {
    'en': 'English',
    'hi': 'Hindi',
    'bn': 'Bengali',
}

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        for lang_code in LANGUAGES:
            if lang_code != 'en':
                translated_text = translator.translate(self.question, dest=lang_code).text
                setattr(self, f'question_{lang_code}', translated_text)
        super().save(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        cache_key = f'faq_{self.id}_{lang}'
        question = cache.get(cache_key)
        if not question:
            question = getattr(self, f'question_{lang}', self.question)
            cache.set(cache_key, question, timeout=3600)
        return question

    def _str_(self):
        return self.question