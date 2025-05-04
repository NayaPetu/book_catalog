from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'authors',
        sa.Column('author_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('bio', sa.Text, nullable=True)
    )
    op.create_table(
        'books',
        sa.Column('book_id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('author_id', sa.Integer, sa.ForeignKey('authors.author_id'), nullable=False),
        sa.Column('genre', sa.String, nullable=True),
        sa.Column('publication_year', sa.Integer, nullable=True),
        sa.Column('isbn', sa.String, nullable=True, unique=True)
    )
    op.create_table(
        'users',
        sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, nullable=False, unique=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password_hash', sa.String, nullable=False)
    )
    op.create_table(
        'ratings',
        sa.Column('rating_id', sa.Integer, primary_key=True),
        sa.Column('book_id', sa.Integer, sa.ForeignKey('books.book_id'), nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.user_id'), nullable=False),
        sa.Column('rating', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False)
    )

def downgrade():
    op.drop_table('ratings')
    op.drop_table('users')
    op.drop_table('books')
    op.drop_table('authors')