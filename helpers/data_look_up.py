import json
from pathlib import Path
from typing import Any, Dict, List
from collections import Counter


def load_data(root: Path):
    data: List[Dict[str, Any]] = list()
    for file in root.iterdir():
        if file.is_dir():
            continue
        if not file.name.endswith(".json"):
            continue
        file_data = json.loads(file.read_text())
        data.append(
            {
                "request_id": file.name,
                "result": file_data.get("result", "unknown"),
                "strategy_name": file_data.get("strategy_name", "unknown"),
            }
        )
    return data


def main():
    project_root = Path(__file__).parent.parent
    test_result_folder = project_root / "test_result"
    data = load_data(test_result_folder)
    strategies_counter: Counter[str] = Counter()

    for item in data:
        strategies_counter[item["strategy_name"]] += 1

    print(strategies_counter)


if __name__ == "__main__":
    main()
