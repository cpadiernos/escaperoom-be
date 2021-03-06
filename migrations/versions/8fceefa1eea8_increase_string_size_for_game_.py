"""increase string size for game description and hints

Revision ID: 8fceefa1eea8
Revises: 1166c0270198
Create Date: 2020-10-26 15:52:41.712894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fceefa1eea8'
down_revision = '1166c0270198'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=350),
               existing_nullable=True)

    with op.batch_alter_table('hint', schema=None) as batch_op:
        batch_op.alter_column('text',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=250),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hint', schema=None) as batch_op:
        batch_op.alter_column('text',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)

    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.alter_column('description',
               existing_type=sa.String(length=350),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###
