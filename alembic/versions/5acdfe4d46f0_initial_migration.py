"""initial migration

Revision ID: 5acdfe4d46f0
Revises: 5d3b4b3b8a17
Create Date: 2024-01-11 16:07:20.896029

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5acdfe4d46f0'
down_revision: Union[str, None] = '5d3b4b3b8a17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
