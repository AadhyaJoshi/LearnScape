import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_homepage_view(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200