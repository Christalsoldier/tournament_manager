from sqlalchemy import create_engine



class DBHandler(object):
    
    def __init__(self, engine_url: str):
        self.engine = create_engine(engine_url, echo=True)
        