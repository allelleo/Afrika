from tortoise import fields, Model


class Article(Model):
    id = fields.IntField(pk=True)
    time_created = fields.DatetimeField(auto_now_add=True)
    content = fields.JSONField()
    author = fields.ForeignKeyField("")

    class Meta:
        table = "articles"
        ordering = ["-time_created"]


class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)

    class Meta:
        table = "users"
