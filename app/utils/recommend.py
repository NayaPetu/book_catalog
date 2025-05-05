"""Recommendation utilities."""

from typing import List

from sqlalchemy.sql import func
from sqlmodel import Session, select

from app.models.books import Book
from app.models.ratings import Rating
from app.models.users import User


def get_recommendations(db: Session, username: str) -> List[Book]:
    """Generate book recommendations for a user."""
    user = db.exec(select(User).where(User.username == username)).first()
    if not user:
        return []

    # Get books rated by the user
    rated_books = db.exec(
        select(Rating.book_id).where(Rating.user_id == user.id)
    ).all()
    rated_book_ids = [book_id for book_id, in rated_books]

    # Collaborative filtering: find similar users
    similar_users = db.exec(
        select(Rating.user_id)
        .where(Rating.book_id.in_(rated_book_ids))
        .where(Rating.user_id != user.id)
        .group_by(Rating.user_id)
        .having(func.count(Rating.id) > 1)
    ).all()
    similar_user_ids = [user_id for user_id, in similar_users]

    # Get books rated highly by similar users
    recommended_books = db.exec(
        select(Book)
        .join(Rating)
        .where(Rating.user_id.in_(similar_user_ids))
        .where(Rating.score >= 4)
        .where(Book.id.notin_(rated_book_ids))
        .group_by(Book.id)
        .order_by(func.avg(Rating.score).desc())
        .limit(5)
    ).all()

    # Fallback to random books if no recommendations
    if not recommended_books:
        recommended_books = db.exec(
            select(Book).where(Book.id.notin_(rated_book_ids)).limit(5)
        ).all()

    return recommended_books


# """Recommendation utilities."""

# from typing import List

# from sqlalchemy.sql import func
# from sqlmodel import Session, select

# from app.models.books import Book
# from app.models.ratings import Rating
# from app.models.users import User


# def get_recommendations(db: Session, username: str) -> List[Book]:
#     """Generate book recommendations for a user."""
#     user = db.exec(select(User).where(User.username == username)).first()
#     if not user:
#         return []

#     # Get books rated by the user
#     rated_books = db.exec(select(Rating.book_id).where(Rating.user_id == user.id)).all()
#     rated_book_ids = [book_id for book_id, in rated_books]

#     # Collaborative filtering: find similar users
#     similar_users = (
#         db.exec(
#             select(Rating.user_id)
#             .where(Rating.book_id.in_(rated_book_ids))
#             .where(Rating.user_id != user.id)
#             .group_by(Rating.user_id)
#             .having(func.count() > 1)
#         )
#         .all()
#     )
#     similar_user_ids = [user_id for user_id, in similar_users]

#     # Get books rated highly by similar users
#     recommended_books = (
#         db.exec(
#             select(Book)
#             .join(Rating)
#             .where(Rating.user_id.in_(similar_user_ids))
#             .where(Rating.score >= 4)
#             .where(~Book.id.in_(rated_book_ids))
#             .group_by(Book.id)
#             .order_by(func.avg(Rating.score).desc())
#             .limit(5)
#         )
#         .all()
#     )

#     return recommended_books or db.exec(select(Book).where(~Book.id.in_(rated_book_ids)).limit(5)).all()



# # # Алгоритм рекомендаций

# # from sqlmodel import Session, select
# # from app.models.ratings import Rating
# # from app.models.books import Book
# # from app.models.users import User
# # from sqlalchemy.sql import func

# # def get_recommendations(db: Session, username: str):
# #     user = db.exec(select(User).where(User.username == username)).first()
# #     if not user:
# #         return []

# #     # Get books rated by the user
# #     rated_books = db.exec(
# #         select(Rating.book_id).where(Rating.user_id == user.id)
# #     ).all()
# #     rated_book_ids = [book_id for (book_id,) in rated_books]

# #     # Find users with similar ratings (simple collaborative filtering)
# #     similar_users = db.exec(
# #         select(Rating.user_id)
# #         .where(Rating.book_id.in_(rated_book_ids))
# #         .where(Rating.user_id != user.id)
# #         .group_by(Rating.user_id)
# #         .having(func.count() > 1)  # At least 2 common books
# #     ).all()
# #     similar_user_ids = [user_id for (user_id,) in similar_users]

# #     # Get books rated highly by similar users
# #     recommended_books = db.exec(
# #         select(Book)
# #         .join(Rating)
# #         .where(Rating.user_id.in_(similar_user_ids))
# #         .where(Rating.score >= 4)
# #         .where(~Book.id.in_(rated_book_ids))
# #         .group_by(Book.id)
# #         .order_by(func.avg(Rating.score).desc())
# #         .limit(5)
# #     ).all()

# #     return recommended_books if recommended_books else db.exec(
# #         select(Book).where(~Book.id.in_(rated_book_ids)).limit(5)
# #     ).all()


