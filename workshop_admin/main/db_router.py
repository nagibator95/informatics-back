class PynformaticsRouter:
    def __init__(self):
        self._models = {
            'WorkshopConnection',
            'Workshop',
            'ContestConnection',
            'Contest',
        }

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'main':
            return 'pynformatics'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'main':
            return 'pynformatics'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'main' or \
           obj2._meta.app_label == 'main':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
