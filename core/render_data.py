import os
import subprocess
from jinja2 import Environment, PackageLoader


class BaseTemplatesRender:
    """The HTML template render"""
    templates_path = ""
    output_path = ""
    
    def __init__(self, context_dict, template_code):
        self.context_dict = context_dict
        self.template_code = template_code
    
    def get_template(self):
        pass
    
    def get_context_dict(self):
        pass
    
    @classmethod
    def change_templates_path(cls, new_path):
        pass
    
    @classmethod
    def change_output_path(cls, new_path):
        pass
    
    def render_context(self):
        pass


class HTML2PDFRender(BaseTemplatesRender):
    """This subclass contains method to render html file to PDF file"""
    
    def __init__(self, context_dict, template_code, **kwargs):
        self.extra_context = kwargs
        super(HTML2PDFRender, self).__init__(context_dict, template_code)
    
    def render_context(self):
        pass



