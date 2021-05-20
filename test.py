'''
    Test cases with positive and negative scenarios
'''
import unittest
from app import app

class testFlaskApp(unittest.TestCase):
    #200 status code/ Positive scenarios
    def test_get(self):
        client=app.test_client(self)
        response=client.get('/song/1')
        self.assertEqual(response.status_code,200)
    
    def test_delete(self):
        client=app.test_client(self)
        response= client.get('/delete/song/1')
        self.assertEqual(response.status_code,200)
    
    def test_update(self):
        client=app.test_client(self)
        response= client.post('/update/song/2',data={'meta':'{"name":"2012"}'})
        self.assertEqual(response.status_code,200)

    def test_insert(self):
        client=app.test_client(self)
        response= client.post('/insert',data={'audioFileType':'song','meta':'{"ID":3,"Name":"dil to pagal hai","duration":"111"}'})
        self.assertEqual(response.status_code,200)
    
    #check content return is 'text/html; charset=utf-8'
    def test_get_content_type(self):
        client=app.test_client(self)
        response=client.get('/song/1')
        self.assertEqual(response.content_type,'text/html; charset=utf-8')
    
    def test_delete_content_type(self):
        client=app.test_client(self)
        response= client.get('/delete/song/1')
        self.assertEqual(response.content_type,'text/html; charset=utf-8')
    
    
    def test_update_content_type(self):
        client=app.test_client(self)
        response= client.post('/update/song/2',data={'meta':'{"name":"2012"}'})
        self.assertEqual(response.content_type,'text/html; charset=utf-8')
    
    def test_insert(self):
        client=app.test_client(self)
        response= client.post('/insert',data={'audioFileType':'song','meta':'{"ID":3,"Name":"dil to pagal hai","duration":"111"}'})
        self.assertEqual(response.content_type,'text/html; charset=utf-8')
    
    #negative scenarios
    def test_get_wrong_id(self):
        client=app.test_client(self)
        response=client.get('/song/none')
        self.assertNotEqual(response.status_code,200)
    
    def test_delete_wrong_id(self):
        client=app.test_client(self)
        response= client.get('/delete/song/none')
        self.assertNotEqual(response.status_code,200)
    
    def test_update_wrong_id(self):
        client=app.test_client(self)
        response= client.post('/update/song/none',data={'meta':'{"name":"2012"}'})
        self.assertNotEqual(response.status_code,200)

    def test_insert_wrong_id(self):
        client=app.test_client(self)
        response= client.post('/insert',data={'audioFileType':'song','meta':'{"ID":3,"Name":"dil to pagal hai","duration":"111"}'})
        print(response)
        self.assertNotEqual(response.status_code,200)

if __name__=="__main__":
    unittest.main()