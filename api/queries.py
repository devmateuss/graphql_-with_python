from .models import Post
from ariadne import convert_kwargs_to_snake_case

@convert_kwargs_to_snake_case
def listPosts_resolver(obj, info):
    try:
        posts = [post.to_dict() for post in Post.query.all()]
        payload = {
            "success": True,
            "posts": posts
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    print(payload)
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        post = Post.query.filter_by(id=id)
        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Post item matching {id} not found"]
        }
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver_by_title(obj, info, title):
    try:
        post = Post.query.filter_by(title=title).first()

        payload = {
            "success": True,
            "post": post.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Post item matching {title} not found"]
        }
    return payload