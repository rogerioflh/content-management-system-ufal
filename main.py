from models.author import Author
from models.category import Category
from models.article import Article

author1 = Author("John Doe", "john@example.com")
category1 = Category("Technology")
article1 = Article("Intro to Python", "Python is a versatile language...", author1, category1)
article1.publish()

print(article1)
print(author1)
print(category1)