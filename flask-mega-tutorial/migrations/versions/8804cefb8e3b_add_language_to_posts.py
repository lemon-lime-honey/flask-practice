"""add language to posts

Revision ID: 8804cefb8e3b
Revises: 81866d68960a
Create Date: 2024-06-07 20:41:00.240291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8804cefb8e3b'
down_revision = '81866d68960a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###