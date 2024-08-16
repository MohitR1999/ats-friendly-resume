class Certification:
    def __init__(self, title='', link='') -> None:
        self.title = title
        self.link = link
        
    def set_title(self, title : str) -> None:
        self.title = title
        
    def set_link(self, link : str) -> None:
        self.link = link