"""empty message

Revision ID: 3ba0ceb98580
Revises: ea135fd8f043
Create Date: 2024-03-15 23:48:48.561472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ba0ceb98580'
down_revision = 'ea135fd8f043'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=240), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.Column('todo_list_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['todo_list_id'], ['todo_list.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('todo_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo_list', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    op.drop_table('task')
    # ### end Alembic commands ###
