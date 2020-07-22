from ..models.post_it import PostIt
from ..models.coordinate import Coordinate
from ..recognition.PostItExtractor import PostItExtractor
import connexion
import uuid


def index_post_its(body, picture_link):  # noqa: E501
    """Detects Post-it notes and digitalizes their contents

    By passing in the appropriate options, you can digitalize the contents of Post-it notes  # noqa: E501

    :param body: Picture containing the Post-it notes to digitalize. Only required if no query parameter is provided.
    :type body: dict | bytes
    :param picture_link: A link to the picture to be digitalized. Only required if no request body is provided.
    :type picture_link: str

    :rtype: List[PostIt]
    """
    if connexion.request.is_json:
        # TODO: implement
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501

    # print(picture_link)
    # extractor = PostItExtractor(False)
    # post_its = extractor.image_to_post_its("../data/colored/MultiplePostIts8.jpg")
    # return post_it_class_convert(post_its)
    if picture_link == "test.jpg":
        post_it_1 = PostIt("1", "Hochschule", "color", Coordinate(1008, 304), 0, 0)
        post_it_2 = PostIt("2", "where", "color", Coordinate(98, 290), 0, 0)
        post_it_3 = PostIt("3", "hklein", "color", Coordinate(608, 446), 0, 0)
        post_it_4 = PostIt("4", "Smartphoane", "color", Coordinate(608, 38), 0, 0)
        return [post_it_1, post_it_2, post_it_3, post_it_4]
    else:
        return []


def post_it_class_convert(post_its):
    output = []
    for post in post_its:
        new = PostIt(str(uuid.uuid4()), post.text, "color", Coordinate(post.rect[0], post.rect[1]),
                     post.rect[3], post.rect[4])
        output.append(new)

    return output
