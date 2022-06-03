# Data-Cleaning
Данный репозитория является библиотекой функция для работы в Colab

Для того чтобы использовать в своём Colab

Добавление своих библиотек
```
!git clone https://github.com/MikeSaltykov07/Data-Cleaning
import sys
sys.path.append('/content/Data-Cleaning/')
from data_clean import type_clean
```
Обновление своих проектов github
```
!git config --global user.email "YOUR_EMAIL"
!git config --global user.name "YOUR_PROFILE"
!git add . 
!git commit -m "colab first commit"
!git push https://<YOUR_TOKEN_GITHUB>@github.com/YOUR_PROFILE/YOUR_PROJECT
```