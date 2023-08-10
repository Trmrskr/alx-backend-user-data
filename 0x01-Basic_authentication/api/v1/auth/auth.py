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
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) <= 0:
            return True

        if not path.endswith('/'):
            path += '/'

        for pth in excluded_paths:
            if '*' in pth:
                # handle paths which ends with * and in excluded path
                pth_split = pth.split('*')
                if path.startswith(pth_split[0]):
                    return False

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """
        take care of later
        """
        if request is None:
            return None
        authorization = request.headers.get('Authorization')
        if authorization is None:
            return None
        return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """
        take care of later
        """
        return None
