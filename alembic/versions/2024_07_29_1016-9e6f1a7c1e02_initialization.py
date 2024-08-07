"""initialization

Revision ID: 9e6f1a7c1e02
Revises: 
Create Date: 2024-07-29 10:16:58.112988

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e6f1a7c1e02'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('lines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('stations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('longitude', sa.String(), nullable=False),
    sa.Column('latitude', sa.String(), nullable=False),
    sa.Column('line_id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('first_neighbour_id', sa.Integer(), nullable=False),
    sa.Column('second_neighbour_id', sa.Integer(), nullable=False),
    sa.Column('radius', sa.Integer(), nullable=False),
    sa.Column('radius_rate', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.ForeignKeyConstraint(['first_neighbour_id'], ['stations.id'], ),
    sa.ForeignKeyConstraint(['line_id'], ['lines.id'], ),
    sa.ForeignKeyConstraint(['second_neighbour_id'], ['stations.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('user_favourite_stations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('station_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['station_id'], ['stations.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_favourite_stations')
    op.drop_table('stations')
    op.drop_table('lines')
    op.drop_table('cities')
    # ### end Alembic commands ###
