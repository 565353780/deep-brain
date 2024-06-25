class Cell(object):
    def __init__(self, id: Union[int, None]=None) -> None:
        self.id = None
        return

    def isValid(self) -> bool:
        return self.id is not None
