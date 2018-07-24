# realbio_prag
The Pipeline of Report Auto-Generations (PRAG) coupled with `wkhtmltopdf`.      
(What's wkhtmltppdf? here: https://github.com/wkhtmltopdf/wkhtmltopdf)      
        
# introduction
This package supplied interfaces to common data file (including csv, tsv, txt,      
xls/xlsx), `django queryset` (lower level to SQL database is coming soon)       
and stdout data source, and rendered such dataset to pdf file using python      
template package `jinja2`. To accelerate the pdf-rendering process in bulk, the     
async multiprocess method in `multiprocessing` is applied.

### Main packages that meant to be used
>1.`multiprocess` or `threading`: this pipeline should use the multiprocess             
>  package to improve the efficiency               
>2.`jinjia2`: template-parsing frame to deal with the html file    
>3.`pandas`: the data structure which data in html template should store   
    
>4.to be continued ...      
                
>Last edit by gmdzy2010, 07/24/2018, 11:44:54
