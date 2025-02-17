"""phone number added

Revision ID: 54a0feae7839
Revises: 
Create Date: 2025-02-15 00:12:57.844509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54a0feae7839'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("phone_number", sa.String(), nullable=True ))



def downgrade() -> None:
    #op.drop_column("users", "phone_number")
    pass
