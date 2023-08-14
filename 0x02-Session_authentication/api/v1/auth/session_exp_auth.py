#!/usr/bin/env python3
"""
Expiration module
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from models.user import User
from os import getenv


class SessionExpAuth(SessionAuth):
    """
    Session Expriation Authentication
    """
    def __init__(self):
        """
        Constructor function
        """
        try:
            duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            duration = 0
        self.session_duration = duration

    def create_session(self, user_id=None):
        """
        Create a session
        """
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Return user_id for session_id
        """
        if session_id is None:
            return None
        if session_id not in user_id_by_session_id:
            return None
        if self.session_duration <= 0:
            return self.user_id

        created_at = session_dictionary.get('created_at')

        if created_at is None:
            return None

        expired_time = created_at + timedelta(seconds=self.session_duration)
        if expired_time < datetime.now():
            return None

        return session_dictionary.get('user_id')
