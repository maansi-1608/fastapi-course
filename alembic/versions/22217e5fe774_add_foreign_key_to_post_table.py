"""add_foreign_key_to_post_table

Revision ID: 22217e5fe774
Revises: d1125e7508a3
Create Date: 2022-01-10 02:04:35.001970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22217e5fe774'
down_revision = 'd1125e7508a3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts' , sa.Column('owner_id' , sa.Integer() , nullable=False))
    op.create_foreign_key('post_users_fk' , source_table='posts' , referent_table='users' , local_cols=['owner_id'], remote_cols=['id'] , ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk' , table_name='posts')
    op.drop_column('posts' , 'owner_id')
    pass
