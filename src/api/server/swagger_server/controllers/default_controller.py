from ..models.post_it import PostIt
from ..models.coordinate import Coordinate
from time import sleep
import connexion

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

    print(picture_link)
    if picture_link == "test.jpg":
        post_it_1 = PostIt("1", "Hochschule", "color", Coordinate(1008, 304), 0, 0)
        post_it_2 = PostIt("2", "where", "color", Coordinate(98, 290), 0, 0)
        post_it_3 = PostIt("3", "hklein", "color", Coordinate(608, 446), 0, 0)
        post_it_4 = PostIt("4", "Smartphoane", "color", Coordinate(608, 38), 0, 0)
        sleep(5)
        return [post_it_1, post_it_2, post_it_3, post_it_4]
    else:
        return []
