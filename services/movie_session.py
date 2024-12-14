from datetime import datetime

from django.db.models import QuerySet, Q

from db.models import MovieSession

def create_movie_session(
    movie_show_time: datetime,
    movie_id: int,
    cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(
        session_date: str=None,
) -> QuerySet:
    movie_date_filter = Q()
    if session_date:
        movie_date_filter &= Q(show_time__date=session_date)
    return MovieSession.objects.filter(movie_date_filter)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id,
        show_time: datetime=None,
        movie_id: int=None,
        cinema_hall_id: int=None,
) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time=show_time
    if movie_id:
        movie_session.movie_id=movie_id
    if cinema_hall_id:
        movie_session.cinema_hall_id=cinema_hall_id

    movie_session.save()


def delete_movie_session_by_id(
        session_id: int
) -> None:
    MovieSession.objects.get(id=session_id).delete()
