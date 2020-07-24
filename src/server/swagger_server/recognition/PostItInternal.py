class PostItInternal:
    def __init__(self, file, rect):
        self.file = file
        self.rect = rect
        self.text = ''
        self.rgb = (0, 0, 0)
        self.color_grp = (0, 0, 0)

    def __str__(self):
        return f"Post-It position: ({self.rect[0]}|{self.rect[1]})\n"\
             + f"Post-It size: ({self.rect[2]}|{self.rect[3]})\n"\
             + f"Post-It text: {self.text}\n"\
             + f"Post-It color: {self.rgb}\n"
