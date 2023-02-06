"""empty message

Revision ID: 53579ecbfcdc
Revises: 4a395410a323
Create Date: 2023-02-06 17:28:49.001594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53579ecbfcdc'
down_revision = '4a395410a323'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=32),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.String(length=32),
               type_=sa.VARCHAR(length=16),
               existing_nullable=True)

    # ### end Alembic commands ###
