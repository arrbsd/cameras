from models.keno import CameraSettingsAPI


camera_ip = 'http://192.168.1.188'
username = 'admin'
password = ''

camera = CameraSettingsAPI(camera_ip, username, password)
camera_info = camera.get_device_para()
camera_time = camera.get_device_time()
camera_network = camera.get_network_settings()

print(camera_network)



