"""empty message

Revision ID: d032da119336
Revises: 74a3a4d07e37
Create Date: 2020-07-25 01:07:59.665423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd032da119336'
down_revision = '74a3a4d07e37'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('projects_student_id_key', 'projects', type_='unique')
    op.create_unique_constraint(None, 'students', ['auth_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'students', type_='unique')
    op.create_unique_constraint('projects_student_id_key', 'projects', ['student_id'])
    # ### end Alembic commands ###