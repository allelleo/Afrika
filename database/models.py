from tortoise import fields, Model


class Category(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=100)

    class Meta:
        table = "categories"
        ordering = ["-id"]


class Article(Model):
    id = fields.IntField(pk=True)
    time_created = fields.DatetimeField(auto_now_add=True)
    title = fields.CharField(max_length=100)
    content = fields.JSONField()
    author = fields.ForeignKeyField("models.User")
    category = fields.ManyToManyField("models.Category")
    views = fields.IntField(default=0)

    class Meta:
        table = "articles"
        ordering = ["-time_created"]


class Peoples(Model):
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    bio = fields.TextField()

    class Meta:
        table = "peoples"


class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)

    class Meta:
        table = "users"
