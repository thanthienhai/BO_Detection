import serial

def send_data(port, data):
    """
    Gửi dữ liệu qua cổng COM serial.

    Args:
        port: Cổng COM serial.
        data: Dữ liệu cần gửi.

    Returns:
        True nếu gửi dữ liệu thành công, False nếu không.
    """
    try:
        port.write(data)
        return True
    except Exception as e:
        print(f"Lỗi khi gửi dữ liệu: {e}")
        return False

def receive_data(port):
    """
    Nhận dữ liệu từ cổng COM serial.

    Args:
        port: Cổng COM serial.

    Returns:
        Dữ liệu nhận được.
    """
    try:
        data = port.read()
        return data
    except Exception as e:
        print(f"Lỗi khi nhận dữ liệu: {e}")
        return None

def main():
    # Cấu hình cổng COM
    port = serial.Serial("COM1", baudrate=9600)

    # Gửi dữ liệu
    data = b"Hello, world!"
    if not send_data(port, data):
        return

    # Nhận phản hồi
    response = receive_data(port)
    if response is None:
        return

    # In ra phản hồi
    print(response.decode())

if __name__ == "__main__":
    main()
