"""posts table

Revision ID: 0ff4a2243e87
Revises: 8caf80673ee3
Create Date: 2024-06-02 00:24:36.902042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ff4a2243e87'
down_revision = '8caf80673ee3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_post_user_id'), ['user_id'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_user_id'))
        batch_op.drop_index(batch_op.f('ix_post_timestamp'))

    op.drop_table('post')
    # ### end Alembic commands ###
