clear

pip3 install django

@SET /P pname="請輸入專案名稱: " 
@echo 你輸入的是：%pname%

pstartloop:
@set pstart="Y"
@SET /P pstart="自動開始執行專案([Y]/N)? "
if pstart!="Y" || pstart!="N":
    goto pstartloop

django-admin startproject %pname%

cd %pname%

py manage.py startapp members

if %pstart%=="Y":
    py manage.py runserver
