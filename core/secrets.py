"""Helpers for keeping credentials out of logs."""
from __future__ import annotations


def mask_secret(value: str | None, *, keep: int = 2) -> str:
    """Return a masked form of a secret that is safe to print in logs.

    Empty or short values collapse to a fixed placeholder so the real length is
    not leaked; longer values keep a few leading/trailing characters to aid
    debugging while hiding the middle.
    """
    if not value:
        return ""
    text = str(value)
    if len(text) <= keep * 2:
        return "***"
    return f"{text[:keep]}***{text[-keep:]}"
