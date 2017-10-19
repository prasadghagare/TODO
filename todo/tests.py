import unittest
from flask import request
from todo.models import Item
from todo import creat_app,db
import tempfile , os

class HomePageTest(unittest.TestCase):


    def setUp(self):
        self.app = creat_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_can_save_Post_request(self):
        db.create_all()
        tester = self.app.test_client(self)
        tester.post('/', data= {'item_text': 'my list'})
        item = Item.query.filter_by(text = 'my list').first()
        self.assertEquals(item.text ,'my list')

    def test_redirect_after_post(self):
        db.create_all()
        tester = self.app.test_client(self)
        response = tester.post('/', data= {'item_text': 'my list'})
        self.assertEquals(response.status_code,302)
        self.assertEquals(response.location, 'http://localhost/lists/the-only-list-in-the-world')

class ItemModelTest(unittest.TestCase):

    def test_saving_and_retreiving_items(self):
        first_item = Item("The first (ever) list item")
        second_item = Item("the second item")
        #first_item_string = first_item
        self.assertEquals(str(first_item), "The first (ever) list item")
        self.assertEquals(str(second_item), 'the second item')

class ListViewTest(unittest.TestCase):

    def setUp(self):
        self.app = creat_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_displays_all_items(self):
        db.create_all()
        tester = self.app.test_client(self)
        tester.post('/', data= {'item_text': 'itemey 1'})
        tester.post('/', data= {'item_text': 'itemey 2'})
        response = tester.get('/lists/the-only-list-in-the-world')
        if not (response.data.find("itemey 1") > 0 and response.data.find("itemey 2") > 0):
            self.fail('items not inserted')

if __name__ == '__main__':
    unittest.main()
