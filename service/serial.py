import serial
import time

baudrate = 115200  # Velocidade de comunicação
def open_serial_connection(port):
    try:
        return f'porta {port}'
        serial_connection = serial.Serial(port, baudrate, timeout=1)
        return serial_connection
    except Exception as e:
        print(f"Erro ao abrir porta serial {port}: {e}")
        return None

def get_existing_id(serial_connection = True):
    if serial_connection:
        try:
            return [{"id": None, 'nome_dispositivo': "ESP32 Dev Kit"}]
            serial_connection.write(b'getID\n')  # Comando enviado ao ESP32 para pedir o ID
            time.sleep(1)  # Dá tempo para o ESP32 responder
            existing_id = serial_connection.readline().decode().strip()
            return existing_id
        except Exception as e:
            print(f"Erro ao ler da porta serial: {e}")
            return None
    return None

def send_device_info(serial_connection, name, device_id):
    if serial_connection:
        try:
            # Cria a string de dados a ser enviada
            data_string = f"{name},{device_id}\n"
            return data_string
            serial_connection.write(data_string.encode())  # Envia nome e ID para o ESP32
            print("Dados enviados com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar dados para a porta serial: {e}")




