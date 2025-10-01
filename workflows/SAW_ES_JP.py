from .models import Task, Flow
from services.email import create_POreq_mailto


flows = [
    Flow(
        gate=Task("Design Review 実施"),
        items={
            "Workflow": [
                Task("Design Review 会議設定"),
                Task("SAP 登録シートを記入して担当者に連絡"),
                Task("Design Review Check"),
            ],
            "SkyFoundry": [
                Task("プロセスバリアントとファイルの詳細", link="https://www.nissan.co.jp/"),
                Task("Die Map/Mask Lauout リクエスト"),
                Task("1S/PCM リクエスト"),
                Task("Process Recipe リクエスト"),
                Task("マスク/レイヤ"),
            ],
            "Agile": [],
        }
    ),
    Flow(
        gate=Task("CAD 提出"),
        items={
            "Workflow": [
                Task("PO 発行依頼", link=create_POreq_mailto(), icon=":material/email:"),
                Task("マニュアルチェック依頼"),
                Task("マニュアルチェック実施"),
                Task("Mask Assembly Utility 実施"),
                Task("RDS サーバに HFSS/SNSS ファイルを格納"),
            ],
            "SkyFoundry": [
                Task("PO 入力"),
                Task("Manual Layout Check 登録"),
                Task("Waiver"),
            ],
            "Agile": [
                Task("MDR 作成"),
                Task("-- CDI"),
                Task("-- Test Specification"),
                Task("-- EVB Simulation S-parameter"),
                Task("-- fTEG Simulation S-parameter"),
                Task("MDR 提出"),
            ]
        }
    ),
    Flow(
        gate=None,
        items={
            "Workflow": [
                Task("プローブ測定依頼書を SharePoint に格納"),
            ],
            "SkyFoundry": [],
            "Agile": [],
        }
    )
]

