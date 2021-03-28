from sqlalchemy import PrimaryKeyConstraint, ForeignKey, Column, Integer

from src.models.base import Base


class UserCompany(Base):
	__tablename__  = "user_company"
	__tables_args__ = (PrimaryKeyConstraint("user_id", "company_id"))
	user_id = Column(Integer, ForeignKey("user.id", ondelete = "CASCADE"), nullable = False)
	user_id = Column(Integer, ForeignKey("company.id", ondelete="CASCADE"), nullable = False)
