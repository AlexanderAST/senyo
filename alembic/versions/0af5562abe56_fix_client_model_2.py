"""fix client model 2

Revision ID: 0af5562abe56
Revises: 15358242b2a4
Create Date: 2025-04-06 02:01:17.460817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0af5562abe56'
down_revision: Union[str, None] = '15358242b2a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gender',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_gender_id'), 'gender', ['id'], unique=False)
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('id_gender', sa.Integer(), nullable=True),
    sa.Column('telegram_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_gender'], ['gender.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_client_id'), 'client', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_client_id'), table_name='client')
    op.drop_table('client')
    op.drop_index(op.f('ix_gender_id'), table_name='gender')
    op.drop_table('gender')
    # ### end Alembic commands ###
