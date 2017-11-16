# djangotest
 1.下载后，请将“django小例子的教程.pdf”和“message_form.html”移出去(它们不属于项目)
 2.找到setting.py文件，修改DATABASES中相关数据库配置
 3.cd 到项目目录下(manage.py同级）
 	python manage.py makemigrations 
 	python manage.py migrate
 4.python manage.py runserver
 5.访问http://127.0.0.1:8000/message

