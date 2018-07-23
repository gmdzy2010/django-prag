# -*- coding: utf-8 -*-
import os
import subprocess
import sys
from conf.configurations import (
    TEMPLATE_PATH,
    TEMPLATE_PATH_RENDERED,
    PACKAGE_NAME,
)
from core.exceptions import PathIllegalException
from multiprocessing import Pool
from jinja2 import Environment, PackageLoader


class HTMLTemplateRender:
    """The HTML template render"""
    templates_path = TEMPLATE_PATH
    output_path = TEMPLATE_PATH_RENDERED
    
    def __init__(self, context_dict, template_code):
        self.context_dict = context_dict
        self.template_code = template_code
        self.rendered_file_path = None
        self.is_render_end = False
        
    @classmethod
    def change_templates_path(cls, new_templates_path):
        """This method supplied interface to change templates directory, if
        necessary, it didn't recommend to change this.
        """
        # TODO: to replace below with a more effective method such as os.F_OK
        if new_templates_path and isinstance(new_templates_path, str):
            cls.templates_path = new_templates_path
        else:
            raise PathIllegalException("The path input is illegal!")
    
    @classmethod
    def change_output_path(cls, new_output_path):
        if new_output_path and isinstance(new_output_path, str):
            cls.templates_path = new_output_path
        else:
            raise PathIllegalException("The path input is illegal!")

    @staticmethod
    def _name(separator, path, name, suffix):
        return "%s%s%s.%s" % (separator, path, name, suffix)

    def _render_context(self, barcode, context_dict):
        env = Environment(loader=PackageLoader(PACKAGE_NAME, 'templates'))
        template_handler = env.get_template("%s.html" % self.template_code)
        html_handler = template_handler.render(context_dict=context_dict)
        html_name = "%s/%s.html" % (self.templates_path, barcode)
        with open(html_name, "w", encoding="utf-8") as file_handler:
            file_handler.write(html_handler)
    
    def render_context_to_html(self):
        """This method used multiprocessing package to accelerate the process
        of rendering those ORM objects of django queryset into respective HTML
        templates. The async process method was applied.
        """
        pool = Pool(processes=len(self.context_dict))
        for barcode, context in self.context_dict.items():
            pool.apply(self._render_context, args=(barcode, context))
        pool.close()
        pool.join()
        self.is_render_end = True

    def render_context_to_html_async(self):
        """The async version of method "render_context"."""
        pool = Pool(processes=len(self.context_dict))
        for barcode, context in self.context_dict.items():
            pool.apply_async(self._render_context, args=(barcode, context))
        pool.close()
        pool.join()
        self.is_render_end = True
    
    def get_terminal_command(self, **kwargs):
        command_list = ["wkhtmltopdf"]
        for key, value in kwargs.items():
            command_list.extend([key, value])

    def convert_html_to_pdf(self, if_keeps_html=False):
        """This method used multiprocessing package to accelerate the process
        of rendering those ORM objects of django queryset into respective HTML
        templates. The async process method was applied.
        """
        sep = "\\" if sys.platform == "win32" else "/"
        for barcode, context in self.context_dict.items():
            html_name = self._name(self.templates_path, sep, barcode, "html")
            pdf_name = self._name(self.output_path, sep, barcode, "pdf")
            child = subprocess.Popen([
                "wkhtmltopdf",
                "--disable-smart-shrinking",
                "--dpi", "96",
                "--page-width", "210mm",
                "--page-height", "297mm",
                "--log-level", "none",
                "--margin-top", "0mm",
                "--margin-bottom", "0mm",
                "--margin-left", "0mm",
                "--margin-right", "0mm",
                html_name, pdf_name
            ])
            child.wait()
            
            # if "if_keeps_html" is set to True, the rendered html file will be
            # saved permanently, This may lead to the WASTING OF STORAGE.
            if not if_keeps_html and os.access(html_name, os.F_OK):
                os.remove(html_name)
