from sqlalchemy import Column, String, Integer

from src.adapters.companies import CompanyAdapter
from src.models.base import Base
from src.utils.exceptions import Conflict
from src.utils.validators import validate_company_body


class Company(Base, CompanyAdapter):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    street = Column(String(200))
    city = Column(String(100))
    country = Column(String(100))

    @classmethod
    def get_companies(cls, context):
        result = context.query(cls).all()
        return cls.to_json(result)

    @classmethod
    def create_company(cls, context, body):
        if body.get("email"):
            validate_company_body(body)
        if cls.get_company_by_name(context, body.get("name")):
            raise Conflict("This email address is already used", status=409)
        company = Company()
        company.to_object(body)
        context.add(company)
        context.commit()

    @classmethod
    def get_company_by_name(cls,context, name):
        return context.query(cls).filter_by(name=name).first()

    @classmethod
    def get_company_by_id(cls, context, id):
        return context.query(cls).filter_by(id=id).first()

    @classmethod
    def update_company(cls, context, body, company_id):
        if body.get("email"):
            validate_company_body(body)
        company = cls.get_company_by_id(context, company_id)
        if not company:
            return Conflict("The company you are trying to update does not exist", 404)
        company.to_object(body)
        context.commit()

    @classmethod
    def update_company_partialy(cls, context, body, company_id):
        if body.get("email"):
            validate_company_body(body)
        company = cls.get_company_by_id(context, company_id)
        if not company:
            return Conflict("The company you are trying to update does not exist", 404)
        company.data = body
        context.commit()

    @classmethod
    def delete_company(cls, context, company_id):
        company = cls.get_company_by_id(context, company_id)
        if not company:
            return Conflict("The company you are trying to update does not exist", 404)
        context.delete(company)
        context.commit()