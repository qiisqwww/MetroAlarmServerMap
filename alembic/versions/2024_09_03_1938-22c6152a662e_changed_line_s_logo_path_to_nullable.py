"""changed line's logo path to nullable

Revision ID: 22c6152a662e
Revises: 340150a5b8e7
Create Date: 2024-09-03 19:38:19.589065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22c6152a662e'
down_revision: Union[str, None] = '340150a5b8e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('lines', 'logo_path',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('lines', 'logo_path',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
