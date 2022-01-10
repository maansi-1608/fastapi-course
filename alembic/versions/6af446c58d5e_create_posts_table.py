"""create_posts_table

Revision ID: 6af446c58d5e
Revises: 
Create Date: 2022-01-10 00:06:36.669048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6af446c58d5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id' , sa.Integer() , nullable=False , primary_key=True ) , sa.Column('title' , sa.String , nullable=False)
    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
