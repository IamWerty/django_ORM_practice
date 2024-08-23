import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_ORM.settings")
django.setup()

from users_and_roles.models import Role, User
from tasks.models import Status, Task

role_admin = Role.objects.get_or_create(role_type = "admin")[0]
role_user = Role.objects.get_or_create(role_type="user")[0]

admin = User.objects.get_or_create(
    name = "Johny",
    email = "bigJohn@gmail.com",
    role = role_admin
)[0]

user = User.objects.get_or_create(
    name = "Billy",
    email = "JustBill@gmail.com",
    role = role_user
)[0]

status_in_progress = Status.objects.get_or_create()

task1 = Task.objects.get_or_create(
    title = "погудувати кота",
    describtion = "",
    user = admin
)[0]