#!/bin/bash

# Переходимо в кореневу папку
cd /usr/share/nginx/html

# 1. Ініціалізація Git та налаштування користувача (потрібно для комітів)
git init

# Встановлюємо фіктивні дані користувача, щоб коміти були можливі
git config user.email "dev@ctf-donntu.local"
git config user.name "CTF Developer"

# 2. Перший коміт (базова сторінка)
git add index.html
git commit -m "Initial commit: setting up the homepage"

# 3. Створення та коміт прапора (ВРАЗЛИВІСТЬ)
echo "The flag is FLAG{flag_placeholder}" > secret_flag.txt
git add secret_flag.txt
git commit -m "Added secret flag file temporarily"

# 4. Видалення файлу з прапором та фінальний коміт
rm secret_flag.txt
git add secret_flag.txt # Додаємо видалення до staging area
git commit -m "Removed secret_flag file"
