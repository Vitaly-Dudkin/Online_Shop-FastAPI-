from sqlalchemy import Table, Column, Integer, String, MetaData, Boolean, DateTime, ForeignKey

from src.category.models import category
metadata = MetaData()

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("category", Integer, ForeignKey(category.c.id)),
    Column("price", String),
    Column("name", String),
    Column("description", String, nullable=True),
    Column("created_at", DateTime),
    Column("updated_at", DateTime),
    Column("is_active", Boolean, default=True),
)
