"""Create File

Revision ID: ab328d26f09e
Revises: 3adfb091024e
Create Date: 2021-02-04 22:49:30.091025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab328d26f09e'
down_revision = '3adfb091024e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('files',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('ref_file', sa.VARCHAR(length=4096), nullable=True),
    sa.Column('is_delete', sa.BOOLEAN(), nullable=False),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'messages', ['id'])


def downgrade():
    op.drop_constraint(None, 'messages', type_='unique')
    op.drop_table('files')
