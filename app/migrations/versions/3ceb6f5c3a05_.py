"""empty message

Revision ID: 3ceb6f5c3a05
Revises: 
Create Date: 2019-02-16 21:33:15.100705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ceb6f5c3a05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relationships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_number1', sa.String(), nullable=False),
    sa.Column('phone_number2', sa.String(), nullable=False),
    sa.Column('twilio_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('relationships')
    # ### end Alembic commands ###
