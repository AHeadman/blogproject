"""empty message

Revision ID: e004c0356508
Revises: 65647fc69a28
Create Date: 2019-09-18 11:36:11.594399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e004c0356508'
down_revision = '65647fc69a28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'entry', 'user', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'entry', type_='foreignkey')
    op.drop_column('entry', 'author_id')
    # ### end Alembic commands ###
