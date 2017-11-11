import unittest
from flask import request
from todo.models import Item, List
from todo import creat_app,db
import tempfile , os, time

class HomePageTest(unittest.TestCase):


    def setUp(self):
        self.app = creat_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

class ListAndItemModelsTest(unittest.TestCase):

    def setUp(self):
        self.app = creat_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_saving_and_retreiving_items(self):
        list_ = List()

        first_item = Item(text = "The first (ever) list item", list_if = list_)
        second_item = Item(text = "the second item", list_if = list_)

        first_item.list = list_

        self.assertEquals(first_item.text, "The first (ever) list item")
        self.assertEquals(second_item.text, 'the second item')

        self.assertEquals(first_item.list, list_)

class ListViewTest(unittest.TestCase):

    def setUp(self):
        self.app = creat_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_displays_only_items_for_that_list(self):
        db.create_all()
        tester = self.app.test_client(self)
        tester.post('/lists/new', data= {'item_text': 'itemey 1'})
        tester.post('/lists/new', data= {'item_text': 'itemey 2'})

        response_1 = tester.get('/lists/1')

        response_2 = tester.get('/lists/2')

        if not (response_1.data.find("itemey 1") > 0 and response_2.data.find("itemey 2") > 0):
            self.fail('items not inserted')

class NewListTestCase(unittest.TestCase):

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
        tester.post('/lists/new', data= {'item_text': 'my list'})
        item = Item.query.filter_by(text = 'my list').first()
        self.assertEquals(item.text ,'my list')

    def test_redirect_after_post(self):
        db.create_all()
        tester = self.app.test_client(self)
        response = tester.post('/lists/new', data= {'item_text': 'my list'})
        self.assertEquals(response.status_code,302)
        self.assertEquals(response.location, 'http://localhost/lists/1')

class NewItemTest(unittest.TestCase):

    def setUp(self):
        self.app = creat_app('test')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_can_save_POST_request_to_existing_list(self):
        db.create_all()
        tester = self.app.test_client(self)
        tester.post('/lists/new', data= {'item_text': 'my list'})
        tester.post('/lists/1/add_item', data= {'item_text': 'a new item in existing list'})
        response_1 = tester.get('/lists/1')
        if not (response_1.data.find("my list") > 0 and response_1.data.find("a new item in existing list") > 0):
            self.fail('items not inserted')

if __name__ == '__main__':
    unittest.main()
