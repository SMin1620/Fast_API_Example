from sqlmodel import Session

from app.poll.models import Poll, PollContent, PollCreate


class PollService:
    def create(self, session: Session, object_data: PollCreate) -> Poll:

        poll_data = object_data.dict(exclude_unset=True)
        poll_data["contents"] = [PollContent(content=content) for content in object_data.contents]

        poll = Poll(**poll_data)

        session.add(poll)

        return poll


service = PollService()
