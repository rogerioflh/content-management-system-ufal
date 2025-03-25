import json
from datetime import datetime

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

def load_from_json(filename="database.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"authors": [], "categories": [], "articles": []}

def save_to_json(data, filename="database.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def main():
    # Carregar os dados existentes
    data = load_from_json()
    
    authors = {author["email"]: Author(author["name"], author["email"]) for author in data.get("authors", [])}
    categories = {cat["name"]: Category(cat["name"]) for cat in data.get("categories", [])}
    
    # Entrada do usuário
    name = input("Digite o nome do autor: ")
    email = input("Digite o email do autor: ")
    
    if email in authors:
        author = authors[email]
    else:
        author = Author(name, email)
        authors[email] = author
    
    category_name = input("Digite o nome da categoria: ")
    
    if category_name in categories:
        category = categories[category_name]
    else:
        category = Category(category_name)
        categories[category_name] = category
    
    title = input("Digite o título do artigo: ")
    content = input("Digite o conteúdo do artigo: ")
    
    article = Article(title, content, author, category)
    article.publish()
    
    # Atualizar os dados
    if not any(a["email"] == author.email for a in data["authors"]):
        data["authors"].append({"name": author.name, "email": author.email})
    
    if not any(c["name"] == category.name for c in data["categories"]):
        data["categories"].append({"name": category.name})
    
    data["articles"].append({
        "title": article.title,
        "content": article.content,
        "author": author.email,
        "category": category.name,
        "published_at": article.published_at.strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # Salvar no arquivo JSON
    save_to_json(data)
    
    print("Artigo salvo com sucesso!")

if __name__ == "__main__":
    main()