# Schedule App

Веб-приложение для просмотра и фильтрации расписания.

## Деплой на GitHub Pages

1. Создай новый репозиторий на GitHub, например `schedule-app`.
2. В настройках репозитория включи **GitHub Pages**:
   - Settings → Pages
   - Source: выбери `main` branch и `/ (root)`
3. Склонируй репозиторий и скопируй файлы:
   ```bash
   git clone https://github.com/<username>/schedule-app.git
   cd schedule-app
   cp /path/to/index.html .
   cp /path/to/README.md .
   git add .
   git commit -m "init"
   git push
   ```
4. Через 1–2 минуты сайт будет доступен по адресу:
   `https://<username>.github.io/schedule-app/`
