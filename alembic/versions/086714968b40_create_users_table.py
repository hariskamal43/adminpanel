"""create users table

Revision ID: 086714968b40
Revises: 
Create Date: 2022-03-12 16:17:47.904585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '086714968b40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False, unique=True),
                    sa.Column('email', sa.String(), nullable=False, unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')                
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
