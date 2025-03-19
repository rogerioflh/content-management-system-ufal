from datetime import datetime
from .author import Author
from .category import Category

class Article:
    def __init__(self, title: str, content: str, author: Author, category: Category):
        self.__title = title
        self.__content = content
        self.__author = author
        self.__category = category
        self.__published_at = None
        
        author.add_article(self)
        category.add_article(self)
    
    @property
    def title(self):
        return self.__title
    
    @property
    def content(self):
        return self.__content
    
    @property
    def author(self):
        return self.__author
    
    @property
    def category(self):
        return self.__category
    
    @property
    def published_at(self):
        return self.__published_at
    
    def edit(self, new_title: str, new_content: str):
        self.__title = new_title
        self.__content = new_content
    
    def publish(self):
        self.__published_at = datetime.now()
    
    def __str__(self):
        return f"Article: {self.__title} by {self.__author.name} in {self.__category.name}" + (f" (Published: {self.__published_at})" if self.__published_at else " (Draft)")