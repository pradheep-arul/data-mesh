
MOCK_DAG_DATA = [
    {
        "name": "import.intercom.conversations",
        "description": "Imports conversations object from Intercom",
        "source_file": "dags/intercom-import.py",
        "schedule": "1 * * * *",
        "max_run": 1,
        "owner": "finance",
        "tags": {
            "category": "import",
            "source": "intercom"
        },
        "notification_channel": "team-finance",
        "priority": 2,
        "execution_timeout": 60,
        "tasks": [
            {
                "name": "collection",
                "description": "Collects the data from conversations",
                "upstream": [
                ],
                "downstream": [
                    "copy_to_snowflake"
                ],
                "pool": "intercom_import",
                "retries": 3,
                "execution_timeout": 60
            },
            {
                "name": "copy_to_snowflake",
                "description": "Collects the data from conversations",
                "upstream": [
                    "collection"
                ],
                "downstream": [
                    "move_to_processed"
                ],
                "pool": "intercom_import",
                "retries": 3,
                "execution_timeout": 60
            },
            {
                "name": "move_to_processed",
                "description": "Collects the data from conversations",
                "upstream": [
                    "copy_to_snowflake"
                ],
                "downstream": [
                ],
                "pool": "intercom_import",
                "retries": 3,
                "execution_timeout": 60
            }
        ]
    }
]

MOCK_DAG_BACKFILL_DATA = [
    {
        "dag_run_id": "backfill__2023-02-03T00:00:00+00:00",
        "dag_id": "import.intercom.conversations"
    },
    {
        "dag_run_id": "backfill__2023-02-03T00:00:00+00:00",
        "dag_id": "import.intercom.conversations"
    }
]

MOCK_DAG_TRIGGER_DATA = {
    "dag_run_id": "manual__2023-02-03T00:00:00+00:00",
    "dag_id": "import.intercom.conversations"
}
