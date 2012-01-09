import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):    
    def get(self):
        template_values={}
        path = os.path.join(os.path.dirname(__file__), 'acercaDe.html')
        self.response.out.write(template.render(path, template_values))

class AcercaDe(webapp.RequestHandler):
    def get(self):
        template_values={}
        path=os.path.join(os.path.dirname(__file__),'acercaDe.html')
        self.response.out.write(template.render(path, template_values))

class Actividad7(webapp.RequestHandler):
    def get(self):
        template_values={}
        path=os.path.join(os.path.dirname(__file__),'actividad7.html')
        self.response.out.write(template.render(path, template_values))

class Actividad9(webapp.RequestHandler):
    def get(self):
        template_values={}
        path=os.path.join(os.path.dirname(__file__),'Actividad9.html')
        self.response.out.write(template.render(path, template_values))

class Actividad11(webapp.RequestHandler):
    def get(self):
        template_values={}
        path=os.path.join(os.path.dirname(__file__),'actividad11.html')
        self.response.out.write(template.render(path, template_values))

class Actividad13(webapp.RequestHandler):
    def get(self):
        template_values={}
        path=os.path.join(os.path.dirname(__file__),'Actividad13.html')
        self.response.out.write(template.render(path, template_values))

class Actividad15(webapp.RequestHandler):
    def get(self):
        template_values={}
        path=os.path.join(os.path.dirname(__file__),'Actividad15.html')
        self.response.out.write(template.render(path, template_values))
        
class Actividad17(webapp.RequestHandler):
    def get(self):
        template_values={}
        path=os.path.join(os.path.dirname(__file__),'Actividad17.html')
        self.response.out.write(template.render(path, template_values))
        
class Preguntas(webapp.RequestHandler):
    def get(self):
        template_values={}
        path=os.path.join(os.path.dirname(__file__),'Preguntas.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/index.html',MainPage),
                                      ('/acercaDe.html',AcercaDe),
                                      ('/actividad7.html',Actividad7),
                                      ('/Actividad9.html',Actividad9),
                                      ('/Actividad11.html',Actividad11),
                                      ('/Actividad13.html',Actividad13),
                                      ('/Actividad15.html',Actividad15),
                                      ('/Actividad17.html',Actividad17),
                                      ('/Preguntas.html',Preguntas)
                                      ], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
