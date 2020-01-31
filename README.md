Steps:

1.Clone/pull/download 這個 repository

2.使用 virtualenv env 來建立你的虛擬環境 並且使用 pip install -r requirements.txt 來安裝你的依賴套件

3.設定你的 .env 變數

4.使用 python manage.py rename <newprojectname> 來修改你的專案名稱


…or create a new repository on the command line

echo "# django_template" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/ryowuandjanet/django_template.git
git push -u origin master

…or push an existing repository from the command line

git remote add origin https://github.com/ryowuandjanet/django_template.git
git push -u origin master
