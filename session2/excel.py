import pyexcel
a_list_of_dictionaries = [
    {
        'title': 'Su-25',
        'link' :'http://dantri.com.vn'
    },
    {
        'title': 'Bo may',
        'link' :'http://google.com.vn'
    },
    {
        'title': 'Me may',
        'link' :'http://dantri.com.vn'
    },
    {
        'title': 'Em may',
        'link' :'http://dantri.com.vn'
    },
]
pyexcel.save_as(records = a_list_of_dictionaries, dest_file_name = 'your_file.xls')
