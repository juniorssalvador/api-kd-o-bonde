class SearchModel:

    def __init__(self, ident: int, title: str, data, sub_title: str, typee: str):
        self.id = ident
        self.title = title
        self.data = data
        self.seb_title = sub_title
        self.typee = typee

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "seb_title": self.seb_title,
            "typee": self.typee,
            "data": self.data
        }
