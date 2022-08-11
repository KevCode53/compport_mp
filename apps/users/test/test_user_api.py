from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
  """Test the users API (public)"""


  def setUp(self):
    self.client = APIClient()


  def test_create_valid_user_success(self):
    """Test creating user with valid payload is successful"""
    payload = {
        'email': 'test@gmail.com',
        'username': 'test',
        'password': 'testpassAbc123',
        'name': 'Test name'
      }

    response = self.client.post(CREATE_USER_URL, payload)

    # Check that the response is successful
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    user = get_user_model().objects.get(**response.data)
    self.assertTrue(user.check_password(payload['password']))
    self.assertNotIn('password', response.data)


  def test_user_exists(self):
    """Test creating a user that already exists fails"""
    payload = {
        'email': 'test@gmail.com',
        'username': 'test',
        'password': 'testpassAbc123',
        'name': 'Test name'
      }

    create_user(**payload)

    response = self.client.post(CREATE_USER_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


  def test_password_too_short(self):
    """Test that the password must be more than 5 characters"""
    payload = {
        'email': 'test@gmail.com',
        'username': 'test',
        'password': 'pw',
        'name': 'Test name'
      }

    response = self.client.post(CREATE_USER_URL, payload)

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    user_exists = get_user_model().objects.filter(
      email=payload['email']
    ).exists()

    self.assertFalse(user_exists)


# -*-*-*-*-*-*-*-*-* Token test area *-*-*-*-*-*-*-*-*-
  
  
  def test_create_token_for_user(self):
    """Test that a token is created for the user"""
    payload = {
        'email': 'test@gmail.com',
        'password': 'testpassAbc123'
      }

    create_user(email='test@gmail.com', username='test', password='testpassAbc123')

    response = self.client.post(TOKEN_URL, payload)

    self.assertIn('token', response.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
  

  def test_create_token_invalid_credentials(self):
    """Test that token is not created if invalid credentials are given"""
    create_user(email='testuser@gmail.com', username='testuser', name='user', password='testpassAbc123')
    payload = {
      'email':'testuser@gmail.com',
      'password':'wrong',
    }

    response = self.client.post(TOKEN_URL, payload)

    self.assertNotIn('token', response.data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
  

  def test_create_token_no_user(self):
    """Test that token is not created if user doesn't exist"""
    payload = {
        'email': 'test@gmail.com',
        'password': 'testpassAbc123',
      }

    response = self.client.post(TOKEN_URL, payload)

    self.assertNotIn('token', response.data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
  

  def test_create_token_missing_field(self):
    """Test that email and password are required"""
    
    response = self.client.post(TOKEN_URL, {'email': 'one', 'password': 'two'})

    self.assertNotIn('token', response.data)
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)