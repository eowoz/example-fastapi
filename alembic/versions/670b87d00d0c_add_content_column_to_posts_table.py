"""add content column to posts table

Revision ID: 670b87d00d0c
Revises: 2bbe9cb6f84a
Create Date: 2021-11-09 23:42:50.443560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '670b87d00d0c'
down_revision = '2bbe9cb6f84a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
