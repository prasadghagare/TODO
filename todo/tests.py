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
        response = tester.post('/', data= {'item_text': 'my list'})
        item = Item.query.filter_by(text = 'my list').first()
        print "items is", item.text
        self.assertEquals(item.text ,'my list')
        self.assertEquals(response.location, 'http://localhost/')

class ItemModelTest(unittest.TestCase):

    def test_saving_and_retreiving_items(self):
        first_item = Item("The first (ever) list item")
        second_item = Item("the second item")
        #first_item_string = first_item
        self.assertEquals(str(first_item), "The first (ever) list item")
        self.assertEquals(str(second_item), 'the second item')


if __name__ == '__main__':
    unittest.main()
