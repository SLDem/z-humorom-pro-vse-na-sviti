"""empty message

Revision ID: b25f2ff27a6f
Revises: 
Create Date: 2020-04-10 09:51:56.691797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b25f2ff27a6f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('humoresques',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=True),
    sa.Column('text', sa.String(length=1028), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('text'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('humoresques')
    # ### end Alembic commands ###