class Author:
    def __init__(self, name: str, email: str):
        self.__name = name
        self.__email = email
        self.__articles = []
    
    @property
    def name(self):
        return self.__name
    
    @property
    def email(self):
        return self.__email
    
    def add_article(self, article):
        self.__articles.append(article)
    
    def get_articles(self):
        return self.__articles
    
    def __str__(self):
        return f"Author: {self.__name} ({self.__email})"