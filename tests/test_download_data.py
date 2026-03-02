import os
import unittest
from unittest.mock import MagicMock, patch

from download_data import download_and_extract


class TestDownloadAndExtract(unittest.TestCase):
	@patch("download_data.zipfile.ZipFile")
	@patch("download_data.requests.get")
	@patch("download_data.os.path.exists", return_value=False)
	def test_successful_download_and_extract(
		self, mock_exists, mock_get, mock_zipfile
	):
		url = "https://example.com/data.zip"
		extract_to = "data"

		mock_response = MagicMock()
		mock_response.status_code = 200
		mock_response.content = b"fake zip bytes"
		mock_get.return_value = mock_response

		zip_context = MagicMock()
		mock_zipfile.return_value.__enter__.return_value = zip_context

		result = download_and_extract(url, extract_to=extract_to)

		mock_exists.assert_called_once_with(os.path.join(extract_to, "Online Retail.xlsx"))
		mock_get.assert_called_once_with(url)
		mock_zipfile.assert_called_once()
		zip_context.extractall.assert_called_once_with(extract_to)
		self.assertEqual(result, os.path.abspath(extract_to))

	@patch("download_data.zipfile.ZipFile")
	@patch("download_data.requests.get")
	@patch("download_data.os.path.exists", return_value=False)
	def test_unsuccessful_download(
		self, mock_exists, mock_get, mock_zipfile
	):
		url = "https://example.com/data.zip"

		mock_response = MagicMock()
		mock_response.status_code = 404
		mock_response.content = b""
		mock_get.return_value = mock_response

		result = download_and_extract(url)

		mock_exists.assert_called_once()
		mock_get.assert_called_once_with(url)
		mock_zipfile.assert_not_called()
		self.assertIsNone(result)


if __name__ == "__main__":
	unittest.main()
