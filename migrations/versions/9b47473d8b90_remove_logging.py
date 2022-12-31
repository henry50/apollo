"""Remove logging

Revision ID: 9b47473d8b90
Revises: 988a71e876c3
Create Date: 2022-12-31 15:45:53.589887

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '9b47473d8b90'
down_revision = '988a71e876c3'
branch_labels = None
depends_on = None

# https://alembic.sqlalchemy.org/en/latest/batch.html#dropping-unnamed-or-named-foreign-key-constraints
naming_convention = {
    "fk":
    "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message_edits')
    op.drop_table('messages')

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'karma_changes', 'messages', ['message_id'], ['id'])
    op.create_table('message_edits',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('original_message', sa.INTEGER(), nullable=False),
    sa.Column('new_content', sa.BLOB(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['original_message'], ['messages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('message_uid', sa.BIGINT(), nullable=False),
    sa.Column('message_content', sa.BLOB(), nullable=False),
    sa.Column('author', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=False),
    sa.Column('channel_name', sa.BLOB(), nullable=False),
    sa.Column('deleted_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###