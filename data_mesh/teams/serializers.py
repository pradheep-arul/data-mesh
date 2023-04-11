from rest_framework.serializers import CharField, ListField, Serializer, IntegerField


class TeamSerializer(Serializer):
    id = IntegerField()
    name = CharField(max_length=200)
    description = CharField(max_length=500)
    manager = CharField(max_length=200)
    members = ListField(
        child=CharField(max_length=200)
    )
    slack_channel = CharField(max_length=200)
    mail_id = CharField(max_length=200)
