"""Init tables

Revision ID: 275515c51af1
Revises:
Create Date: 2021-03-24 15:03:16.549798

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy import inspect

# revision identifiers, used by Alembic.
revision = "275515c51af1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    inspector = inspect(bind)

    if "comments_threads" in inspector.get_table_names():
        print("comments_threads existiert bereits - Migration wird übersprungen.")
    else:
        op.create_table(
            "comments_threads",
            sa.Column("id", sa.Text, primary_key=True),
            sa.Column("subject_id", sa.Text, nullable=False),
            sa.Column("subject_type", sa.Text, nullable=False),
            sa.Column(
                "created_at",
                sa.DateTime,
                nullable=False,
                server_default=sa.func.current_timestamp(),
            ),
            sa.Index("subject_idx", "subject_id", "subject_type", unique=True),
        )
    if "comments_comments" in inspector.get_table_names():
        print("comments_comments existiert bereits - Migration wird übersprungen.")
    else:
        op.create_table(
            "comments_comments",
            sa.Column("id", sa.Text, primary_key=True),
            sa.Column(
                "thread_id",
                sa.Text,
                sa.ForeignKey("comments_threads.id"),
                nullable=False,
            ),
            sa.Column("content", sa.Text, nullable=False),
            sa.Column("author_id", sa.Text, nullable=False),
            sa.Column("author_type", sa.Text, nullable=False),
            sa.Column("state", sa.Text, nullable=False),
            sa.Column(
                "reply_to_id",
                sa.Text,
                sa.ForeignKey("comments_comments.id"),
                nullable=True,
                index=True,
            ),
            sa.Column(
                "created_at",
                sa.DateTime,
                nullable=False,
                server_default=sa.func.current_timestamp(),
            ),
            sa.Column("modified_at", sa.DateTime, nullable=True),
            sa.Index("author_idx", "author_id", "author_type"),
        )


def downgrade():
    op.drop_table("comments_comments")
    op.drop_table("comments_threads")
