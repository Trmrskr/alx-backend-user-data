#!/usr/bin/env python3
"""
Basic authentication
"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """
    Basic Auth class
    """
    def extract_base64_authorization_header(
                                            self,
                                            authorization_header: str
                                            ) -> str:
        """
        extract base64 string
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        base64str = authorization_header.split(' ')[1].strip()
        return base64str

    def decode_base64_authorization_header(
                                            self,
                                            base64_authorization_header: str
                                            ) -> str:
        """Base 64 decoding"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = base64.b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded
