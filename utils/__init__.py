import hashlib
import urllib.parse


def generate_sha256_hash(text: str) -> str:
    """Returns 64 string hash"""
    return hashlib.sha256(text.encode()).hexdigest()


def create_mailto(
    to: list[str],
    cc: list[str] = [],
    subject: str = "",
    body: list[str] = []) -> str:
    
    body_text = urllib.parse.quote('\n'.join(body))
    
    result = f"mailto:{';'.join(to)}?body={body_text}"
    if cc:
        result += "&cc=" + ';'.join(cc)
    if subject:    
        result += f"&subject={subject}"
    
    return result