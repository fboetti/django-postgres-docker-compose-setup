from polls.models import Question, Choice


ROUTED_MODELS = [
    Question,
    Choice,
]


class SchemaRouter:
    """
    A router to control database operations on models across different schemas.
    Not working as expected.
    """

    def db_for_read(self, model, **hints):
        # Models read from their respective database
        if model._meta.db_table.startswith('polls.'):
            return 'polls'
        return None
    
    def db_for_write(self, model, **hints):
        # Models write to their respective database
        if model._meta.db_table.startswith('polls.'):
            return 'polls'
        return None
