from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Memory


# Create your tests here.
def _create_memory(owner, title, description, location):
    return Memory.objects.create(
        owner=owner, title=title, description=description, location=location
    )


class MemoryDetailViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user("temporary", "temporary@gmail.com", "temporary")

    def test__non_existing_memory__returns_404(self):
        """
        The detail view of an unexisting memory returns 404.
        """
        self.client.login(username="temporary", password="temporary")
        url = reverse("details", args=(1,))

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test__with_non_authorised_user__redirects_to_login(self):
        """
        The detail view redirects to the login page for unauthenticated user.
        """
        url = reverse("details", args=(1,))

        response = self.client.get(url)

        self.assertRedirects(
            response,
            "/accounts/login/?next=/memories/1/",
            status_code=302,
            fetch_redirect_response=False,
        )

    def test__with_one_memory__displays_memory(self):
        """
        The detail view displays one memory if it exists.
        """
        url = reverse("details", args=(1,))
        self.client.login(username="temporary", password="temporary")
        _create_memory(
            get_user_model().objects.get(pk=1), "test name", "test description", "1,1"
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test name")
        self.assertContains(response, "test description")
