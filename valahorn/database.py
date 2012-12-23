from config import Config
from models import Base, Article

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

print(fake_article.id)

class Database(object):
    def __init__(self):
        cfg = Config()
        self.engine = create_engine(cfg.database.connect_string)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_latest_article(self, group):
        pass

