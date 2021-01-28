"""Create Message

Revision ID: 506916225db1
Revises: 0f460d275643
Create Date: 2021-01-26 12:34:01.728993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '506916225db1'
down_revision = '0f460d275643'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.VARCHAR(length=4096), nullable=True),
    sa.Column('is_delete', sa.BOOLEAN(), nullable=False),
    sa.ForeignKeyConstraint(['recipient_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'users', ['id'])


def downgrade():
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_table('messages')
