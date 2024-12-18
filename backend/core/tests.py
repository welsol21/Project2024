# core/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class FirebaseModelsTests(APITestCase):
    def setUp(self):
        # Create a user and authenticate with JWT token
        self.user = User.objects.create_user(username='testuser', password='testpass')
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')

    def test_client_crud_operations(self):
        # Create a client
        create_url = reverse('client-list-create')
        data = {"name": "Test Client", "fund_manager_id": 1}
        response = self.client.post(create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client_id = response.data['client_id']

        # Retrieve the client
        retrieve_url = reverse('client-detail', args=[client_id])
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Client")

        # Update the client
        update_data = {"name": "Updated Test Client", "fund_manager_id": 1}
        response = self.client.put(retrieve_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Test Client")

        # Delete the client
        response = self.client.delete(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_fund_crud_operations(self):
        # Create a fund
        create_url = reverse('fund-list-create')
        data = {"name": "Test Fund", "user_id": 1}
        response = self.client.post(create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        fund_id = response.data['fund_id']

        # Retrieve the fund
        retrieve_url = reverse('fund-detail', args=[fund_id])
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Fund")

        # Update the fund
        update_data = {"name": "Updated Test Fund", "user_id": 1}
        response = self.client.put(retrieve_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Test Fund")

        # Delete the fund
        response = self.client.delete(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_portfolio_crud_operations(self):
        # Create a portfolio
        create_url = reverse('portfolio-list-create')
        data = {"name": "Test Portfolio", "fund_id": "some_fund_id"}
        response = self.client.post(create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        portfolio_id = response.data['portfolio_id']

        # Retrieve the portfolio
        retrieve_url = reverse('portfolio-detail', args=[portfolio_id])
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Portfolio")

        # Update the portfolio
        update_data = {"name": "Updated Test Portfolio", "fund_id": "some_fund_id"}
        response = self.client.put(retrieve_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Test Portfolio")

        # Delete the portfolio
        response = self.client.delete(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_asset_crud_operations(self):
        # Create an asset
        create_url = reverse('asset-list-create')
        data = {"symbol": "AAPL", "price": 150.0, "volume": 1000, "amount": 10, "portfolio_id": "some_portfolio_id"}
        response = self.client.post(create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        asset_id = response.data['asset_id']

        # Retrieve the asset
        retrieve_url = reverse('asset-detail', args=[asset_id])
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['symbol'], "AAPL")

        # Update the asset
        update_data = {"symbol": "AAPL", "price": 155.0, "volume": 1000, "amount": 10, "portfolio_id": "some_portfolio_id"}
        response = self.client.put(retrieve_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['price'], 155.0)

        # Delete the asset
        response = self.client.delete(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_order_crud_operations(self):
        # Create an order
        create_url = reverse('order-list-create')
        data = {"order_type": "buy", "amount": 5, "portfolio_id": "some_portfolio_id"}
        response = self.client.post(create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        order_id = response.data['order_id']

        # Retrieve the order
        retrieve_url = reverse('order-detail', args=[order_id])
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['order_type'], "buy")

        # Update the order
        update_data = {"order_type": "buy", "amount": 10, "portfolio_id": "some_portfolio_id"}
        response = self.client.put(retrieve_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['amount'], 10)

        # Delete the order
        response = self.client.delete(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_trade_rating_crud_operations(self):
        # Create a trade rating
        create_url = reverse('trade-rating-list-create')
        data = {"rating": 4.5, "order_id": "some_order_id"}
        response = self.client.post(create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        trade_rating_id = response.data['trade_rating_id']

        # Retrieve the trade rating
        retrieve_url = reverse('trade-rating-detail', args=[trade_rating_id])
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rating'], 4.5)

        # Update the trade rating
        update_data = {"rating": 5.0, "order_id": "some_order_id"}
        response = self.client.put(retrieve_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['rating'], 5.0)

        # Delete the trade rating
        response = self.client.delete(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_ai_forecast_crud_operations(self):
        # Create an AI forecast
        create_url = reverse('ai-forecast-list-create')
        data = {"forecast": "Positive", "user_id": self.user.id}
        response = self.client.post(create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        forecast_id = response.data['forecast_id']

        # Retrieve the AI forecast
        retrieve_url = reverse('ai-forecast-detail', args=[forecast_id])
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['forecast'], "Positive")

        # Update the AI forecast
        update_data = {"forecast": "Negative", "user_id": self.user.id}
        response = self.client.put(retrieve_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['forecast'], "Negative")

        # Delete the AI forecast
        response = self.client.delete(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_support_request_crud_operations(self):
        # Create a support request
        create_url = reverse('support-request-list-create')
        data = {"request": "Need help", "user_id": self.user.id}
        response = self.client.post(create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        support_request_id = response.data['support_request_id']

        # Retrieve the support request
        retrieve_url = reverse('support-request-detail', args=[support_request_id])
        response = self.client.get(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['request'], "Need help")

        # Update the support request
        update_data = {"request": "Updated request for assistance", "user_id": self.user.id}
        response = self.client.put(retrieve_url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['request'], "Updated request for assistance")

        # Delete the support request
        response = self.client.delete(retrieve_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class APITestAuthorization(APITestCase):
    def setUp(self):
        # Create a user for testing authorization
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.auth_url = reverse('token_obtain_pair')
        self.register_url = reverse('register')
        self.asset_url = reverse('asset-list-create')

    def test_registration_access_without_auth(self):
        # Access registration endpoint without authorization
        response = self.client.post(self.register_url, {
            "username": "newuser",
            "password": "newpass",
            "role": "fund_admin"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_access_protected_endpoint_without_auth(self):
        # Remove authorization token and attempt to access a protected endpoint
        response = self.client.get(self.asset_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_protected_endpoint_with_auth(self):
        # Obtain token for the user
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {str(refresh.access_token)}')
        
        # Access protected endpoint with authorization
        response = self.client.get(self.asset_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
