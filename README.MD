1 -Разверни проект
2 -cd Project {Local_Internet} - Если ты не находишься в этой дериктории
3 -Собери проект : -- docker build -t docker_image .
4 -Запусти в ручную команду : -- pip install --no-cache-dir -r requirements.txt
5 -Запусти контейнер -  -- docker run -it --rm docker_image pytest
6 -Если не запускается - Ничего страшного - У тебя видимо нет самого Docker
7 -Запусти тесты : pytest -m smoke