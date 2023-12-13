from django.contrib.auth.models import BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        user = self.model(email=email, username=username)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)

        user.is_admin = True

        user.is_staff = True

        user.is_superuser = True

        user.is_active = True

        user.save(using=self._db)

        return user
