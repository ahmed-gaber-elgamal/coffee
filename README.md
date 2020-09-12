## Inovola coffee rest framework

### Prerequisite:
    python==3.6.9
    mongo==3.6.3
### Installation
- `git clone https://github.com/ahmed-gaber-elgamal/coffee.git`
- `cd coffee`
- `pip3 install -r requirements.txt`
- `python3 manage.py migrate`
### Database
- `cd inovola-coffee`
- `mongoimport --db inovola-coffee --collection coffee_coffeepod --file 'your_project_path/inovola-coffee/coffee_coffeepod.json'`
- `mongoimport --db inovola-coffee --collection coffee_coffeemachine --file 'your_project_path/inovola-coffee/coffee_coffeemachine.json'`
- `mongoimport --db inovola-coffee --collection auth_user --file 'your_project_path/inovola-coffee/auth_user.json'`
### Running Server
- `python3 manage.py runserver`
###login to django-admin
- go to `http://localhost:8000/admin/`
- username: `inovola`
- Password: `inovola`
