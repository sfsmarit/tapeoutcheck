import urllib.parse


def get_mailto_link(
    to: list[str],
    cc: list[str] = [],
    subject: str = "",
    body: list[str] = [],
) -> str:
    body_text = urllib.parse.quote('\n'.join(body))
    result = f"mailto:{';'.join(to)}?body={body_text}"
    if cc:
        result += "&cc=" + ';'.join(cc)
    if subject:    
        result += f"&subject={subject}"
    return result



def get_PO_request_mailto_link() -> str:
    return get_mailto_link(
        to=[
            "hogehoge@gmail.com",
        ],
        cc=[],
        subject="PO request",
        body=["Hi,",
              "",
              "Thanks,",
              "<Your name>"]
    )
