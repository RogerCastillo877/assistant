from pathlib import Path
import tempfile
import unittest

from implementation.validators.validate_document_references import validate_related_documents


class DocumentReferenceValidationTests(unittest.TestCase):
    def test_rejects_file_style_related_document_entries(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            sample = Path(tmp_dir) / "sample.md"
            sample.write_text(
                "Related Documents:\n  - 101-OSEF-Specification.md\n",
                encoding="utf-8",
            )

            errors = validate_related_documents([sample])

            self.assertTrue(errors)
            self.assertIn("must use a document ID", errors[0])

    def test_accepts_document_id_references(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            sample = Path(tmp_dir) / "sample.md"
            sample.write_text(
                "Related Documents:\n  - OSEF-SPE-101\n  - OSEF-CPR-001\n",
                encoding="utf-8",
            )

            errors = validate_related_documents([sample])

            self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
