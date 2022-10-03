class ValueNotInRangeError(Exception):
    """Raised when the input value is not between given range"""

    def __init__(self,input,value,start,end):
        self.message = f"{input} -> {value} is not in ({start}, {end}) range"
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'