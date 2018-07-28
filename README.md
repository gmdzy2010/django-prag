# realbio_prag
The Pipeline of Report Auto-Generations (PRAG) coupled with `wkhtmltopdf`.      
(What's wkhtmltppdf? here: https://github.com/wkhtmltopdf/wkhtmltopdf)      
        
### Introduction
This package supplied interfaces to common data file such as csv, tsv, txt, xls/xlsx using the package of `pandas`, django queryset (lower level to SQL database is coming soon) and stdout data source, and rendered such dataset to pdf file using python template package `jinja2`. To accelerate the pdf-rendering process in bulk, the async multiprocess method in `multiprocessing` is applied.

### Main packages that meant to be used
>1.`multiprocess` or `threading`: this pipeline should use the multiprocess package to improve the efficiency         
>2.`subprocess`: to control the outter binary command of wkhtmltopdf
>2.`jinjia2`: template-parsing frame to deal with the html file    
>3.`pandas`: the data structure which data in html template should store   
>4.to be continued ...      

### What's now
As so far, the key module `get_original_data.py` and `render_data.py` are finished partially, some simple functions test were run and then passed, but no unittest.

### TODO
The next step is to finish the subclass of FileDataSource and StdoutDataSource. 
The arguments of wkhtmltopdf is still fixed and it's not flexible to change the style of pdf generated, so the method `get_command_arguments` need to be done.
### Version
##### v0.8.0 (07/26/2018)
>update README.md about project info
