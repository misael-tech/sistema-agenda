import os

from storages.backends.s3 import S3Storage


class SupabaseStorage(S3Storage):

    def url(self, name, parameters=None, expire=None, http_method=None):
        base_url = os.getenv("SUPABASE_PUBLIC_URL")

        return f"{base_url}/{name}"