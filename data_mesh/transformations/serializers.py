from rest_framework.serializers import (BooleanField, CharField, DictField,
                                        IntegerField, ListField, Serializer)


class TransformationSerializer(Serializer):
    id = IntegerField()
    name = CharField(max_length=200)
    table = CharField(max_length=200)
    schema = CharField(max_length=200)
    db = CharField(max_length=200)
    sql = CharField(max_length=10000)
    schedule = CharField(max_length=20)
    owner = CharField(max_length=100)
    metadata = DictField()
    snapshot = CharField(max_length=100)
    id_column = ListField(
        child=CharField(max_length=200)
    )
    execution_timeout = IntegerField()
    priority = IntegerField()
    refresh_type = CharField(max_length=100)
    deduplicate = BooleanField()
    notification_channel = CharField(max_length=100)
