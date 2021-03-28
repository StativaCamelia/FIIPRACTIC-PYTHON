import bcrypt
import hashlib

from binascii import a2b_qp


class CompanyAdapter:

    @staticmethod
    def to_json(results):
        return [
            {
                "id": user.id,
                "name": user.name,
                "street": user.street,
	            "city" : user.city,
	            "country": user.country
            } for user in results
        ]

    def to_object(self, body):
        for key, value in body.items():
            if hasattr(self, key):
                setattr(self, key, value)