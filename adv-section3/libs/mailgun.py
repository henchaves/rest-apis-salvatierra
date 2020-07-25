from typing import List
from requests import Response, post
from credentials import MAILGUN_DOMAIN, MAILGUN_API_KEY

class Mailgun:
    FROM_EMAIL = "mailgun@" + MAILGUN_DOMAIN
    FROM_TITLE = "Stores REST API"

    @classmethod
    def send_email(cls, email: List[str], subject: str, text: str, html: str) -> Response:
            return post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", MAILGUN_API_KEY),
                data={
                    "from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
                    "to": email,
                    "subject": subject,
                    "text": text,
                    "html": html
                }
            )