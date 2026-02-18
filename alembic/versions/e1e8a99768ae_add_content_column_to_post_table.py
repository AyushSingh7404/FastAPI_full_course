"""Add content column to post table

Revision ID: e1e8a99768ae
Revises: b9f35b77555e
Create Date: 2026-02-18 16:06:11.773000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1e8a99768ae'
down_revision: Union[str, Sequence[str], None] = 'b9f35b77555e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
