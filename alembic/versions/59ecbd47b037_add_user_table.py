"""add user table

Revision ID: 59ecbd47b037
Revises: 670b87d00d0c
Create Date: 2021-11-09 23:47:18.381367

"""
from typing import Text
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59ecbd47b037'
down_revision = '670b87d00d0c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
