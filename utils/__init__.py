import urllib.parse


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