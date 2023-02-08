# Name : Hamada Sayed Mohamed 
# ID : 621224


# http://192.168.1.5:3335/ Open To browner
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def Rak ():
    put_html('<center> <h3>استماره الطالب المقبول</h3> </center>') .style('background-color:#25316D ; padding:20px; color:gold ;  ')
    put_html('<p>تطبيق ويب لتصدير السيره الذاتية للطلاب المقبولين للدراسه</p>') .style('text-align:center ; font-weight:bold')
    put_html('<center> <img src="https://www.tvdsb.ca/en/schools/resources/Information-for-Grade-8-Students/Info-for-Grade-8-banner.jpg" alt="student imge"></center>').style('')

    data = input_group(
        'ملىْ استماره الطالب المتفوق المؤهل',
        [
            input('اسم الطالب', name='student'),
            input('عنوان الطالب', name='country'),
            input('البريد الالكترونى', name='email'),
            input('رقم الهاتف', name='phone' , type=NUMBER),
            radio('موهلات الطالب' , options=['word','excel','powerpoint'],name='certi'),
            checkbox('اتقان اللغات',options=['Arabic','English','France'] , inline=True , name='lang')
        ],
    )

    imgs = file_upload(
        'تحميل صوره',
        accept='images/*',
        multiple=True
    )

    for img in imgs:
        global rr 
        rr = img['content']


    # show CV
    put_text('student CV')
    put_table([
        ['student img' , 'Name' , 'Address' , 'Phone' , 'Certificate' , 'Language'],
        [put_image(rr).style('width:50px;0,.'),data['student'],data['country'],data['phone'],data['certi'],data['lang']]
    ])

start_server(Rak , port=3335 , debug=True)