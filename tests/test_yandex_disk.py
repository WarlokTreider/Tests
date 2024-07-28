import pytest
from yandex_disk import YandexDisk


@pytest.fixture
def yandex_disk():
    token = "Замените на ваш токен"
    return YandexDisk(token)


def test_create_folder_success(yandex_disk):
    folder_path = "test_folder"

    # Удаляем папку, если она существует
    response = yandex_disk.get_folder(folder_path)
    if response.status_code == 200:
        yandex_disk.delete_folder(folder_path)

    # Пытаемся создать папку
    response = yandex_disk.create_folder(folder_path)
    assert response.status_code == 201

    # Проверяем, что папка была создана
    response = yandex_disk.get_folder(folder_path)
    assert response.status_code == 200


def test_create_folder_already_exists(yandex_disk):
    folder_path = "test_folder"

    # Создаем папку, если она не существует
    response = yandex_disk.get_folder(folder_path)
    if response.status_code == 404:
        yandex_disk.create_folder(folder_path)

    # Пытаемся создать папку еще раз
    response = yandex_disk.create_folder(folder_path)
    assert response.status_code == 409


def test_create_folder_invalid_path(yandex_disk):
    invalid_folder_path = "///invalid///folder///path"

    # Пытаемся создать папку с некорректным путем
    response = yandex_disk.create_folder(invalid_folder_path)
    assert response.status_code in [400, 404, 409]  
