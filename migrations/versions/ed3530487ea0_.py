"""empty message

Revision ID: ed3530487ea0
Revises: 8b9a0d27968e
Create Date: 2024-09-18 16:00:42.363969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed3530487ea0'
down_revision = '8b9a0d27968e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('weater',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=42),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('weater',
               existing_type=sa.String(length=42),
               type_=sa.VARCHAR(length=15),
               existing_nullable=False)

    # ### end Alembic commands ###