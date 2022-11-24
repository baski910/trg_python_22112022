import os
import json
import unittest
from app import db,create_app

# setUp
# tearDown

class BookTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_pyfile("configtest.py")
        self.client = self.app.test_client
        self.book = {'title':'programming in python'}

        with self.app.app_context():
            db.create_all()


    def test_creat_book(self):
        res = self.client().post('/booklists',data = self.book)
        self.assertEqual(res.status_code, 201)
        self.assertIn('programming in python', str(res.data))

    def test_get_all_books(self):
        res = self.client().post('/booklists',data = self.book)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/booklists')
        self.assertEqual(res.status_code, 200)
        self.assertIn('programming in python', str(res.data))

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()



