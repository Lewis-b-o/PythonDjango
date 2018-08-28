from django.test import TestCase
from django.test import Client
from .forms import *
from .views import *
# import all forms
# Create your tests here.


class TitleTest(TestCase):
    # Testing the getpagetitle method to ensure the page title retrieves the correct product name
    def test_change_page_title(self):
        """Total should not return correct total"""
        self.assertEqual(getpagetitle(name="Ralph Lauren"), "Ralph Lauren - LSBD")

    def test_change_page_title_positive(self):
        """Total should not return correct total"""
        self.assertEqual(getpagetitle(name="Nike"), "Nike - LSBD")

    def test_change_page_title_negative(self):
        """Total should not return correct total"""
        self.assertNotEqual(getpagetitle(name="Bobby"), "LSBD - Bobby")


class SignUpFormTest(TestCase):
    # Testing SignUp form validation
    def test_userform_failed_password(self):
        """ Testing invalid password validation """
        form = SignUp(data={'email': "test@test.com", 'username': "testing", 'password1': "P@ass", 'password2': "P@ass"})
        self.assertFalse(form.is_valid())

    def test_userform_failed_email(self):
        """ Testing invalid email address missing '@' """
        form = SignUp(data={'email': "test", 'username': "testing", 'password1': "P@assWord123", 'password2': "P@ass"})
        self.assertFalse(form.is_valid())

    def test_userform_failed_password_match(self):
        """ Testing mismatch in password fields """
        form = SignUp(data={'email': "test@test.com", 'username': "testing", 'password1': "P@assWord123", 'password2': "P@ass"})
        self.assertFalse(form.is_valid())

    def test_userform_valid(self):
        """ Testing all valid input values into form """
        form = SignUp(data={'email': "test@test.com", 'username': "testing", 'password1': "P@assWord123", 'password2': "P@assWord123"})
        self.assertTrue(form.is_valid())

    def test_userform_failed_email_missing(self):
        """ Testing the form fails when email field is missing """
        form = SignUp(data={'username': "testing", 'password1': "P@assWord123", 'password2': "P@assWord123"})
        self.assertFalse(form.is_valid())

    def test_userform_invalid_email(self):
        """ Test the max length email address field - Input: 261 characters """
        form = SignUp(data={'email': "testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest@test.com", 'username': "testing", 'password1': "P@assWord123", 'password2': "P@assWord123"})
        self.assertFalse(form.is_valid())


class AuthenticationFormTest(TestCase):

    def setUp(self):
        User.objects.create(username='testuser')

    def test_auth_form_valid(self):
        user = User.objects.get(username='testuser')
        user.set_password('testpassword12345')
        user.save()
        form = AuthenticationForm(data={'username': "testuser", 'password': "testpassword12345"})
        print(form)
        self.assertTrue(form.is_valid())

    def test_auth_form_invalid_password(self):
        user = User.objects.get(username='testuser')
        user.set_password('testpassword12345')
        user.save()
        form = AuthenticationForm(data={'username': "testuser", 'password': "testpassword"})
        print(form)
        self.assertFalse(form.is_valid())

    def test_auth_form_invalid_username(self):
        user = User.objects.get(username='testuser')
        user.set_password('testpassword12345')
        user.save()
        form = AuthenticationForm(data={'username': "test", 'password': "testpassword12345"})
        print(form)
        self.assertFalse(form.is_valid())
