from django.core.files.storage import FileSystemStorage
from django.db.models.fields.files import FieldFile

class ForgeStorage(FileSystemStorage):

    def get_available_name(self, name):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # Clobber existing files, or else will get filenames that won't
        # comply with the module naming format.
        if self.exists(name):
            self.delete(name)
        return name

def file_cleanup(sender, instance, *args, **kwargs):
    '''
        Deletes the file(s) associated with a :model instance. The model
        is not saved after deletion of the file(s) since this is meant
        to be used with the pre_delete signal.
    '''
    for field_name, _ in instance.__dict__.iteritems():
        field = getattr(instance, field_name)
        if issubclass(field.__class__, FieldFile) and field.name:
            field.delete(save=False)