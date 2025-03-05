import unittest
from unittest.mock import patch
import types
from importlib import machinery

from dynamic.dynamic_loader import DynamicClassFinder, DynamicClassLoader
from dynamic.source_grabbers import SourceGrabber

    @patch.object(SourceGrabber, "fetch_source")
    @patch("google.cloud.storage.Client.get_bucket")
    @patch("google.cloud.storage.Blob.download_as_text")
    def test_cloud_storage_fetch_source(self, mock_download, mock_bucket):
        mock_bucket.return_value.blob.return_value.download_as_text.return_value = "code"
        cloud_storage = CloudStorage(bucket="test_bucket")
        self.assertEqual(cloud_storage.fetch_source("test"), "code")
    
    @patch("google.cloud.secretmanager.SecretManagerServiceClient.secret_version_path")
    @patch("google.cloud.secretmanager.SecretManagerServiceClient.access_secret_version")
    def test_secret_manager_fetch_source_success(self, mock_secret, mock_client):
        mock_client.return_value.secret_version_path.return_value = "test_secret"
        mock_client.return_value.access_secret_version.return_value.payload.data.decode.return_value = "code"
        secret_manager = SecretManager()
        self.assertEqual(secret_manager.fetch_source("test_secret"), "code")

    @patch("google.cloud.secretmanager.SecretManagerServiceClient.secret_version_path")
    @patch("google.cloud.secretmanager.SecretManagerServiceClient.access_secret_version")
    def test_secret_manager_fetch_source_error(self, mock_secret, mock_client):
        mock_client.return_value.secret_version_path.side_effect = Exception("Error")
        secret_manager = SecretManager()
        self.assertIsNone(secret_manager.fetch_source("test_secret"))

    @patch("builtins.open")
    def test_local_storage_fetch_source_success(self, mock_open):
        mock_open.return_value.read.return_value = "code"
        local_storage = LocalStorage(folder="test_folder")
        self.assertEqual(local_storage.fetch_source("test"), "code")
    
    @patch("sys.meta_path.append")
    @patch("dynamic.dynamic_loader.import_module")
    @patch("dynamic.dynamic_loader.reload")
    def test_dynamic_class_install(self, mock_reload, mock_import, mock_append):
        class MockStorage(SourceGrabber):
            def fetch_source(self, source: str, **kwargs: Mapping[str, Any]) -> str:
                return "code"
        class MockDynamicClass(DynamicClass):
            def run(self, **attributes: Mapping[str, str]) -> Any:
                return "result"
        mock_append.return_value = None
        mock_import.return_value = MockDynamicClass
        mock_reload.return_value = MockDynamicClass
        result = DynamicClass.install(module_name="test", class_name="Class", storage=MockStorage, bucket="bucket_test", folder="folder_test")
        self.assertEqual(result, MockDynamicClass)
        self.assertEqual(len(sys.meta_path), 1)

    def test_dynamic_class_run(self):
        class MockDynamicClass(DynamicClass):
            def run(self, **attributes: Mapping[str, str]) -> Any:
                return "result"
        mock_dynamic_class = MockDynamicClass()
        self.assertEqual(mock_dynamic_class.run(), "result")
