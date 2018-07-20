# "python main.py" should execute the pipline and output the wanted pdf file
from core.get_original_data import DjangoDataSource


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

    
if __name__ == "__main__":
    queryset = [QuerySet(), QuerySet(), QuerySet()]
    get_data = DjangoDataSource.get_data_from("django")
    print(get_data(queryset=queryset))
    
