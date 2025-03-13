"""initial migration

Revision ID: initial
Revises: 
Create Date: 2024-03-13 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Створення таблиці груп
    op.create_table('groups',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    # Створення таблиці викладачів
    op.create_table('teachers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    # Створення таблиці студентів
    op.create_table('students',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('group_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    # Створення таблиці предметів
    op.create_table('subjects',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('teacher_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    # Створення таблиці оцінок
    op.create_table('grades',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('student_id', sa.Integer(), nullable=True),
                    sa.Column('subject_id', sa.Integer(), nullable=True),
                    sa.Column('grade', sa.Float(), nullable=False),
                    sa.Column('date', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
                    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('grades')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('teachers')
    op.drop_table('groups')
