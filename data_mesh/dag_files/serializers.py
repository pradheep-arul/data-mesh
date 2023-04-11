from rest_framework.serializers import (CharField, DateTimeField, IntegerField,
                                        Serializer)


class FileSerializer(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=255)
    created_at = DateTimeField(read_only=True)
