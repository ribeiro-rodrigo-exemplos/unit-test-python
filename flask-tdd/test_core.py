from app import meu_web_app

import unittest

class TestHomeView(unittest.TestCase):
    '''
      Como todos os 3 casos de teste fazem um get na home "/"
      da nossa aplicacao, definimos a funcao setUp. Ela e executada
      automaticamente sempre que o Pytest instancia a classe TestHomeView.
      A funcao setUp e semelhante a um metodo construtor.
    '''

    def setUp(self) -> None:
        app = meu_web_app.test_client()
        self.response = app.get('/')

    # Testamos se a resposta é 200 (OK)
    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    # Testamos se a nossa home retorna a string ok
    def test_html_string_response(self):
        self.assertEqual("ok", self.response.data.decode('utf-8'))

    # Testamos se o content_type da resposta da home está correto
    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)