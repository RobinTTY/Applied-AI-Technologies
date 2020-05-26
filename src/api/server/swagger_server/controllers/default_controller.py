import connexion
import six

from swagger_server.models.post_it import PostIt  # noqa: E501
from swagger_server import util


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
        body = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
