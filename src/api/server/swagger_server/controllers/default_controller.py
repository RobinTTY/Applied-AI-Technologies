from ..models.post_it import PostIt
from ..models.coordinate import Coordinate
from ..recognition.PostItExtractor import PostItExtractor
from io import BytesIO
from PIL import Image
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

    # assemble image
    stream = BytesIO(body)
    image = Image.open(stream).convert("RGB")
    stream.close()

    # extract post its
    extractor = PostItExtractor(False)
    post_its = extractor.image_to_post_its(image)

    # return post its
    return post_it_class_convert(post_its)


def post_it_class_convert(post_its):
    output = []
    for post in post_its:
        obj = PostIt(str(uuid.uuid4()), post.text, "color", Coordinate(post.rect[0], post.rect[1]),
                     post.rect[2], post.rect[3])
        output.append(obj)

    return output
