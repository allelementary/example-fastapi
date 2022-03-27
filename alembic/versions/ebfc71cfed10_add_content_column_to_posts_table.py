"""add content column to posts table

Revision ID: ebfc71cfed10
Revises: 9d80c3c36b3b
Create Date: 2022-03-24 20:04:59.323568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebfc71cfed10'
down_revision = '9d80c3c36b3b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
