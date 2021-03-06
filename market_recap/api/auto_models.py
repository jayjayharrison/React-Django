# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ApiStockprofile(models.Model):
    closing_date = models.DateField(blank=True, null=True)
    company = models.CharField(unique=True, max_length=5, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    industry = models.CharField(max_length=126, blank=True, null=True)
    market_cap = models.FloatField(blank=True, null=True)
    pe = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    price = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    sector = models.CharField(max_length=126, blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    ticker = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'api_stockprofile'


class ApiWatchlist(models.Model):
    uid = models.CharField(unique=True, max_length=8)
    ticker = models.CharField(unique=True, max_length=5)
    created_at = models.DateTimeField()
    highlighted = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'api_watchlist'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Overview(models.Model):
    no_field = models.IntegerField(db_column='No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ticker = models.TextField(db_column='Ticker', blank=True, null=True)  # Field name made lowercase.
    company = models.TextField(db_column='Company', blank=True, null=True)  # Field name made lowercase.
    sector = models.TextField(db_column='Sector', blank=True, null=True)  # Field name made lowercase.
    industry = models.TextField(db_column='Industry', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    market_cap = models.TextField(db_column='Market_Cap', blank=True, null=True)  # Field name made lowercase.
    p_e = models.TextField(db_column='P/E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    change = models.TextField(db_column='Change', blank=True, null=True)  # Field name made lowercase.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'overview'


class Valuation(models.Model):
    no_field = models.IntegerField(db_column='No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    ticker = models.TextField(db_column='Ticker', blank=True, null=True)  # Field name made lowercase.
    market_cap = models.TextField(db_column='Market_Cap', blank=True, null=True)  # Field name made lowercase.
    p_e = models.TextField(db_column='P/E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fwd_p_e = models.TextField(db_column='Fwd_P/E', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    peg = models.TextField(db_column='PEG', blank=True, null=True)  # Field name made lowercase.
    p_s = models.TextField(db_column='P/S', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_b = models.TextField(db_column='P/B', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_c = models.TextField(db_column='P/C', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    p_fcf = models.TextField(db_column='P/FCF', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_this_y = models.TextField(db_column='EPS_this_Y', blank=True, null=True)  # Field name made lowercase.
    eps_next_y = models.TextField(db_column='EPS_next_Y', blank=True, null=True)  # Field name made lowercase.
    eps_past_5y = models.TextField(db_column='EPS_past_5Y', blank=True, null=True)  # Field name made lowercase.
    eps_next_5y = models.TextField(db_column='EPS_next_5Y', blank=True, null=True)  # Field name made lowercase.
    sales_past_5y = models.TextField(db_column='Sales_past_5Y', blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    change = models.TextField(db_column='Change', blank=True, null=True)  # Field name made lowercase.
    volume = models.TextField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'valuation'
