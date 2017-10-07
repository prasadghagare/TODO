from todo import app
import unittest
from flask import request
from todo.models import Item
from todo import db
import tempfile , os

class HomePageTest(unittest.TestCase):


    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_root_url_resolve_to_view(self):
        return None
        #print app.view_functions
        #self.assertEquals(found, "index")
        #for rule in app.url_map.iter_rules():
            #print "rule",rule, rule.endpoint

    def test_home_page_returns_correct_code(self):
        #tester = app.test_client(self)
        response = self.app.get('/',content_type = 'html/text')
        #print response
        self.assertEquals(response.status_code , 200)

    def test_home_page_returns_correct_html(self):
        #tester = app.test_client(self)

        response = self.app.get('/',content_type = 'html/text')
        print response.data
        self.assertIn('<title>To-Do lists</title>', response.data)

    def test_can_save_Post_request(self):
        #tester = app.test_client(self)
        with app.app_context():
            response = self.app.post('/', data= {'item_text': 'my list'})
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
