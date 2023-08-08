#!/usr/bin/env python3
"""
Holds the auth class which manages authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    The Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        take care of later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        take care of later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        take care of later
        """
        return None
