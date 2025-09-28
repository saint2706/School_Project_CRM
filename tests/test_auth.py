import unittest
import os
from run import app, db
from app.models import User, RoleEnum

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register(self):
        response = self.app.post('/auth/register', data=dict(
            username='testuser',
            password='password',
            password2='password',
            role='SALESMAN'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Congratulations, you are now a registered user!', response.data)
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.role, RoleEnum.SALESMAN)

    def test_login_logout(self):
        # First, register a user
        user = User(username='testuser', role=RoleEnum.ADMIN)
        user.set_password('password')
        db.session.add(user)
        db.session.commit()

        # Test login
        response = self.app.post('/auth/login', data=dict(
            username='testuser',
            password='password'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Authentication setup complete!', response.data)

        # Test logout
        response = self.app.get('/auth/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Authentication setup complete!', response.data)

if __name__ == '__main__':
    unittest.main()