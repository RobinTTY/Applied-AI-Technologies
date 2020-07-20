class PostIt:
    def __init__(self, file, rect):
        self.file = file
        self.rect = rect
        self.text = ''

    def __str__(self):
        return f"Post-It position: ({self.rect[0]}|{self.rect[1]})\n"\
             + f"Post-It size: ({self.rect[2]}|{self.rect[3]})\n"\
             + f"Post-It text: {self.text}\n"
