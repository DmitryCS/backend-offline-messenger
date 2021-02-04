"""Create User

Revision ID: 5403cd3b8fc0
Revises: 
Create Date: 2021-02-04 22:48:46.858316

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5403cd3b8fc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('login', sa.VARCHAR(length=50), nullable=False),
    sa.Column('password', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('login')
    )


def downgrade():
    op.drop_table('users')
