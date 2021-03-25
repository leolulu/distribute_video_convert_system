import uuid


class UuidUtil:
    @classmethod
    def get_uuid(cls):
        return uuid.uuid4().hex
