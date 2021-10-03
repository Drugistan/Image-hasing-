from test import ImageHashHandler

def main():
    handler = ImageHashHandler("/home/dar-night/PythonProjectideas/MiniprojectsForItself", ".jpg")
    handler.get_all_hash()
    handler.print_all()



if __name__ == "__main__":
    main()
