"""empty message

Revision ID: dc1cc911b2f1
Revises: 
Create Date: 2020-11-02 10:34:27.904739

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dc1cc911b2f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('date_created', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('date_updated', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('maintainer',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('date_created', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('date_updated', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('date_created', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('date_updated', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('date_created', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('date_updated', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('item_tag',
    sa.Column('item_id', postgresql.UUID(), nullable=False),
    sa.Column('tag_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('item_id', 'tag_id')
    )
    op.create_table('stock_item',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('date_created', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('date_updated', postgresql.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('stock_id', postgresql.UUID(), nullable=False),
    sa.Column('item_id', postgresql.UUID(), nullable=False),
    sa.Column('unit_of_measure', sa.String(), nullable=False),
    sa.Column('quantity', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.ForeignKeyConstraint(['stock_id'], ['stock.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stock_maintainer',
    sa.Column('stock_id', postgresql.UUID(), nullable=False),
    sa.Column('maintainer_id', postgresql.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['maintainer_id'], ['maintainer.id'], ),
    sa.ForeignKeyConstraint(['stock_id'], ['stock.id'], ),
    sa.PrimaryKeyConstraint('stock_id', 'maintainer_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock_maintainer')
    op.drop_table('stock_item')
    op.drop_table('item_tag')
    op.drop_table('tag')
    op.drop_table('stock')
    op.drop_table('maintainer')
    op.drop_table('item')
    # ### end Alembic commands ###
