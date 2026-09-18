# API Plan

Планируемые HTTP endpoints:

```text
GET    /events
GET    /events/{id}
POST   /events
DELETE /events/{id}
POST   /events/{id}/registrations
DELETE /events/{id}/registrations/{registration_id}
```

API планируется реализовать на одном из следующих этапов проекта.

## Формат данных

Клиент и сервер обмениваются данными в формате JSON. Для создания мероприятия клиент передаёт название и дату, а сервер возвращает объект с уникальным идентификатором.

## Коды ответа

- `200 OK` для успешного чтения;
- `201 Created` после создания;
- `404 Not Found`, если мероприятие не найдено.
