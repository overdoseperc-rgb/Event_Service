import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app import cli


class EventServiceTests(unittest.TestCase):
    def test_create_and_register(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            data_file = Path(directory) / "events.json"
            with patch.object(cli, "DATA_FILE", data_file):
                created = cli.create_event("Конференция", "2026-11-20")
                updated = cli.register_participant(created["id"], "Анна")

            self.assertEqual(created["id"], 1)
            self.assertEqual(updated["participants"], ["Анна"])


if __name__ == "__main__":
    unittest.main()

