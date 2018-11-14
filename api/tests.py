from django.test import TestCase
from .models import Program, Week, Page
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """This class defines the test suite for the program model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user = User.objects.create(username="nerd")

        self.program_name = "Mindfulness"
        self.program = Program(name=self.program_name, owner=self.user)

    def test_model_can_create_a_program(self):
        """Test the program model can create a program."""
        old_count = Program.objects.count()
        self.program.save()
        new_count = Program.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_model_can_create_a_week(self):
        """Test the week model can create a week."""
        self.program.save()

        old_count = Week.objects.count()

        self.week_name = "Week 1"
        self.week = Week(name=self.week_name, owner=self.user)
        self.week.save()

        self.week_2_name = "Week 2"
        self.week_2 = Week(name=self.week_2_name, owner=self.user)
        self.week_2.save()
        
        new_count = Week.objects.count()
        self.assertNotEqual(old_count, new_count)

        self.program.weeks.add(self.week, self.week_2)
        self.program.save()

    # def test_model_can_create_a_week_with_pages(self):
    #     """Test the week model can create a week."""
    #     self.program.save()

    #     self.week_name = "Week 1"
    #     self.week = Week(name=self.week_name,  owner=self.user)
    #     self.week.save()

    #     old_count = Page.objects.count()
    #     self.page = Page(name="Page 1", 
    #         audio="http://google.com/audio",
    #         video="http://google.com/video",
    #         article="http://google.com/article",
    #         question="http://google.com/question",
    #         form="http://google.com/form",
    #         week=self.week,
    #         owner=self.user
    #     )
    #     self.page.save()
    #     self.page2 = Page(name="Page 2", 
    #         audio="http://google.com/audio",
    #         video="http://google.com/video",
    #         article="http://google.com/article",
    #         question="http://google.com/question",
    #         form="http://google.com/form",
    #         week=self.week,
    #         owner=self.user
    #     )
    #     self.page2.save()
    #     new_count = Page.objects.count()
    #     self.assertNotEqual(old_count, new_count)
    #     self.assertEqual(self.page.week, self.page2.week)

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.week_name = "Week 1"
        self.week = Week(name=self.week_name, owner=user)
        self.week.save()

        self.week_2_name = "Week 2"
        self.week_2 = Week(name=self.week_2_name, owner=user)
        self.week_2.save()

        # Since user model instance is not serializable, use its Id/PK
        self.program_data = {'name': 'Modern Health Program', 'owner': user.id, 'weeks': [self.week.id, self.week_2.id]}
        self.response = self.client.post(
            reverse('createProgram'),
            self.program_data,
            format="json")

    def test_api_can_create_a_program(self):
        """Test the api has program creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/programs/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_can_get_a_program(self):
        """Test the api can get a given program."""
        program = Program.objects.get(id=1)
        response = self.client.get(
            '/programs/',
            kwargs={'pk': program.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, program)

    # def test_api_can_update_program(self):
    #     """Test the api can update a given program."""
    #     program = Program.objects.get()
    #     change_program = {'name': 'Something new'}
    #     res = self.client.put(
    #         reverse('details', kwargs={'pk': program.id}),
    #         change_program, format='json'
    #     )
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_program(self):
        """Test the api can delete a program."""
        program = Program.objects.get()
        response = self.client.delete(
            reverse('detailsProgram', kwargs={'pk': program.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)