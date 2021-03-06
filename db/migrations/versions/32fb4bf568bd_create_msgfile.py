"""Create MsgFile

Revision ID: 32fb4bf568bd
Revises: ab328d26f09e
Create Date: 2021-02-04 22:49:41.201019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32fb4bf568bd'
down_revision = 'ab328d26f09e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('msgs_to_files',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('msg_id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('is_delete', sa.BOOLEAN(), nullable=False),
    sa.ForeignKeyConstraint(['file_id'], ['files.id'], ),
    sa.ForeignKeyConstraint(['msg_id'], ['messages.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'files', ['id'])


def downgrade():
    op.drop_constraint(None, 'files', type_='unique')
    op.drop_table('msgs_to_files')
