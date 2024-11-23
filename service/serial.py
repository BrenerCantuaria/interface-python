import time
import serial

baudrate = 115200  # Velocidade de comunicação
def open_serial_connection(port):
    try:
        serial_connection = serial.Serial(port, baudrate, timeout=1)
        return serial_connection, True
    except Exception as e:
        print(f"Erro ao abrir porta serial {port}: {e}")
        return None,False

# Essa função retorna um dicionário do python
def get_existing_data(serial_connection):
    print(f'porta: {serial_connection}')
    if serial_connection:
        try:
            serial_connection.write(b'getData\n')  # Comando enviado ao ESP32 para pedir os dados
            time.sleep(1)  # Dá tempo para o ESP32 responder
            existing_data = serial_connection.readline().decode().strip()
            """
                ->Este é um exemplo do que deve conter a variável existing_data:
                    'ESP32 Dev Kit,777-111-222'
                Ela deve conter o nome do dispositivo e o ID, separados por vírgula
            """
            # existing_data = 'ESP32 Dev Kit,777-111-222'
            if existing_data:
                # Supondo que os dados sejam separados por vírgula
                parts = existing_data.split(',')
                if len(parts) == 2:  # Certifique-se de que a string está no formato esperado
                    nome_dispositivo, id_retornado = parts
                    return {"nome": nome_dispositivo, "id": id_retornado}
            return None
        except Exception as e:
            print(f"Erro ao ler da porta serial: {e}")
            return None
    return None


def send_device_info(serial_connection, name, device_id):
    if serial_connection:
        try:
            # Cria a string de dados a ser enviada
            data_string = f"{name},{device_id}\n"
            serial_connection.write(data_string.encode())  # Envia nome e ID para o ESP32
            print("Dados enviados com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar dados para a porta serial: {e}")




