# Публикация на GitHub

Архив уже содержит папку `.git`, историю коммитов и ветки. Не запускайте `git init` повторно.

## 1. Создание репозитория

На GitHub создайте пустой публичный репозиторий `event-service`. Не добавляйте на сайте README, `.gitignore` и лицензию.

## 2. Подключение GitHub

Откройте Git Bash в распакованной папке проекта и выполните:

```bash
git remote add origin https://github.com/ВАШ_ЛОГИН/event-service.git
git push -u origin main
git push origin --all
```

Если `origin` уже добавлен с неправильным адресом:

```bash
git remote set-url origin https://github.com/ВАШ_ЛОГИН/event-service.git
```

## 3. Проверка

```bash
git branch -a
git log --oneline --all --graph --decorate
```

На GitHub откройте `Insights`, затем `Network`. Сделайте скриншот графа, сохраните его в корне проекта под именем `git-network.png`, затем выполните:

```bash
git add git-network.png
git commit -m "docs: add GitHub network graph"
git push
```

Для сдачи отправьте преподавателю публичную ссылку на репозиторий.

