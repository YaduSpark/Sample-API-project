class CheckRouter:
    def db_for_read(self,model):
        if model._meta.app_label == "products":
            return 'mongoDB'
        return 'default'

    def db_for_write(self,model):
        if model._meta.app_label == "products":
            return 'mongoDB'
        return 'default'