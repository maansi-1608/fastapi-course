"""add_content_column

Revision ID: 8143cb39fe51
Revises: 6af446c58d5e
Create Date: 2022-01-10 01:54:38.696075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8143cb39fe51'
down_revision = '6af446c58d5e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts' , sa.Column('content' , sa.String , nullable=False))
    
    pass


def downgrade():
    op.drop_column('posts' , 'content')
    pass
