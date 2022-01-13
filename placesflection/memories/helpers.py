from .models import UserSocialMetadata


def update_user_social_metadata(strategy, *args, **kwargs):
    """Updates user social metadata based on api response."""
    response = kwargs["response"]
    backend = kwargs["backend"]
    user = kwargs["user"]

    if response.get("user_photo"):
        metadata = UserSocialMetadata()
        metadata.user = user
        metadata.picture = response["user_photo"]
        metadata.save()
