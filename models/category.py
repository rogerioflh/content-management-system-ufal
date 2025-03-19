class Category:
    def __init__(self, name: str):
        self.__name = name
        self.__articles = []
    
    @property
    def name(self):
        return self.__name
    
    def add_article(self, article):
        self.__articles.append(article)
    
    def get_articles(self):
        return self.__articles

    def __str__(self):
        return f"Category: {self.__name}"