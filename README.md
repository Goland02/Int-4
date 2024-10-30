# Int 4
 
В папке Int 4.1 находится ansible playbook для базовой настройки debian 11 и установки на него postgresql 16 Для корректной работы нужно в файле inventory.yaml изменить адрес хоста debian11 на нужный вам Также в файле playbook.yaml нужно изменить значение переменной postgres_passwd на нужное вам. Эта переменная - это пароль для пользователся postgres, для работы с postgresql Также в папке присутствует файл конфигурации ansible.cfg, содержащий конфиги, необходимые для работы playbook

В папке Int 4.2 находятся файл http сервера server.py и Dockerfile (для того чтобы этот сервер развернуть) Собираем образ командой docker build -t python-server . Запускаем контейнер командой docker run -d --name python_server -p 80:80 python-server При запросе http://localhost/healthz (либо по ip адресу сервера) получим код 200 OK, при любом другом пути получим 404 Not Found

В папке Int 4.3 находятся конфиг файлы для blackbox-exporter и prometheus В файле blackbox.yml описана конфигурация для генерации проб по протоколу http, в файле prometheus.yml описан конфиг для использования blackbox-exporter для сбора метрик доступности https://ptsecurity.com
