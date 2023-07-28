import matplotlib.pyplot as plt
import cv2

def plot_gray(image):
    plt.figure(figsize=(16,10))
    return plt.imshow(image, cmap='Greys_r')


def plot_rgb(image):
    plt.figure(figsize=(16,10))
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def content_str_to_dict(content_str):
    content_list = content_str.split('\n')
    content_list = content_list[1:-1]

    content_list = [{'Name': content.split(' -> ')[0], 'Price': content.split(' -> ')[1]} for content in content_list]

    price_list = [content['Price'] for content in content_list]

    total_price = 0
    for price in price_list:
        try:
            price_int = int(price)
        except:
            pass

        total_price = total_price + price_int

    content_dict = {
        'Total': total_price,
        'Items': content_list
    }

    return content_dict