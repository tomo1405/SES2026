import os
import random

from src_0746 import task_func


def test_task_func():
    script_name = random.choice(SCRIPTS)
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    assert task_func() == script_path