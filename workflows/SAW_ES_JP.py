from .models import Task, Flow
from services.email import get_PO_request_mailto_link


before_DR = Flow(
    gate=Task("Design Review 実施"),
    workflows=[
        Task(":material/group: Design Review 会議設定"),
        Task("SAP 登録シートを記入して担当者に連絡"),
        Task("Design Review Check"),
    ],
    skyfoundry=[
        Task("プロセスバリアントとファイルの詳細", link="https://www.nissan.co.jp/"),
        Task("Die Map/Mask Lauout リクエスト"),
        Task("1S/PCM リクエスト"),
        Task("Process Recipe リクエスト"),
        Task("マスク/レイヤ"),
    ],
    agile=[],
)

before_CAD_submission = Flow(
    gate=Task("CAD 提出"),
    workflows=[
        Task("PO 発行依頼", link=get_PO_request_mailto_link(), icon=":material/email:"),
        Task("マニュアルチェック依頼"),
        Task("マニュアルチェック実施"),
        Task("Mask Assembly Utility 実施"),
        Task("RDS サーバに HFSS/SNSS ファイルを格納"),
    ],
    skyfoundry=[
        Task("PO 入力"),
        Task("Manual Layout Check 登録"),
        Task("Waiver"),
    ],
    agile=[
        Task("MDR 作成"),
        Task("-- CDI"),
        Task("-- Test Specification"),
        Task("-- EVB Simulation S-parameter"),
        Task("-- fTEG Simulation S-parameter"),
        Task("MDR 提出"),
    ]
)

after_CAD_submission = Flow(
    gate=None,
    workflows=[
        Task("プローブ測定依頼書を SharePoint に格納"),
    ],
    skyfoundry=[],
    agile=[]
)

flows = [
    before_DR,
    before_CAD_submission,
    after_CAD_submission,
]

