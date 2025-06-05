import time
import uuid
from typing import List, Dict, Any
from .config import settings
from .schemas import PostOut

# In-memory post store
_POST_STORE: Dict[str, Dict[str, Any]] = {}

# In-memory per-user cache
_POSTS_CACHE: Dict[str, Dict[str, Any]] = {}

def validate_payload_size(text: str):
    return len(text.encode("utf-8")) <= settings.MAX_POST_SIZE_BYTES

def add_post_to_store(owner_email: str, text: str) -> str:
    post_id = str(uuid.uuid4())
    _POST_STORE[post_id] = {
        "text": text,
        "owner_email": owner_email,
        "timestamp": time.time()
    }
    _POSTS_CACHE.pop(owner_email, None)
    return post_id

def get_posts_for_user(owner_email: str) -> List[PostOut]:
    now = time.time()
    cache_entry = _POSTS_CACHE.get(owner_email)
    if cache_entry and now - cache_entry["cached_at"] < settings.POSTS_CACHE_TTL_SECONDS:
        return cache_entry["posts"]

    fresh_posts: List[PostOut] = []
    for pid, rec in _POST_STORE.items():
        if rec["owner_email"] == owner_email:
            fresh_posts.append(PostOut(post_id=pid, owner_email=owner_email, text=rec["text"]))
    _POSTS_CACHE[owner_email] = {"posts": fresh_posts, "cached_at": now}
    return fresh_posts

def delete_post(owner_email: str, post_id: str) -> bool:
    rec = _POST_STORE.get(post_id)
    if not rec or rec["owner_email"] != owner_email:
        return False
    del _POST_STORE[post_id]
    _POSTS_CACHE.pop(owner_email, None)
    return True

