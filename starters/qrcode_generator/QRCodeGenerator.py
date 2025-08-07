import qrcode


class MyQRCode:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def create_qrcode(self, filename: str, fg: str, bg: str):
        user_input: str = input("Enter some text: ")
        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_colo=bg)
            qr_image.save(filename)

            print(f"Successfully created ({filename})")
        except Exception as e:
            print("Error", e)


def main():
    myqr = MyQRCode(30, 2)
    myqr.create_qrcode("my-repo.png",
                       fg='black',
                       bg='white')


if __name__ == "__main__":
    main()
