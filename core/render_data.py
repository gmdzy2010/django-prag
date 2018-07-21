import os
from  multiprocessing import Pool
from core.exceptions import PathIllegalException
from jinja2 import Environment, PackageLoader


class BaseTemplatesRender:
    """The HTML template render"""
    templates_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "templates"
    )
    output_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "templates"
    )
    
    def __init__(self, context_dict, template_code):
        self.context_dict = context_dict
        self.template_code = template_code
        self.logger = self.set_logger()
        self.rendered_file_path = None
        self.is_render_end = False
        
    def get_context_dict(self):
        return self.context_dict
    
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
    
    def _render_context(self, barcode, context_dict):
        env = Environment(loader=PackageLoader('realbio_prag', 'templates'))
        template_handler = env.get_template(
            "template_%s.html" % self.template_code
        )
        html_handler = template_handler.render(context_dict=context_dict)
        with open("%s/%s.html" % (self.output_path, barcode), "w") as handler:
            handler.write(html_handler)
    
    def render_context(self):
        """This method used multiprocessing package to accelerate the process
        of rendering those ORM objects of django queryset into respective HTML
        templates. The async process method was applied.
        """
        pool = Pool(processes=len(self.context_dict))
        for barcode, context in self.context_dict.items():
            pool.apply_async(self._render_context, args=(barcode, context))
        pool.close()
        pool.join()
        self.is_render_end = True
    
    def set_logger(self):
        pass


class HTML2PDFRender:
    """This class contains method to render html file to PDF file"""
    
    def __init__(self, **kwargs):
        self.extra_context = kwargs
    
    def render_context(self):
        pass
