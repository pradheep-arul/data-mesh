

class Transformation():
    def __init__(self,
                 id,
                 name,
                 table,
                 schema,
                 db,
                 sql,
                 schedule,
                 owner,
                 metadata,
                 snapshot,
                 id_column,
                 execution_timeout,
                 priority,
                 refresh_type,
                 deduplicate,
                 notification_channel):
        self.id = id
        self.name = name
        self.table = table
        self.schema = schema
        self.db = db
        self.sql = sql
        self.schedule = schedule
        self.owner = owner
        self.metadata = metadata
        self.snapshot = snapshot
        self.id_column = id_column
        self.execution_timeout = execution_timeout
        self.priority = priority
        self.refresh_type = refresh_type
        self.deduplicate = deduplicate
        self.notification_channel = notification_channel


MOCK_TRANSFORMATION_DATA = [
    Transformation(1,
                   'salary_europe',
                   'salary_europe',
                   'dw',
                   'finance',
                   'select * from salary',
                   '0 * * * *',
                   'team-finance',
                   {
                       'tag': 'trans'
                   },
                   'weekly',
                   ['id'],
                   90,
                   1,
                   'incremental',
                   True,
                   '#team-finance',
                   )

]
