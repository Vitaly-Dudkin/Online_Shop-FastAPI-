from sqlalchemy import Table, Column, Integer, String, MetaData


metadata = MetaData()

category = Table(
    "category",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String, nullable=True),
)
