# from alembic import op
# import sqlalchemy as sa

# def upgrade():
#     op.create_table(
#         'authors',
#         sa.Column('author_id', sa.Integer, primary_key=True),
#         sa.Column('name', sa.String, nullable=False),
#         sa.Column('bio', sa.Text, nullable=True)
#     )
#     op.create_table(
#         'books',
#         sa.Column('book_id', sa.Integer, primary_key=True),
#         sa.Column('title', sa.String, nullable=False),
#         sa.Column('author_id', sa.Integer, sa.ForeignKey('authors.author_id'), nullable=False),
#         sa.Column('genre', sa.String, nullable=True),
#         sa.Column('publication_year', sa.Integer, nullable=True),
#         sa.Column('isbn', sa.String, nullable=True, unique=True)
#     )
#     op.create_table(
#         'users',
#         sa.Column('user_id', sa.Integer, primary_key=True),
#         sa.Column('username', sa.String, nullable=False, unique=True),
#         sa.Column('email', sa.String, nullable=False, unique=True),
#         sa.Column('password_hash', sa.String, nullable=False)
#     )
#     op.create_table(
#         'ratings',
#         sa.Column('rating_id', sa.Integer, primary_key=True),
#         sa.Column('book_id', sa.Integer, sa.ForeignKey('books.book_id'), nullable=False),
#         sa.Column('user_id', sa.Integer, sa.ForeignKey('users.user_id'), nullable=False),
#         sa.Column('rating', sa.Integer, nullable=False),
#         sa.Column('created_at', sa.DateTime, nullable=False)
#     )

# def downgrade():
#     op.drop_table('ratings')
#     op.drop_table('users')
#     op.drop_table('books')
#     op.drop_table('authors')



"""Initial migration

Revision ID: initial_migration
Revises: 
Create Date: 2025-05-04 12:00:00

"""
from alembic import op
import sqlalchemy as sa

revision = 'initial_migration'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('hashed_password', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    
    op.create_table('authors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('bio', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_authors_id'), 'authors', ['id'], unique=False)
    op.create_index(op.f('ix_authors_name'), 'authors', ['name'], unique=False)
    
    op.create_table('books',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('author_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_books_id'), 'books', ['id'], unique=False)
    op.create_index(op.f('ix_books_title'), 'books', ['title'], unique=False)
    
    op.create_table('ratings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('score', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('book_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ratings_id'), 'ratings', ['id'], unique=False)

def downgrade():
    op.drop_index(op.f('ix_ratings_id'), table_name='ratings')
    op.drop_table('ratings')
    op.drop_index(op.f('ix_books_id'), table_name='books')
    op.drop_index(op.f('ix_books_title'), table_name='books')
    op.drop_table('books')
    op.drop_index(op.f('ix_authors_id'), table_name='authors')
    op.drop_index(op.f('ix_authors_name'), table_name='authors')
    op.drop_table('authors')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')