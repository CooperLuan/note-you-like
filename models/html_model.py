from goose import Goose
from goose.text import StopWordsChinese

from models.base import BaseModel


class HTMLModel(BaseModel):

    def __init__(self, html):
        self.html = isinstance(html, str) and html.decode('utf-8') or html
        self.goose = Goose(config={
            'debug': True,
            'stopwords_class': StopWordsChinese,
        })

    def extract_all(self):
        page = self.goose.extract(raw_html=self.html)
        return {
            'meta_lang': page.meta_lang,
            'meta_keywords': page.meta_keywords,
            'meta_description': page.meta_description,
            'domain': page.domain,
            'title': page.title,
            'tags': page.tags,
            'cleaned_text': page.cleaned_text,
            'top_image': page.top_image.src,
        }
