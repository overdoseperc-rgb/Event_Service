"""Simple command line prototype for Event Service."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "events.json"


def load_events() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_events(events: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(
        json.dumps(events, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def create_event(title: str, date: str) -> dict:
    events = load_events()
    event = {
        "id": max((item["id"] for item in events), default=0) + 1,
        "title": title,
        "date": date,
        "participants": [],
    }
    events.append(event)
    save_events(events)
    return event


def register_participant(event_id: int, participant: str) -> dict:
    events = load_events()
    for event in events:
        if event["id"] == event_id:
            event["participants"].append(participant)
            save_events(events)
            return event
    raise ValueError(f"Мероприятие с id={event_id} не найдено")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Event Service CLI")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("list", help="Показать мероприятия")

    create = commands.add_parser("create", help="Создать мероприятие")
    create.add_argument("title")
    create.add_argument("date")

    register = commands.add_parser("register", help="Зарегистрировать участника")
    register.add_argument("event_id", type=int)
    register.add_argument("participant")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "list":
        print(json.dumps(load_events(), ensure_ascii=False, indent=2))
    elif args.command == "create":
        print(json.dumps(create_event(args.title, args.date), ensure_ascii=False, indent=2))
    elif args.command == "register":
        try:
            result = register_participant(args.event_id, args.participant)
        except ValueError as error:
            raise SystemExit(str(error)) from error
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

