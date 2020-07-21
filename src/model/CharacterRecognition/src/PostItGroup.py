class PostItGroup:
    def __init__(self, rgb):
        self.color = rgb
        self.post_its = []

    def __str__(self):
        grp_text = f"Group color: {self.color}\n\n"

        for post_it in self.post_its:
            grp_text += post_it.__str__() + "\n"

        return grp_text
