# -*- coding: utf-8 -*-
from core.get_original_data import django_data_source
from core.render_data import HTMLTemplateRender


class QuerySet:
    """
    for test queryset of django queryset interface
    """
    birthday = "1990/06/24"
    check_date = "2018/07/19"
    code = "V20180720"
    contact = 13003672642
    gender = 1
    name = "Refactor Man"
    result = "negative"
    report_date = "2018/07/20"
    score = 666
    send_date = "2018/07/10"
    KRAS_mutation_rate = 0.05
    BMP3_methylation_rate = 0.01
    NDRG4_methylation_rate = 0.07
    
    def __init__(self, code):
        self.code = code

    
if __name__ == "__main__":
    queryset = [
        QuerySet("CYS180000001"),
        QuerySet("CYS180000002"),
    ]
    context_dict = django_data_source(queryset=queryset)
    template_render = HTMLTemplateRender(context_dict, "MEIYIN001")
    template_render.render_context_to_html()
    template_render.convert_html_to_pdf(if_keeps_html=True)
