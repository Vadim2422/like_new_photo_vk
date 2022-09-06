import json
import vk_api.exceptions
import os

from server import keep_alive

keep_alive()

session = vk_api.VkApi(
    token=os.getenv('token'))


def main():
    with open('current_user.json', 'r') as file:
        users = json.load(file)['users']
    while True:
        for user in users:
            user_data = session.method("users.get", {'user_ids': user, 'fields': 'domain'})
            id = user_data[0]['id']
            photos = get_200(user_data[0]['id'])
            count = photos['count']
            if not count:
                print("user dont have a photo")

            for photo in photos['items']:
                if is_liked(id, photo['id'])['liked']:
                    break
                else:
                    print(like(photo['owner_id'], photo['id']))


def get_200(owner_id, offset=0):
    return session.method("photos.getAll", {
        'owner_id': owner_id,
        'count': 200,
        'offset': offset
    })


def is_liked(owner_id, item_id):
    return session.method("likes.isLiked", {
        'owner_id': owner_id,
        'type': 'photo',
        'item_id': item_id
    })


def like(owner_id, item_id):
    return session.method("likes.add", {
        'type': 'photo',
        'owner_id': owner_id,
        'item_id': item_id
    })


if __name__ == '__main__':
    main()
