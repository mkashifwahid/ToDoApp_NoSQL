from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
  

    def test_get_all_tasks(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertTrue('Stranger' in response.get_data(as_text=True))

    def test_get_one_task(self):
        tester = app.test_client(self)
        response = tester.get('', content_type='html/css')
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        tester = app.test_client(self)
        response = tester.post('', content_type='html/css')
        self.assertEqual(response.status_code, 200)        

    def test_delete_task(self):
        tester = app.test_client(self)
        response = tester.get('', content_type='html/css')
        self.assertEqual(response.status_code, 200)        

    def test_complete_task(self):
        tester = app.test_client(self)
        response = tester.get('', content_type='html/css')
        self.assertEqual(response.status_code, 200)      

    #def test_complete_task(self):
     #   tester = app.test_client(self)
      ##  response = tester.get('', content_type='html/css')
        #self.assertEqual(response.status_code, 200)      


if __name__ == '__main__':
    unittest.main()