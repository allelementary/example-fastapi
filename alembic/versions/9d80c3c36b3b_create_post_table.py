"""create post table

Revision ID: 9d80c3c36b3b
Revises: 
Create Date: 2022-03-24 19:40:00.814338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d80c3c36b3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)
                    )


def downgrade():
    op.drop_table('posts')
