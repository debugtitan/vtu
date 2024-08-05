"""buddy points

Revision ID: a5ba51820e1a
Revises: 
Create Date: 2024-08-05 20:02:25.996632

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a5ba51820e1a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("buddy_points", sa.Integer(), default=0))


def downgrade() -> None:
    op.drop_column("users", "buddy_points")
