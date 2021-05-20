import unittest
from app import app

class testFlaskApp(unittest.TestCase):
    #200 status code
    def test_getRecord(self):
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
        print(response)
        self.assertEqual(response.status_code,200)

    def test_insert(self):
        client=app.test_client(self)
        response= client.post('/insert',data={'audioFileType':'song','meta':'{"ID":3,"Name":"dil to pagal hai","duration":"111"}'})
        print(response)
        self.assertEqual(response.status_code,200)
    
if __name__=="__main__":
    unittest.main()