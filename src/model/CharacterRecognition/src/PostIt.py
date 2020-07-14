class PostIt:
    def __init__(self, file_path, rect):
        self.file_path = file_path
        self.rect = rect
        self.text = ''

    def print_info(self):
        print(f"Path: {self.file_path}")
        print(f"Post-It position: ({self.rect[0]}|{self.rect[1]})")
        print(f"Post-It size: ({self.rect[2]}|{self.rect[3]})")
        print(f"Post-It text: {self.text}")