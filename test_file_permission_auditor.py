import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import audit

def row(p, mode, owner="root"):
    return {"path": p, "mode": mode, "owner": owner}

class TestPermissions(unittest.TestCase):
    def test_world_writable(self):
        self.assertEqual(audit([row("/tmp/x", "666")])[0][2], "WORLD-WRITABLE")
    def test_group_writable(self):
        self.assertEqual(audit([row("/srv/x", "664")])[0][2], "GROUP-WRITABLE")
    def test_ok(self):
        self.assertEqual(audit([row("/etc/x", "644")])[0][2], "OK")
    def test_highest_first(self):
        r = audit([row("/a", "644"), row("/b", "777")])
        self.assertEqual(r[0][0], "/b")
