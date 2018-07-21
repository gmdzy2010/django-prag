from core.get_original_data import django_data_source
from core.render_data import HTMLTemplateRender


class QuerySet:
    """
    for test queryset of django queryset interface
    """
    birthday = "1990/06/24"
    check_date = "2018/07/19"
    code = "V20180720"
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
    queryset = [QuerySet("TEST001"), QuerySet("TEST002"), QuerySet("TEST003")]
    context_dict = django_data_source(queryset=queryset)
    template_render = HTMLTemplateRender(context_dict, "MEIYIN001")
    template_render.render_context() 
