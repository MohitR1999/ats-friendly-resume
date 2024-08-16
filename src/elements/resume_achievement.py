class Achievement:
    def __init__(self, title='') -> None:
        self.title = title
        
    def set_title(self, title : str) -> None:
        self.title = title