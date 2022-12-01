"""Initial migration.

Revision ID: 30bf6e37fc59
Revises: 
Create Date: 2022-12-01 14:27:13.952455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30bf6e37fc59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.Text(), nullable=True),
    sa.Column('last_name', sa.Text(), nullable=True),
    sa.Column('contact_number', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('password', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('contact_number'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('product',
    sa.Column('prod_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.Column('seller_email', sa.Text(), nullable=True),
    sa.Column('initial_price', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('increment', sa.Float(), nullable=True),
    sa.Column('deadline_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('email_sent', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['seller_email'], ['users.email'], ),
    sa.PrimaryKeyConstraint('prod_id'),
    sa.UniqueConstraint('prod_id'),
    sa.UniqueConstraint('prod_id')
    )
    op.create_table('bids',
    sa.Column('prod_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('bid_amount', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['users.email'], ),
    sa.ForeignKeyConstraint(['prod_id'], ['product.prod_id'], ),
    sa.PrimaryKeyConstraint('prod_id', 'email')
    )
    op.create_table('claims',
    sa.Column('prod_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('expiry_date', sa.DateTime(), nullable=True),
    sa.Column('claim_status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['users.email'], ),
    sa.ForeignKeyConstraint(['prod_id'], ['product.prod_id'], ),
    sa.PrimaryKeyConstraint('prod_id', 'email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('claims')
    op.drop_table('bids')
    op.drop_table('product')
    op.drop_table('users')
    # ### end Alembic commands ###
