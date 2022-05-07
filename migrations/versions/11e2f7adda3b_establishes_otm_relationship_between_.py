"""establishes OtM relationship between Goal and Task classes

Revision ID: 11e2f7adda3b
Revises: 1ea0982c41e3
Create Date: 2022-05-07 11:21:15.969253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11e2f7adda3b'
down_revision = '1ea0982c41e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###