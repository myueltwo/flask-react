"""add table subject

Revision ID: 1a1ed2a7f63c
Revises: 94d17cc8ee11
Create Date: 2022-12-14 23:15:27.381213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a1ed2a7f63c'
down_revision = '94d17cc8ee11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subject',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('count_hours', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_subject'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subject')
    # ### end Alembic commands ###