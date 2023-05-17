"""empty message

Revision ID: d4b39b819189
Revises: c630a6a10f49
Create Date: 2023-05-11 22:55:17.823847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b39b819189'
down_revision = 'c630a6a10f49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Products', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Products_producer'), ['producer'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Products', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Products_producer'))

    # ### end Alembic commands ###