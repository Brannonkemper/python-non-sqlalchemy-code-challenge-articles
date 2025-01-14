class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
        type(self).all.append(self)
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, '_title'):
            self._title = title
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    def articles(self):
        pass
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 1 and not hasattr(self, '_name'):
            self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        pass
        return list({article.magazine for article in self.articles()})
    
    def add_article(self, magazine, title):
        pass
        return Article(self, magazine, title)

    def topic_areas(self):
        pass
        if self.articles():
            return list({article.magazine.category for article in self.articles()})
        return None

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) >= 1:
            self._category = category

    def articles(self):
        pass
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        pass
        return list({article.author for article in self.articles()})

    def article_titles(self):
        pass
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        pass
        author_count = {}
        for article in self.articles():
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1
        return [author for author, count in author_count.items() if count >= 2] or None