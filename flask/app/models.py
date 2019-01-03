# docker1/app/models.py

from datetime import datetime

from app import db



class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text())
    pubDateTime = db.Column(db.DateTime())
  

    # ---------------------------------------------------------------
  

    @classmethod
    def GetAll(cls):
        postQuery = cls.query\
            .order_by(cls.pubDateTime.desc())

        return postQuery


    @classmethod
    def Get(cls, id):
        return cls.query.get(id)
    
    
    @classmethod
    def Delete(cls, id):
        post = cls.Get(id)
        if post:
            db.session.delete(post)
            db.session.commit()
        
        return True
    
        
    @classmethod
    def Insert(cls, formData):
        fd = formData
        post = cls(fd['title'], fd['content'], fd['pubDateTime'])
        db.session.add(post)
        db.session.commit()
        
        
    # ---------------------------------------------------------------
    
    
    def __init__(self, title, content, pubDateTime):
        self.title = title
        self.content = content
        self.pubDateTime = pubDateTime if pubDateTime else datetime.now()
    
    
    def update(self, formData):
        fd = formData
        self.title = fd['title']
        self.content = fd['content']
        self.pubDateTime = fd['pubDateTime'] if fd['pubDateTime'] else datetime.now()
        db.session.commit()
    