from hello.ola import OlaMundo
import unittest

class TestOlaMundo(unittest.TestCase):

    def test_dizOla(self):
        ola = OlaMundo()
        self.assertEqual(ola.dizOla(), "Ola mundo!")